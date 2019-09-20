# -*- coding: utf-8 -*-

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl
import pysrt

class Player(QMediaPlayer):

    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.positionChanged.connect(self.position_changed)
        self.subs = None
        self.sub_index = -1
        self.total = None

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
        # print('file_name', file_name)
        srt_name = file_name.replace('.mp3', '.srt')
        self.subs = pysrt.open(srt_name)
        # print(subs[15].text, subs[15].start.seconds)
        # for sub in self.subs:
        #     print(sub.end.seconds, sub.text)

    def play_pause(self):
        if self.state() == QMediaPlayer.PlayingState:
            self.pause()
        else:
            self.play()
        # print(self.state())

    def position_changed(self, ms):
        if not self.total:
            self.total = int(self.duration() / 1000)
        self.ui.update_time(int(ms / 1000), self.total)
        if not self.subs:
            return
        # print('positionChanged', position)
        self.check_sub(ms)

    def update_sub(self):
        sub = self.subs[self.sub_index].text.replace('\n', ' ')
        prev_sub = self.subs[self.sub_index - 1].text.replace('\n', ' ') if self.sub_index > 0 else ''
        self.ui.update_sub(sub, prev_sub)

    def check_sub(self, ms):
        # print('sec', sec)
        new_index = self.sub_index + 1
        sub = self.subs[new_index]
        start = sub.start.minutes * 60000 + sub.start.seconds * 1000 + sub.start.milliseconds
        end = sub.end.minutes * 60000 + sub.end.seconds * 1000 + sub.end.milliseconds
        if start <= ms <= end:
            self.sub_index = new_index
            self.update_sub()
            # print(self.subs[self.sub_index].text.replace('\n', ' '))


    def repeat(self, back=False):
        if back:
            if self.sub_index == 0:
                return
            self.sub_index -= 1
        sub = self.subs[self.sub_index]
        time = sub.start.minutes * 60000 + sub.start.seconds * 1000 + sub.start.milliseconds - 1000
        self.setPosition(time)
        self.update_sub()

    def back(self):
        self.repeat(True)
        # for i, sub in enumerate(self.subs[self.sub_index:]):
        #     if sub.end.minutes * 60 + sub.end.seconds < sec:
        #         print('sub.end.seconds', sub.end.seconds, 'i', i)
        #         self.sub_index = self.sub_index + i + 1
        #         print(self.subs[self.sub_index].text.replace('\n', ' '))
        #         return


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
