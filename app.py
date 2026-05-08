import gradio as gr
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

model = YOLO("yolov8n.pt")

def count_objects(image):
    # convert PIL to numpy array
    img_array = np.array(image)
    
    results = model(img_array, verbose=False)
    annotated = results[0].plot()
    
    # count objects by class
    counts = {}
    for box in results[0].boxes:
        class_id = int(box.cls)
        class_name = model.names[class_id]
        counts[class_name] = counts.get(class_name, 0) + 1
    
    # build a clean summary string
    if counts:
        summary = "\n".join([f"{name}: {count}" for name, count in counts.items()])
    else:
        summary = "No objects detected"
    
    # convert back to PIL for Gradio
    output_image = Image.fromarray(annotated)
    
    return output_image, summary

demo = gr.Interface(
    fn=count_objects,
    inputs=gr.Image(type="pil", label="Upload an image"),
    outputs=[
        gr.Image(type="pil", label="Detected objects"),
        gr.Textbox(label="Object counts")
    ],
    title="Smart Visual Counter",
    description="Upload any image — YOLO detects and counts every object in it.",
)

demo.launch()