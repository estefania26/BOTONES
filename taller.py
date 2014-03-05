import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)


class usuario(QtGui.QDialog):
	def __init__(self):
		super(usuario, self).__init__()

		cuadro = QtGui.QLabel(self)
		cuadro.setText("nombre")
		cuadro.setGeometry(20,10,70,40)

		line = QtGui.QLineEdit(self)
		line.setText("escribe .-.")
		line.setGeometry(100,15,200,25)

		cuadro2 = QtGui.QLabel(self)
		cuadro2.setText("apellido")
		cuadro2.setGeometry(20,43,47,43)

		line2 = QtGui.QLineEdit(self)
		line2.setText("escribe .-.")
		line2.setGeometry(100,40,200,25)


vent = usuario()
vent.show()

sys.exit(app.exec_())