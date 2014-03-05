import sys
from PySide import QtGui
from PySide import QtCore


class VentanaBoton(QtGui.QDialog):
	def __init__(self):
		
		super(VentanaBoton, self).__init__()

		selfGeometry(300,400,300,300)

		btn = QtGui.QPushButton(self)
		btn.setText("Boton 1")
		btn.setGeometry(20,20,100,300)
		btn.clicked.connect(self.mensajear)

		btn2 = QtGui.QPushButton(self)
		btn2.setText("Boton 2")
		btn2.setGeometry(150,20,300,300)
		btn2.clicked.connect(self.mensajear2)

		btn3 = QtGui.QPushButton(self)
		btn3.setText("Boton 3")
		btn3.setGeometry(40,20,300,300)
		btn3.clicked.connect(self.mensajear3)

		btn4 = QtGui.QPushButton(self)
		btn4.setText("Boton 4")
		btn4.setGeometry(60,20,300,300)
		btn4.clicked.connect(self.mensajear4)

		btn5 = QtGui.QPushButton(self)
		btn5.setText("Boton 5")
		btn5.setGeometry(80,20,300,300)
		btn5.clicked.connect(self.mensajear5)


	
	def mensajear(self):
		print("OJO PUES")
		QtGui.QMessageBox.warning(self, "OJO PUES")
	
	def mensajear2(self):
		print(".-.")
		QtGui.QMessageBox.information(self, "ACABAS DE PRESIONAR :D")
    
	def mensajear3(self):
		print("HOLA")
		QtGui.QMessageBox.critical(self, "BUAJAJAJ")
    
	def mensajear4(self):
		print(":d -.-")
		QtGui.QMessageBox.question(self, "¿¡?")
    
	def mensajear5(self):
		print(":}")
		QtGui.QMessageBox.information(self, "ESTAS PENSANDO ")

vent = VentanaBoton()
vent.show()

sys.exit(app.exec_())
