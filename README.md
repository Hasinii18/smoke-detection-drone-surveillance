\# Deep Learning Smoke Detection for Drone-Based Surveillance



A real-time \*\*YOLOv8-based smoke detection system\*\* designed for early wildfire detection using aerial drone imagery. The model detects \*\*Fire, Smoke, and Cloud\*\* to minimize false positives and support rapid emergency response.



\---



\## Project Overview



Wildfires can spread rapidly before they are detected. This project leverages the \*\*YOLOv8 object detection framework\*\* to identify smoke and fire from aerial images captured by drones, enabling faster detection and response.



The model was trained on a dataset of \*\*22,854 annotated aerial images\*\* and achieved \*\*76.87% precision\*\* while distinguishing between \*\*Fire, Smoke, and Cloud\*\*.



\---



\## Features



\- Real-time smoke and fire detection

\- Three-class classification:

&#x20; - 🔥 Fire

&#x20; - 🌫️ Smoke

&#x20; - ☁️ Cloud

\- Built using YOLOv8

\- Supports image and video inference

\- Designed for aerial surveillance scenarios



\---



\## Model Performance



| Metric | Value |

|---------|-------|

| Precision | \*\*76.87%\*\* |

| Recall | \*\*70.21%\*\* |

| Framework | YOLOv8 |

| Total Images | 22,854 |

| Classes | Fire, Smoke, Cloud |



\---



\## Dataset



\- \*\*Total Images:\*\* 22,854 annotated images

\- \*\*Classes:\*\*

&#x20; - Fire: 1,164 images

&#x20; - Smoke: 5,867 images

&#x20; - Cloud + Smoke (Negative): 1,327 images

&#x20; - Background: 9,838 images

&#x20; - Fire + Smoke: 4,658 images

\- \*\*Source:\*\* D-Fire Dataset (Kaggle)

\- \*\*Annotations:\*\* Bounding boxes for object detection



\---



\## Model Architecture



\- \*\*Framework:\*\* YOLOv8 (Ultralytics)

\- \*\*Input Size:\*\* 640 × 640 pixels

\- \*\*Output:\*\* Bounding boxes with class predictions

\- \*\*Classes:\*\* Fire, Smoke, Cloud

\- \*\*Training Strategy:\*\* Transfer learning using pretrained YOLOv8 weights



\---



\## Technologies Used



\- Python

\- YOLOv8 (Ultralytics)

\- OpenCV

\- NumPy

\- Pandas

\- ONNX (Deployment)

\- Raspberry Pi 4 (Target Edge Device)



\---





\## Installation



```bash

git clone https://github.com/Hasinii18/smoke-detection-drone-surveillance.git



cd smoke-detection-drone-surveillance



pip install -r requirements.txt



\---



\## Usage



Run inference using:



```bash

python test.py

```



or



```bash

python test2.py

```



\---



\## Key Learnings



\- Deep learning model training and optimization

\- Real-time object detection

\- Handling class imbalance in aerial imagery

\- Dataset curation and annotation at scale (22K+ images)

\- Edge deployment using Raspberry Pi

\---



\## Future Work



\- Deploy on actual drone hardware (DJI)

\- Real-time RTSP video stream processing

\- Integration with emergency alert systems

\- Improve precision using larger datasets



\---

\## License



This project is intended for educational and research purposes.

\---



\## Author



**\*\*Lakshmi Sai Hasini B\*\***

B.Tech, Civil Engineering (2024–2028)

IIT Palakkad

📧 saihasini0618@gmail.com

📧 hasinibasireddy007@gmail.com



GitHub: https://github.com/Hasinii18

