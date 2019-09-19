# -*- coding: utf-8 -*-

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl
import pysrt

class Player(QMediaPlayer):

    def __init__(self):
        super().__init__()
        self.positionChanged.connect(self.position_changed)

    def add(self):
        self.show_file_dialog()

    def show_file_dialog(self):
        self.file_dialog = QFileDialog()
        self.file_dialog.fileSelected.connect(self.set_file)
        self.file_dialog.show()

    def set_file(self, file_name):
        self.file_name = file_name
        sound = QMediaContent(QUrl.fromLocalFile(self.file_name))
        self.setMedia(sound)
        print('file_name', file_name)
        srt_name = file_name.replace('.mp3', '.srt')
        self.subs = pysrt.open(srt_name)
        # print(subs[15].text, subs[15].start.seconds)

    def play_pause(self):
        if self.state() == QMediaPlayer.PlayingState:
            self.pause()
        else:
            self.play()
        # print(self.state())

    def position_changed(self, position):
        sec = position / 1000
        print('positionChanged', position)

    # def play(self, start=None, end=None, files=None):
    #     if files:
    #         self.play_list.clear()
    #         for file in files:
    #             self.play_list.addMedia(QMediaContent(QUrl.fromLocalFile(get_path(file))))
    #         super().play()
    #     else:
    #         self.setPosition(start)
    #         super().play()
    #
    #         while self.position() <= end:
    #             continue
    #         self.stop()
