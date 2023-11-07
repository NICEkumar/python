from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use the model
# model.train(data="config.yaml", epochs=100)  # train the model
results = model('/Users/NICE/Downloads/soccer-playing-time.jpg')  # predict on an image
for r in results:
    print(r.boxes)
model.export(format='')