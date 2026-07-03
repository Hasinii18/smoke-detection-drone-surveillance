from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO('C:/Users/polys/Downloads/DFire_Final/best.pt')

    results = model.val(
        data='C:/Users/polys/Downloads/DFire_Final/data.yaml',
        imgsz=640,
        batch=16,
        device=0,
        workers=0,   # 👈 IMPORTANT FIX
        save=True
    )

    print("mAP50:", results.box.map50)
    print("mAP50-95:", results.box.map)