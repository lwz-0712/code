import sys
import os
import typing
if not hasattr(typing, 'Self'):
    typing.Self = type('Self', (), {})

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog,QLabel,QLineEdit
from PySide6.QtGui import QPixmap,QImage
from lese import Ui_MainWindow  # 导入生成的UI类
import cv2 as cv
from ultralytics import YOLO
import requests
# 创建全局变量
url = "https://api.siliconflow.cn/v1/chat/completions"
app = None
window = None
ui = None
cap=None
stop=False
model=YOLO("./runs/detect/train/weights/last.pt")
def on_clear_click():
    global cap ,stop
    if stop == False:
        stop=True
    else:
        stop=False
    if cap is not None:
        cap.release()
        cap = None
    
    for child in ui.groupBox.findChildren(QLineEdit):
         child.clear()  # 或者 child.setText("")
    ui.x1.clear()
    ui.y1.clear()
    ui.x2.clear()
    ui.y2.clear()
    ui.idname.clear()
    ui.timelabel.clear()
    ui.conflabel.clear()
    ui.numlabel.clear()
    ui.question.clear()
    ui.response.clear()
    ui.showlabel.clear()
    cv.destroyAllWindows()

def on_camera_click():
    global cap
    cap=cv.VideoCapture(0)
    if cap.isOpened():
        ui.cameraedit.setText("摄像头打开")
    else:
        ui.cameraedit.setText("摄像头没有打开")
        
    while True:
        res,frame=cap.read()
        img_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results=model(img_rgb)
        detections = results[0].boxes.data.cpu().numpy()  # shape: [N, 6] (x1, y1, x2, y2, conf, cls)
        for detection in detections:
            x1, y1, x2, y2, conf, cls_id = detection[:6]
            if conf < 0.5:  # 只显示置信度大于 50% 的检测结果
                continue
          
            # 获取类别名称
            cls_name = model.names[int(cls_id)]  # 从模型中获取类别名称
            # 绘制矩形框  
            showlabel(x1,x2,y1,y2,conf,results,cls_name)
            cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            # 绘制标签（类别 + 置信度）
            label = f"{cls_name} {conf:.2f}"
            cv.putText(frame, label, (int(x1), int(y1) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        # 转换回 RGB 格式并显示在 QLabel 上
        height, width, ch = frame.shape
        bytes_per_line = ch * width
        qimage = QImage(frame.data, width, height, bytes_per_line, QImage.Format_BGR888)
        ui.showlabel.setPixmap(QPixmap.fromImage(qimage))
        code=cv.waitKey(30)
        if code == 27:
            break
    cap.release()

def on_photo_click():
    file_path,type= QFileDialog.getOpenFileName(
    parent=None,
    caption="选择文件",
    dir="",
    filter=" (*.jpg)",
    options=QFileDialog.Options()
)
    ui.photoedit.setText(file_path)
    pix=QPixmap(file_path)
    ui.showlabel.setPixmap(pix)
    ui.showlabel.setScaledContents(True)
    if ui.showlabel.pixmap() is not None and not ui.showlabel.pixmap().isNull():
        update_display(file_path)

def on_video_click():
    global stop
    file_path = QFileDialog.getExistingDirectory(
        None,                   
        "选择文件夹",           
        "",                     
        QFileDialog.ShowDirsOnly 
    )
    ui.videoedit.setText(file_path)
    all_files = [
            os.path.join(file_path, f) 
            for f in os.listdir(file_path) 
            if os.path.isfile(os.path.join(file_path, f))
        ]
    
    i=0
    while True:
        if stop==True:
            break
        if not all_files[i] :
            break
        update_display(all_files[i])
        i+=1
        ui.showlabel.setScaledContents(True)
        cv.waitKey(2000)
        
def showlabel( x1, x2 ,y1,y2,conf,results,id_name):
    ui.conflabel.setText(str(conf))
    ui.x1.setText(str(x1))
    ui.x2.setText(str(x2))
    ui.y1.setText(str(y1))
    ui.y2.setText(str(y2))
    ui.idname.setText(str(id_name))
    num = len(results[0].boxes) 
    speed_data = results[0].speed
# 尝试获取时间（单位：毫秒）
    if 'total' in speed_data:
        time = speed_data['total'] / 1000  # 转换为秒
    else:
        # 计算总和作为替代方案
        time = (speed_data.get('preprocess', 0) + 
        speed_data.get('inference', 0) + 
        speed_data.get('postprocess', 0)) / 1000
    ui.timelabel.setText(str(time))
    ui.numlabel.setText(str(num))

def on_save_click():
    filepath, _ = QFileDialog.getSaveFileName(
        None,                  
        "选择保存位置",        
        "",                     
        "(*)"   
    )       
    save_path =filepath
    if save_path:
        ui.showlabel.pixmap().save(save_path)
    

def on_exit_click():
    window.close()

def on_ai_click():
    global url
    payload = {
        "model": "deepseek-ai/DeepSeek-V3",
        "max_tokens": 512,
        "enable_thinking": True,
        "thinking_budget": 4096,
        "min_p": 0.05,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "stream": False,
        "stop": [],
        "messages": [
            {
                "role": "user",
                "content": ui.question.text()
            }
        ]
    }
    headers = {
        "Authorization": "Bearer sk-oywbygreeqeosreahqsmtrisyirupafcnaqglixcjiccikeg",
        "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers) 
    if response.status_code == 200:
        try:
            response_data = response.json()
            answer = response_data.get("choices", [{}])[0].get("message", {}).get("content", "未获取到有效回复")
            ui.response.setText(answer)  # 传入字符串
        except Exception as e:
            ui.response.setText(f"解析响应失败: {str(e)}")
    else:
        ui.response.setText(f"请求失败 (状态码 {response.status_code}): {response.text}")


def update_display(path):
    global model
    img=cv.imread(path)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results=model(img_rgb)
    detections = results[0].boxes.data.cpu().numpy() 
    for detection in detections:
        x1, y1, x2, y2, conf, cls_id = detection[:6]
        if conf < 0.5:  # 只显示置信度大于 50% 的检测结果
            continue
       
        # 获取类别名称
        cls_name = model.names[int(cls_id)]  # 从模型中获取类别名称
        showlabel(x1,x2,y1,y2,conf,results,cls_name)
        # 绘制矩形框
        cv.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

        # 绘制标签（类别 + 置信度）
        label = f"{cls_name} {conf:.2f}"
        cv.putText(img, label, (int(x1), int(y1) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    # 转换回 RGB 格式并显示在 QLabel 上
    height, width, ch = img.shape
    bytes_per_line = ch * width
    qimage = QImage(img.data, width, height, bytes_per_line, QImage.Format_BGR888)
    ui.showlabel.setPixmap(QPixmap.fromImage(qimage))
    

def setup_window():
    global app, window, ui
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    # 创建UI对象
    ui = Ui_MainWindow()
    ui.setupUi(window)
    
    # 连接按钮信号和槽函数
    ui.clear.clicked.connect(on_clear_click)
    ui.camera.clicked.connect(on_camera_click)
    ui.photo.clicked.connect(on_photo_click)
    ui.video.clicked.connect(on_video_click)
    ui.exit.clicked.connect(on_exit_click)
    ui.save.clicked.connect(on_save_click)
    ui.ai.clicked.connect(on_ai_click)
    

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    setup_window()