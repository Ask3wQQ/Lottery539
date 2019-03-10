from mainWindow import Ui_MainWindow
import showCombinations

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QTableWidgetItem, QMessageBox
from itertools import combinations
from random import sample

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.Initial_UI()

    def Initial_UI(self):
        self.setupUi(self)
        self.show()
        self.pushButton_Gen.clicked.connect(self.Generate)
        self.pushButton_Random.clicked.connect(self.RandomNumber)
        self.ButtonGroup = [self.pushButton_01, self.pushButton_02, self.pushButton_03, self.pushButton_04, self.pushButton_05,
                           self.pushButton_06, self.pushButton_07, self.pushButton_08, self.pushButton_09, self.pushButton_10,
                           self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15,
                           self.pushButton_16, self.pushButton_17, self.pushButton_18, self.pushButton_19, self.pushButton_20,
                           self.pushButton_21, self.pushButton_22, self.pushButton_23, self.pushButton_24, self.pushButton_25,
                           self.pushButton_26, self.pushButton_27, self.pushButton_28, self.pushButton_29, self.pushButton_30,
                           self.pushButton_31, self.pushButton_32, self.pushButton_33, self.pushButton_34, self.pushButton_35,
                           self.pushButton_36, self.pushButton_37, self.pushButton_38, self.pushButton_39]

    def DefualtButton(self):
        for button in self.ButtonGroup:
            if button.isChecked():
                button.toggle()
        return

    def RandomNumber(self):
        x = int(self.spinBox.text())
        self.DefualtButton()
        numbers = list(range(1, 40))
        choose = sample(numbers, x)
        choose.sort()
        for i in choose:
            self.ButtonGroup[i-1].toggle()
        return

    def CheckAllButtons(self):
        buttonChecked = []
        for i in range(len(self.ButtonGroup)):
            if self.ButtonGroup[i].isChecked():
                buttonChecked.append(self.ButtonGroup[i].text())
        print(buttonChecked)
        if len(buttonChecked) < 5:
            print("less than 5")
            return False
        return buttonChecked

    def InfoDialog(self):
        infoBox = QMessageBox()
        infoBox.setIcon(QMessageBox.Information)
        infoBox.setText("The numbers you choose must be more than 5 numbers.")
        infoBox.setWindowTitle("Information")
        infoBox.setStandardButtons(QMessageBox.Ok)
        infoBox.setEscapeButton(QMessageBox.Close)
        infoBox.exec_()

    def Generate(self):
        buttons = self.CheckAllButtons()
        if not buttons:
            self.InfoDialog()
            return -1
        self.showTable = ShowCombinations()
        self.showTable.pushButton.clicked.connect(self.showTable.close)
        try:
            x = combinations(buttons, 5)
            for row_index, row_data in enumerate(x):
                self.showTable.tableWidget.insertRow(row_index)
                for col_index, col_data in enumerate(row_data):
                    self.showTable.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))
        except Exception as error:
            print(error)
        self.showTable.label.setText("How many: " + str(row_index + 1))
        self.showTable.label_2.setText("How much: " + str((row_index + 1)*50))
        self.showTable.exec_()
        return

class ShowCombinations(QDialog, showCombinations.Ui_Dialog):
    def __init__(self, parent=None):
        super(ShowCombinations, self).__init__(parent)
        self.setupUi(self)

app = QApplication([])
win = MainApp()
app.exec_()