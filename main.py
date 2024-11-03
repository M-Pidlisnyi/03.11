from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


#створити екземпляр App (в конструктор передати пустий список)
app = QApplication([])
#створити екземпляр вікна
win = QWidget()

#створити віджет - текст
text = QLabel("Hello World")

# розмістити віджет на вікні
line = QVBoxLayout()
line.addWidget(text)
win.setLayout(line)

# показати вікно
win.show()
# запустити програму
app.exec()
