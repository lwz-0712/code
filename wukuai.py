import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2 
from mediapipe.framework.formats import landmark_pb2
import time
from mediapipe.tasks.python.vision import GestureRecognizer, GestureRecognizerOptions, GestureRecognizerResult
import numpy as np
# Add missing imports for drawing utilities and hand connections
import mediapipe.python.solutions.drawing_utils as mp_drawing
import mediapipe.python.solutions.drawing_styles as mp_drawing_styles
import mediapipe.python.solutions.hands as mp_hands


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 半透明物块类
class TransparentBlock:
    def __init__(self, x=320, y=240, size=80):
        self.x = x
        self.y = y
        self.size = size
        self.base_color = (200, 150, 0)  # 默认颜色（BGR格式）
        self.drag_color = (0, 200, 100)  # 拖动时颜色
        self.alpha = 0.6  # 透明度
        self.dragging = False
    
    def draw(self, frame):
        """在帧上绘制半透明物块"""
        overlay = frame.copy()
        color = self.drag_color if self.dragging else self.base_color
        
        # 绘制半透明矩形
        cv2.rectangle(overlay,
                     (self.x-self.size//2, self.y-self.size//2),
                     (self.x+self.size//2, self.y+self.size//2),
                     color, -1)
        
        # 混合透明度
        cv2.addWeighted(overlay, self.alpha, frame, 1-self.alpha, 0, frame)
        
        # 绘制边框（不透明）
        cv2.rectangle(frame,
                     (self.x-self.size//2, self.y-self.size//2),
                     (self.x+self.size//2, self.y+self.size//2),
                     (255, 255, 255), 2)

# 初始化物块
block = TransparentBlock()

# 手势识别配置
model_path = "gesture_recognizer.task"
BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

latest_result = None

def result_callback(result, output_image, timestamp_ms):
    global latest_result
    latest_result = result

options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=result_callback
)

cap = cv2.VideoCapture(0)

with GestureRecognizer.create_from_options(options) as recognizer:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 获取图像尺寸
        h, w = frame.shape[:2]
        
        # 手势识别处理
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        recognizer.recognize_async(mp_image, int(cv2.getTickCount() * 1000 / cv2.getTickFrequency()))
        
        # 处理手势结果
        if latest_result and latest_result.hand_landmarks:
            landmarks = latest_result.hand_landmarks[0]
            
            # 获取拇指(4)和食指(8)指尖坐标
            thumb = landmarks[4]
            index = landmarks[8]
            
            # 转换为像素坐标
            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)
            index_x, index_y = int(index.x * w), int(index.y * h)
            
            # 计算两指距离
            distance = np.sqrt((thumb_x-index_x)**2 + (thumb_y-index_y)**2)
            
            # 捏合检测与拖动控制
            if distance < 30:  # 捏合阈值
                block.dragging = True
                block.x = (thumb_x + index_x) // 2
                block.y = (thumb_y + index_y) // 2
            else:
                block.dragging = False
            
            # 绘制手部关键点（保持原有手势识别显示）
            hand_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            hand_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=l.x, y=l.y, z=l.z) for l in landmarks
            ])
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks_proto,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            
            # 显示指尖坐标（增强可视化）
            cv2.putText(frame, f"Thumb:({thumb_x},{thumb_y})", 
                       (thumb_x+10, thumb_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            cv2.putText(frame, f"Index:({index_x},{index_y})", 
                       (index_x+10, index_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        
        # 绘制物块（始终显示）
        block.draw(frame)
        
        # 显示状态信息
        status = "DRAGGING" if block.dragging else "READY"
        cv2.putText(frame, f"Block State: {status}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(frame, f"Position: ({block.x}, {block.y})", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1)
        
        cv2.imshow('Gesture Controlled Block', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC退出
            break

cap.release()
cv2.destroyAllWindows()