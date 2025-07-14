import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QLabel,QMessageBox
from PySide6.QtGui import QPixmap,QImage,Qt
from PySide6.QtCore import QTimer
from face import Ui_MainWindow
from daka import Ui_MainWindow  as dakaui # 导入生成的UI类
import cv2 as cv
import os
import numpy as np
from PIL import Image
import sqlite3
from datetime import datetime
import dlib
from scipy.spatial import distance as dist
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")




# 创建全局变量
fass=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
app = None
window = None
ui = None
timer=None
cap=None
path="./data"
db=sqlite3.connect("employ.db")
cur=db.cursor()

#显示时间
def update_time():
    global timer, ui
    
    # 确保定时器只被创建一次
    if timer is None:
        timer = QTimer()
        
        # 定义时间更新函数
        def update_time():
            current_time = datetime.now().strftime('%H:%M:%S')
            ui.time.setText(current_time)  # 直接更新UI标签
        
        # 连接定时器信号与更新函数，每秒触发一次
        timer.timeout.connect(update_time)
        timer.start(1000)  # 1000毫秒 = 1秒
        
        # 初始化显示当前时间
        update_time()
    else:
        # 如果定时器已存在，确保它处于运行状态
        if not timer.isActive():
            timer.start(1000)
  
def on_startbutton_click():
    global cap, timer
    print("start按钮被点击了!")
    
    # 释放已有的摄像头资源
    if cap is not None:
        cap.release()
    
    # 打开摄像头
    cap = cv.VideoCapture(0)
    
    if not cap.isOpened():
        print("无法打开摄像头")
        return
    
    # 创建定时器，定时更新画面
    timer = QTimer()
    timer.timeout.connect(update_frame)
    timer.start(30)  # 每30毫秒更新一次

def update_frame():
    global cap, ui
    
    if cap is None:
        return
    
    ret, frame = cap.read()
    if not ret:
        print("无法获取帧")
        return
    
    # 转换为RGB格式
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face=fass.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=2)
    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(200,0,0),2)
    
    rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    
    # 创建QImage并显示在QLabel上
    q_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
    pixmap = QPixmap.fromImage(q_img)
    
    if not pixmap.isNull():
        # 缩放pixmap以适应QLabel大小，并保持宽高比
        scaled_pixmap = pixmap.scaled(
            ui.showlable.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        ui.showlable.setPixmap(scaled_pixmap)
        # 不需要调整QLabel大小，让布局管理器处理
    else:
        print("无法创建有效的QPixmap")

def on_catchbutton_click():
     global cap ,db ,cur
     
     cur.execute('''
           CREATE TABLE IF NOT EXISTS employees (
                name TEXT NOT NULL,
                id int NOT NULL  unique)
    ''')
     db.commit()

     if cap is None or not cap.isOpened():
        QMessageBox.warning(window, "警告", "请先打开摄像头并填写用户信息！")
        return
     res,frame=cap.read()
     if not res:
         print("无法获取zhen")
     gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
     face=fass.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=2)
     for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y),(x+w,y+h),(200,0,0),2)
        roi=gray[y:y+h,x:x+w]
    #数据录入
     name = ui.name1.text().strip()
     emp_id = ui.id1.text().strip()
     print(emp_id)
     print(roi)
     cv.imwrite("./data/%d.jpg"%int(emp_id),roi)
     if not name or not emp_id:
            print("姓名和 ID 不能为空！")
            return
     cur.execute("insert into employees (id,name) values(?,?)",(emp_id,name))
     db.commit()
     print("数据录入cg")   
     ui.name1.clear()
     ui.id1.clear()

# def eye_aspect_ratio(eye):
#     """计算眼睛纵横比（确保输入是坐标值）"""
#     # 提取每个点的x、y坐标，转为[(x1,y1), (x2,y2), ...]格式
#     coords = [(p.x, p.y) for p in eye]
#     # 计算三组关键点的欧氏距离
#     A = dist.euclidean(coords[1], coords[5])  # 垂直距离1
#     B = dist.euclidean(coords[2], coords[4])  # 垂直距离2
#     C = dist.euclidean(coords[0], coords[3])  # 水平距离
#     return (A + B) / (2.0 * C)

# def mouth_aspect_ratio(mouth):
#     """计算嘴巴纵横比（同上处理）"""
#     coords = [(p.x, p.y) for p in mouth]
#     A = dist.euclidean(coords[2], coords[10])
#     B = dist.euclidean(coords[4], coords[8])
#     C = dist.euclidean(coords[0], coords[6])
#     return (A + B) / (2.0 * C)

# def is_live(shape, ear_threshold=0.2, mar_threshold=0.6):
#     """判断活体（修正特征点提取方式）"""
#     # 提取眼睛和嘴巴的特征点索引（dlib标准68点分区）
#     left_eye = [shape.part(i) for i in range(36, 42)]  # 左眼36-41点
#     right_eye = [shape.part(i) for i in range(42, 48)]  # 右眼42-47点
#     mouth = [shape.part(i) for i in range(60, 68)]  # 嘴巴60-67点
    
#     # 直接调用修正后的纵横比计算函数
#     ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0
#     mar = mouth_aspect_ratio(mouth)
    
#     return ear < ear_threshold or mar > mar_threshold
         
   
def on_go_click():
    global cap, db,cur
    # 初始化计数器和活体检测标志
    # blink_counter = 0
    # live_detected = False
    recongizer=cv.face.LBPHFaceRecognizer.create()
    cap=cv.VideoCapture(0)
    #读取训练模型
    recongizer.read("./train/trains.yml")
    i=0
    chongfuid=set()
    while True:
        res,frame=cap.read()
        if not res:
            break
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        face=fass.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=2)

        # faces = detector(gray)
        # for face in faces:
        #     # 获取特征点
        #     shape = predictor(gray, face)
        #     for n in range(0, 68):
        #         x = shape.part(n).x
        #         y = shape.part(n).y
        #         cv.circle(frame, (x, y), 2, (0, 255, 0), -1)
        #     if is_live(shape):
        #         blink_counter += 1
        #         if blink_counter >= 3:  # 检测到3次眨眼或张嘴动作
        #             live_detected = True
        #             cv.putText(frame, "LIVE", (10, 30), 
        #                       cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)


        for(x,y,w,h) in face:
            cv.rectangle(frame,(x,y),(x+w,y+h),(200,0,0),2)
            roi=gray[y:y+h,x:x+w]

            if roi.size > 0:#识别人脸,返回id，置信度  # 确保ROI不为空
                id, conf = recongizer.predict(roi)
                label = f"ID:{id} conf:{conf:.2f}"

            if conf < 60 and id not in chongfuid :
                cur.execute("select * from employees where id=?",(id,))
                result=cur.fetchone()
                if result:
                        # 格式化数据为字符串
                        user = f"ID: {result[1]} | 姓名: {result[0]} |时间:{ui.time.text()}"
                        # 逐行添加到QListWidget
                        ui.listWidget.addItem(user)
                        chongfuid.add(id)
                      
                else:
                    ui.listWidget.addItem(f"ID: {id} | 未在数据库中找到")
                        
            cv.putText(frame,label,(x,y-10),2,1.2,(200,0,0),2)
        rgb_image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
    
       # 创建QImage并显示在QLabel上
        q_img = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
    
        if not pixmap.isNull():
            # 缩放pixmap以适应QLabel大小，并保持宽高比
            scaled_pixmap = pixmap.scaled(
                ui.dakalabel.size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            ui.dakalabel.setPixmap(scaled_pixmap)
            # 不需要调整QLabel大小，让布局管理器处理
        else:
            print("无法创建有效的QPixmap")
        
        code=cv.waitKey(10) & 0xFF
        if code==27:
            break

def on_trainbutton_click():
   global path
   images=[]
   lables=[]
   imagepaths=[os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
   print(imagepaths)
   for imagepath in imagepaths:
            #打开图片并转换为灰色图片
            pil_image = Image.open(imagepath).convert("L")
            #这里设为灰度
            np_img=np.array(pil_image,dtype="uint8")
            # print(np_img.shape)
            #将人脸区域添加到images
            face= fass.detectMultiScale(np_img,scaleFactor=1.2,minNeighbors=2)
            #切片路径存入lable
            id=int(os.path.split(imagepath)[1].split(".")[0])
            for x,y,w,h in face:
             images.append(np_img[y:y+h,x:x+w])
             lables.append(id)

   print(lables,images)
   rec = cv.face.LBPHFaceRecognizer.create()

    # 传入数据训练模型
   
    # exit()
   rec.train(images,np.array(lables))

    #保存模型
   rec.write("./train/trains.yml")

def on_close_click():
    global cap
    if cap is None or not cap:
        print("摄像头未开启")
        return
    cap.release()
    ui.showlable.clear()
def on_stop_click():
    global cap
    if cap.isOpened():
        cap.release()
        ui.dakalabel.clear()
        ui.listWidget.clear()
        return


def setup_window():
    global app, window, ui
    
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    # 创建UI对象
    ui = Ui_MainWindow()
    ui.setupUi(window)
    
    # 连接按钮信号和槽函数
    ui.startbutton.clicked.connect(on_startbutton_click)
    ui.catchbutton.clicked.connect(on_catchbutton_click)
    ui.trainbutton.clicked.connect(on_trainbutton_click)
    ui.go.clicked.connect(on_go_click)
    ui.close.clicked.connect(on_close_click)
    ui.stop.clicked.connect(on_stop_click)
    update_time()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    setup_window()