from ultralytics import YOLO

# 加载模型
model = YOLO("yolo11n.pt")

# 将模型导出为 ONNX 格式
path = model.export(format="onnx")  # 返回导出模型的路径