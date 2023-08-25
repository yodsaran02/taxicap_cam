import cv2
import numpy as np
import tensorflow as tf

# Load the pre-trained object detection model (TensorFlow Object Detection API)
model = tf.saved_model.load('path_to_your_model')

# Load and preprocess the image
image = cv2.imread('image_path')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB
input_tensor = tf.convert_to_tensor(image)

# Run object detection
detections = model(input_tensor)

# Post-process the detections to get bounding boxes
# Filter detections based on confidence threshold and class labels

# Extract and save the numbers
for detection in filtered_detections:
    x, y, w, h = detection['bbox']
    number_image = image[y:y+h, x:x+w]
    cv2.imwrite('number_{}.png'.format(some_counter), number_image)
    some_counter += 1
