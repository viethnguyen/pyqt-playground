import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
	def __init__(self,parent=None):
		super(Form, self).__init__(parent)

		date = self.getdata()
		rates = sorted(self.rate.keys())

		dateLabel = QLabel(date)
		self.fromComboBox = QComboBox()
		self.fromComboBox.addItem(rates)
		self.fromSpinBox = QDoubleSpinBox()
		self.fromSpinBox.setRange(0.01, 100000000.00)
		self.fromSpinBox.setValue(1.00)
		self.toComboBox = QComboBox()
		self.toComboBox.addItems(rates)
		self.toLabel = QLabel("1.00")

		grid = QGridLayout()
		grid.addWidget(dateLabel, 0, 0)
		grid.addWidget(self.fromComboBox, 1,0)
		grid.addWidget(self.fromSpinBox, 1,1)
		grid.addWidget(self.toComboBox, 2,0)
		grid.addWidget(self.toLabel, 2,1)
		self.setLayout(grid)