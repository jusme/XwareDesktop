# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject


class Win32Notifier(QObject):
    def __init__(self, parent):
        super().__init__(parent)
