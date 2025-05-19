import argparse
from ultralytics import YOLO
import os

def detect(opt):
    # Load YOLOv8 model
    model = YOLO(opt.weights)

    # Run inference
    results = model.predict(
        source=opt.source,
        conf=opt.conf,
        save=True,
        project=opt.project,
        name=opt.name,
        show=opt.show,
        save_txt=opt.save_txt,
        save_crop=opt.save_crop,
        line_thickness=2
    )

    print(f"Inference complete. Results saved to {os.path.join(opt.project, opt.name)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='best.pt', help='Path to model weights')
    parser.add_argument('--source', type=str, default='data/test', help='Image/video path or directory')
    parser.add_argument('--conf', type=float, default=0.25, help='Confidence threshold')
    parser.add_argument('--project', type=str, default='runs/detect', help='Save directory')
    parser.add_argument('--name', type=str, default='exp', help='Name of the experiment')
    parser.add_argument('--show', action='store_true', help='Show results during inference')
    parser.add_argument('--save_txt', action='store_true', help='Save results to *.txt')
    parser.add_argument('--save_crop', action='store_true', help='Save cropped prediction boxes')

    opt = parser.parse_args()
    detect(opt)
