import cv2
import numpy as np


# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
#set an empty array that will be used to check what objects to use for later
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()] #add all the recognizable objects into the prior array
layer_names = net.getLayerNames() #getLayerNames gives an index of amount of layers in the neural network
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()] #this gets the final layer(s)
colors = np.random.uniform(0, 255, size=(len(classes), 3))


# Loading image
img = cv2.imread("image6.jpg")
img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channels = img.shape #this gets the height width and how many primary colors fill the colorspace ie 2 for B/W 3 for BGR

# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
 # blob is esentally a accessable collection of parameters of the image, height,width
 # depth/channels which gives the ability to process the entire base image in bulk

 # blobFromImage(inputImage, scaleFactor, size, mean, swapRB, crop)
 # scale factor: default 1, is used to scale the image
 # size: spatial size of output image
 # mean: scalar with mean values which are subtracted from channels.
 #       Values are intended to be in (mean-R, mean-G, mean-B) order
 #       if image has BGR ordering and swapRB is true.
 # swapRB: is used in regards to the previous parameter
 # crop: crop after any scaling or resizing

net.setInput(blob)
outs = net.forward(output_layers) #this runs the net against the processed image, detects any possible objects


# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs: #for one output/node in the net
    for detection in out: #for one detection of output/node
        scores = detection[5:] #get everything thats not center_x,center_y, w, h, x, y
        class_id = np.argmax(scores) #get the highest score
        confidence = scores[class_id] #check the highest object confidence
        if confidence > 0.5: #if the confidence is greater then 50%
            # Object detected
            center_x = int(detection[0] * width) #go to center of y of object
            center_y = int(detection[1] * height) #go to center of x of object
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)

font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i-11]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
