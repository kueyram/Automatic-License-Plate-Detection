# Automatic License Plate Recognition (ALPR) using OCR
This project demonstrates how to automatically read vehicle license plates using Optical Character Recognition (OCR) and object detection technologies. The goal is to improve the accuracy and speed of license plate recognition, with applications in parking management, toll collection, and security systems.


## Table of content
- [Project Overview](#project-overview)
- [Installation](#Installation)
- [Usage](#usage)
    - [Training the Model](#train-the-model)
    - [Running License Plate Recognition](#run-the-license-plate-recognition)
    - [Evaluating Performance](#evaluate-performance)
    - [License Plate Detection] (#license-plate-detection)

- [License](#license)


## Project Overview

The goal of this project is to develop a system that can:
    - Detect license plates in images of vehicles.
    - Extract the characters from the detected license plates using OCR.
    - Provide real-time, accurate license plate recognition for applications like parking management, toll booths, and security gates.

## Installation
To run this project, you need to have Python installed on your machine. Additionally, you need to install the required libraries. You can do this using pip:

```bash
pip install -r requirements.txt

```
## Usage
1. ### Clone the repository

```bash
git clone https://github.com/your_username/ALPR-project.git
cd ALPR-project

```
2. ### Train the model:
 To train the YOLOv8 model on the dataset, use the following command:

```bash
python train.py --data data.yaml --epochs 50
```

3. ### Run the License Plate Recognition
Once the model is trained, run the license plate recognition on a new image:
```bash
python recognize.py --image path_to_image.jpg
```

4. ### Evaluate Performance:
To evaluate the system's performance on the validation dataset, use:
```bash
python evaluate.py --data data.yaml
```

# License Plate Detection

YOLOv8 is used for detecting the license plates in images. It is trained to detect bounding boxes around the license plates, allowing the system to focus on the relevant area of the image for OCR.
OCR for Text Recognition

After detecting the license plates, EasyOCR is used to extract the text from the plates.

# Performance Evaluation

The system is evaluated based on:

    Precision: The proportion of correct detections out of all detected plates.
    Recall: The proportion of actual plates correctly detected.
    F1-Score: A combined metric of precision and recall.
    Mean Average Precision (mAP): A measure of the accuracy of the object detection model.
    Processing Speed: The time taken to process each image, ensuring the system can work in real-time applications.

# License

This project is licensed under the MIT License.