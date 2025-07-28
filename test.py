#!/usr/bin/env python3

import cv2
import depthai as dai

# 创建管道
pipeline = dai.Pipeline()

# 定义源（RGB 相机）和输出
camRgb = pipeline.create(dai.node.ColorCamera)
xoutRgb = pipeline.create(dai.node.XLinkOut)

xoutRgb.setStreamName("rgb")

# 属性设置
camRgb.setPreviewSize(300, 300)  # 设置预览分辨率，您可以改为 (640, 400)，但预览适合小尺寸
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# 链接节点
camRgb.preview.link(xoutRgb.input)

# 连接设备并启动管道
with dai.Device(pipeline) as device:
    print('已连接相机:', device.getConnectedCameraFeatures())
    print('USB 速度:', device.getUsbSpeed().name)
    if device.getBootloaderVersion() is not None:
        print('引导加载程序版本:', device.getBootloaderVersion())
    print('设备名称:', device.getDeviceName(), ' 产品名称:', device.getProductName())

    # 获取输出队列
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        inRgb = qRgb.get()  # 阻塞调用，等待新帧到达

        # 显示 OpenCV 格式的帧
        cv2.imshow("rgb", inRgb.getCvFrame())

        if cv2.waitKey(1) == ord('q'):
            break