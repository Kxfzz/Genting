import time

import pyautogui
from pynput.mouse import Button, Controller

mouse = Controller()

# 图片列表
images = ["image1.png", "image2.png", "image3.png", "image4.png", "image5.1.png", "image5.2.png", "image5.3.png",
          "image5.4.png", "image5.5.png", "image6.png", "image7.png", "image8.png", "image9.png", "image10.png"]

while True:
    for image in images:
        try:
            # 在屏幕上查找图片
            location = pyautogui.locateOnScreen(image, confidence=0.9)
            if location is not None:
                center = pyautogui.center(location)

                # 找到图片后移动鼠标并点击
                mouse.position = center
                mouse.click(Button.left, 1)
                time.sleep(0.5)
        except:
            continue
