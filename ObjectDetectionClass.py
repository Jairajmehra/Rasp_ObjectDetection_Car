
import  cv2, os, sys
import label_map_util
import tensorflow as tf
import numpy as np
from StoreSearchClass import store_Search
from utils import visualization_utils as vis_util
import threading
from pathlib import Path
import time
class ObjectDetection(threading.Thread):
    def __init__(self, num_class):
        threading.Thread.__init__(self)
        self.map = {1:"bottle", 2:"speaker", 3:"scissors"}
        self.current_Path = os.getcwd()
        self.Load_from_location = os.path.join(self.current_Path, 'images') 
        self.Store_Search = store_Search(os.path.join(self.current_Path, 'static')) 
        self.NUM_CLASSES = num_class
        self.PATH_TO_LABELS = os.path.join(self.current_Path,'labelmap.pbtxt')
        self.label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        self.PATH_TO_CKPT = os.path.join(self.current_Path,'frozen_inference_graph.pb')
        self.categories = label_map_util.convert_label_map_to_categories(self.label_map, max_num_classes=self.NUM_CLASSES, use_display_name=True)
        self.category_index = label_map_util.create_category_index(self.categories)


    def run(self):
        print("Loading TensorFlow")
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        self.sess = tf.Session(graph=detection_graph)
        self.image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        self.detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
        self.detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = detection_graph.get_tensor_by_name('num_detections:0')
        self.Stop = False
        self.ExtractImage()

    def ExtractImage(self):
        while(self.Stop ==  False):
            items = Path(self.Load_from_location).glob("*.png")
            items = list(items)
            size = len(items)
            if(size > 0):
                for x in items:

                    name = os.path.basename(x)
                    imagepath = os.path.join(self.Load_from_location, name)
                    image = cv2.imread(imagepath)
                    self.Detect(image)
                    os.remove(imagepath)

            else:
                print("no images left to detect, waiting for new images")
                time.sleep(60)
                

    def Detect(self,frame):
        self.frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.frame_expanded = np.expand_dims(self.frame_rgb, axis=0)
        (boxes, scores, classes, num) = self.sess.run([self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],feed_dict={self.image_tensor: self.frame_expanded})
        vis_util.visualize_boxes_and_labels_on_image_array(
        frame,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        self.category_index,
        use_normalized_coordinates=True,
        line_thickness=8,
        min_score_thresh=0.60)
        scores = scores[0][:3]
        classes = classes[0][:3]
        name = ""
        seen = []
        for x in range(3):
            if(scores[x]>0.6 and (not classes[x]  in seen)):
                name += f'{self.map[classes[x]]}&'
                seen.append(classes[x])
        if(name):
            print('Object Detected saving image')
            self.Store_Search.SaveDetected(frame, name) 
    
