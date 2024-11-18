#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing librairies
from ultralytics import YOLO
import cv2
import pytesseract
from PIL import Image
import os


# In[ ]:


# Initializing the YOLOv8 model
model = YOLO('yolov8s.pt')

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[ ]:


def ocr_license_plate(cropped_image):

    # Converting cropped image to PIL format for pytesseract
    img = Image.fromarray(cropped_image)
    text = pytesseract.image_to_string(img, config='--psm 8')  # psm 8 is for single word OCR
    return text.strip()


# In[ ]:


def detect_license_plates(image_path):

    # Perform detection on the image
    results = model(../data/images)

    # Process each detection
    for result in results:
        boxes = result.boxes  # Bounding boxes
        
        # Loop over all detected boxes
        for box in boxes:
            xyxy = box.xyxy[0].cpu().numpy()  # Get coordinates of bounding box
            conf = box.conf[0].cpu().numpy()  # Confidence score

            # We are going to process only license plates
            if class_id == 0:
                x1, y1, x2, y2 = map(int, xyxy)  # Integer coordinates of the bounding box
                print(f"Detected license plate with confidence {conf:.2f} at [{x1}, {y1}, {x2}, {y2}]")

                # Cropping the license plate from the image
                img = cv2.imread(image_path)
                cropped_plate = img[y1:y2, x1:x2]

                # OCR to read the license plate text
                plate_text = ocr_license_plate(cropped_plate)
                print(f"Detected License Plate Text: {plate_text}")

    return results


# In[ ]:


# Testing on all images in a the test floder
test_image_folder = 'data/test'  # Folder containing images for testing

for image_name in os.listdir(test_image_folder):
    if image_name.lower().endswith('.png'):
        image_path = os.path.join(test_image_folder, image_name)
        print(f"Processing image: {image_name}")
        
        # Perform detection and OCR
        detect_license_plates(image_path)

