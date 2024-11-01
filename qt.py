#  jack_midi_recorder/qt.py
#
#  Copyright 2024 liyang <liyang@veronica>

from jack_midi_recorder import MIDIRecorder
from PyQt5.QtCore import QObject, pyqtSignal


class QtMIDIRecorder(MIDIRecorder, QObject):

	sig_PlayFinished = pyqtSignal()

	def play(self):
		super().play()
		self.sig_PlayFinished.emit()

	def __init__(self, client_name):
		QObject.__init__(self)
		MIDIRecorder.__init__(self, client_name)


#  end jack_midi_recorder/qt.py
