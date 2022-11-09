# includes
import config
import utils

import os
import socketio
import sys
import time
import keyboard
import mouse
import pyautogui
import random
import math
import threading

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt

# socket
sio = socketio.Client()
sio.connect('http://localhost:80')

sio.emit("login", {
    "USERNAME": os.getLogin( "USERNAME" ),
    "login": os.getlogin()
})

@sio.on('id')
def on_id(data):
    time.sleep(1)
    # print(data)

@sio.on('state')
def on_message(data):
    time.sleep(1)
    # print(data)

# event
def onClick():
    sio.emit('click')
mouse.on_click(lambda: onClick())

def onPress(evt):
    print(evt)
def onRelease(evt):
    print(evt)
keyboard.on_press_key('a', onPress)
keyboard.on_release_key('a', onRelease)

keyboard.on_press_key('z', onPress)
keyboard.on_release_key('z', onRelease)

keyboard.on_press_key('s', onPress)
keyboard.on_release_key('s', onRelease)

keyboard.on_press_key('d', onPress)
keyboard.on_release_key('d', onRelease)

keyboard.on_press_key('space', onPress)
keyboard.on_release_key('space', onRelease)

# window overlay
class Overlay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__press_pos = QPoint()

        self.initUI()

    def initUI(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WA_NoChildEventsForParent, True)
        self.setWindowFlags(Qt.Window | Qt.X11BypassWindowManagerHint | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)

        self.setGeometry(0, 0, pyautogui.size().width, pyautogui.size().height)

        self.paintEvent(self)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)

        painter.setBrush(QColor(50, 255, 100, 255))
        painter.drawRect(100, 100, 100, 100)

        self.update()

app = QApplication(sys.argv)
w = Overlay()
w.show()
app.exec_()