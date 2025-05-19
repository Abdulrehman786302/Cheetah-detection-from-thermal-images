# 🐆 Cheetah Detection from Thermal Images

Automatically detect cheetahs in thermal imagery using state-of-the-art object detection models (YOLOv8) to support wildlife conservation and monitoring.

## 📌 Project Overview

Conservation efforts require accurate data on animal populations. Manual monitoring is time-consuming and often impractical at large scales. This project provides an automated pipeline to detect cheetahs in thermal infrared imagery using a deep learning-based object detection model.

## 📂 Dataset

We use a thermal cheetah dataset provided by **[Roboflow](https://roboflow.com/)**.

- Format: JPG/PNG thermal images with YOLO annotations
- Class: `cheetah`
- Use Roboflow export options to download in YOLOv8 format

### 🔗 Dataset Access:
You can access and download the dataset [here](https://universe.roboflow.com/) (search for "cheetah thermal").

## 🧠 Model

We use the [YOLOv8](https://github.com/ultralytics/ultralytics) object detection model from Ultralytics, which is fast, accurate, and easy to use.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cheetah-detection-thermal.git
   cd cheetah-detection-thermal
    ```
2. Create a virtual environment and install dependencies:
```bash
conda create -n cheetah-env python=3.9 -y
conda activate cheetah-env
pip install ultralytics
```
3. Download the dataset from Roboflow and place it inside the data/ folde
## 🚀 Training
Train YOLOv8 on your dataset:
```bash
yolo task=detect mode=train data=data/cheetah.yaml model=yolov8s.pt epochs=50 imgsz=640
```

## 🔍 Inference
Run inference on a folder of images or a video using detect.py:
```bash
python detect.py --weights runs/detect/train/weights/best.pt --source data/test --conf 0.3 --show
```