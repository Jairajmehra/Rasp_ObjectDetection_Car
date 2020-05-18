# Raspberry pi Line following car with Object Detection
This is my university project for a subject named embedded systems. The idea is to make a prototype of a system that can be embedded into
existing vacuum robots. The system would enable user to locate lost objects that come in reach of vacuum robot.

I am using tensorflow api with faster_rcnn_inception_v2_coco which seemed to be the perfect balance between speed and accuracy.
Currently I have trained the model on only three objects but it is quite accurate. I have written a class which store images with 
names of objects detected in them along with a unique ID and can also retrieve 3 newest images when searched with a right object name. 
The search functionality is used via a web interface. This is almost complete but the code needs little improvements.

This is a link to see my project in action - https://video.deakin.edu.au/media/t/0_qc26jme1

Little more in depth explanation of the project - https://video.deakin.edu.au/media/t/0_sc0iikf3

