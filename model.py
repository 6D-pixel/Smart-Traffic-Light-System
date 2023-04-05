import cv2
from collections import Counter
from ultralytics import YOLO

def get_total_time(image_path):
    # Load YOLOv8 model
    model = YOLO("400E.pt")

    # Read image
    img = cv2.imread(image_path)

    # Perform object detection
    results = model(img, show=True)

    boxes = results[0].boxes

    # Create counter object to count occurrences of each class
    class_counts = Counter(int(box.cls) for box in boxes)

    # Get counts of each object class
    auto_count = class_counts.get(0, 0)
    bike_count = class_counts.get(1, 0)
    bus_count = class_counts.get(2, 0)
    car_count = class_counts.get(3, 0)
    truck_count = class_counts.get(4, 0)

    # Calculate time based on object counts
    distance = 40;
    speed = 8.4;
    time = distance / speed;
    num_lane = 2 
    total_time = ((auto_count*time) + (bike_count*time) + (bus_count *time) + (car_count*time) + (truck_count*time))/(2*num_lane) 
    print("Green_time:",total_time)
    # Return total time
    return total_time
