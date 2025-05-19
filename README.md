# 🐆 Cheetah Detection from Thermal Images

Automated detection of cheetahs from thermal remote sensing images for wildlife monitoring and conservation.

## 📌 Project Overview

Monitoring wild animal populations is crucial for biodiversity conservation. Traditional methods are often labor-intensive and limited in scale. In this project, we develop an object detection pipeline to automatically detect cheetahs in thermal imagery, using deep learning techniques and remote sensing data.

## 📂 Dataset

We use the **Cheetah Thermal Dataset** provided by the [Roboflow](https://roboflow.com/) team.

- Format: Images + COCO/YOLO annotations
- Modalities: Thermal infrared images
- Classes: `cheetah`

🔗 **Dataset Access**: [Roboflow Cheetah Dataset (Thermal)](https://universe.roboflow.com/)  
(*You may need to create an account to access the dataset.*)

## 🧠 Model

We use an object detection model such as:
- [YOLOv8](https://github.com/ultralytics/ultralytics)

You can experiment with different backbones and training strategies.

## 🚀 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/cheetah-detection-thermal.git
    cd cheetah-detection-thermal
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    conda create -n cheetah-env python=3.9 -y
    conda activate cheetah-env
    pip install -r requirements.txt
    ```

3. Download dataset from Roboflow and place it in the `data/` directory.

## 🏃‍♀️ Usage

### 1. Training
```bash
python train.py --data data/cheetah.yaml --img 640 --batch 16 --epochs 50 --weights yolov5s.pt
```