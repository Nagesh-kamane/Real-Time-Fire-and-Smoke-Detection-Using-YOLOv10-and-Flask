import traceback
import sys

try:
    from ultralytics import YOLO
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_tb(exc_traceback)
    print(exc_value)
