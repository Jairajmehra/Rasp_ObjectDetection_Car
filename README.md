# Raspberry pi Line following car with Object Detection
This is my university project for a subject named embedded systems. The idea is to make a prototype of a system that can be embedded into
existing vacuum robots. The system would enable user to locate lost objects that come in reach of vacuum robot.

I am using tensorflow api with faster_rcnn_inception_v2_coco which seemed to be the perfect balance between speed and accuracy.
Currently I have trained the model on only three objects but it is quite accurate. I have written a class which store images with 
names of objects detected in them along with a unique ID and can also retrieve 3 newest images when searched with a right object name. 
The search functionality is used via a web interface. This is almost complete but the code needs little improvements.

This is a link to see my project in action - https://video.deakin.edu.au/media/t/0_qc26jme1

Little more in depth explanation of the project - https://video.deakin.edu.au/media/t/0_sc0iikf3

To run the program you will need: 
1)	Install TensorFlow v1.5 on pc.
2)	Install OpenCV on raspberry pi as well as pc.
3)	Flask only on pc.
4)	Pickle only on pc.
5)	Numpy only on pc.
6)	Pathlib only on pc.
7)	PIL  only on pc.

In the folder named “code for raspberry pi” contains all the code that directly runs on a raspberry pi car.
1)	On raspberry pi run main.py which will run everything else as needed. 
2)	On pc create a folder named “images” and another named "static" in the same directory as all the other files and copy all the images from ‘test images’ folder to ‘images‘ folder. 
3)	Run main.py on pc, it will start object detection and images inside the ‘images’ folder will be saved in static folder with corresponding object name along with a unique ID. I have commented out the server lines in main.py but that can be uncommented if connecting a client.
4)	Run webserver.py on pc. 



