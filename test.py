from ultralytics import YOLO

model = YOLO(r"C:\Users\hasin\Downloads\DFire_Final (2)\DFire_Final\best.pt")

results = model.predict(
    source = r"C:\Users\hasin\Videos\Screen Recordings\Screen Recording 2026-05-07 114204.mp4",
    conf=0.25,
    save=True,
    # show=True
)
for r in results:
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])

        class_name = model.names[cls_id]

        if class_name in ["smoke"]:
            print(f"🔥 ALERT: {class_name.upper()} detected with confidence {conf:.2f}")