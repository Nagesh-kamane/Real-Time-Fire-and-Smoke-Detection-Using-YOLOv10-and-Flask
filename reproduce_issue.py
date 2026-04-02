from ultralytics import YOLO
import os

try:
    print("Loading model...")
    model = YOLO(r'runs/detect/train7/weights/best.pt')
    
    file_path = os.path.abspath(r'uploads/fire1.jpg')
    print(f"Testing on file: {file_path}")
    
    if not os.path.exists(file_path):
        print("File does not exist!")
    else:
        print("Running prediction...")
        results = model(file_path)
        print("Prediction successful!")
        print(results)

except Exception as e:
    print("Caught exception:")
    print(e)
    import traceback
    traceback.print_exc()
