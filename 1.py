
if __name__ == "__main__":
    from ultralytics import YOLO

    model = YOLO("./yolov8n.pt")  # create a new model from scratch
        # Load a model
    model = YOLO("yolov8n.yaml").load("./yolov8n.pt")  # load a pretrained model (recommended for training)

    # Train the model
    results = model.train(data="./datasets/train.yaml", epochs=80, imgsz=640)
