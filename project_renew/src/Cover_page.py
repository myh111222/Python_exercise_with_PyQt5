from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtWidgets,QtCore
import Main_page

WidgetSize=QtCore.QSize(800, 600)

class SlippedImgWidget(QWidget):

	def __init__(self, bg, fg, *args, **kwargs):
		super(SlippedImgWidget, self).__init__(*args, **kwargs)
		self.setMinimumSize(WidgetSize)
		self.setMaximumSize(WidgetSize)
		self.setMouseTracking(True)
		self.bgPixmap = QPixmap(bg)
		self.pePixmap = QPixmap(fg)
		size = self.bgPixmap.size()
		self.setMinimumSize(size.width() - 40, size.height() - 40)
		self.setMaximumSize(size.width() - 10, size.height() - 10)
		self.stepX = size.width() / 10
		self.stepY = size.height() / 10
		self._offsets = [-4, -4, -4, -4]  


	def mouseMoveEvent(self, event):
		super(SlippedImgWidget, self).mouseMoveEvent(event)
		pos = event.pos()

		offsetX = 5 - int(pos.x() / self.stepX)
		offsetY = 5 - int(pos.y() / self.stepY)
		self._offsets[0] = offsetX
		self._offsets[1] = offsetY
		self._offsets[2] = offsetX
		self._offsets[3] = offsetY

		self.update()

	def paintEvent(self, event):
		super(SlippedImgWidget, self).paintEvent(event)
		painter = QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.drawPixmap(
			-5 + self._offsets[0],
			-5 + self._offsets[1], self.bgPixmap)

		painter.drawPixmap(
			self.width() - self.pePixmap.width() + 5 - self._offsets[2],
			self.height() - self.pePixmap.height() + 5 - self._offsets[3],
			self.pePixmap
		)


if __name__ == '__main__':
	import sys
	from PyQt5.QtWidgets import QApplication
	app = QApplication(sys.argv)
	w = SlippedImgWidget('Pictures/bg.jpg', 'Pictures/fg_1.png')
	w.show()
	sys.exit(app.exec_())