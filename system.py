from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from gui import Ui_MainWindow
import sys
from callModel import Predict
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class App(Ui_MainWindow):
    def __init__(self):
        super().setupUi(MainWindow)
        self.LineEditname = [
            self.fixed, self.volatile_2, self.citric, self.sugar, self.chlorides, self.freesulfur, self.totalsulfur,
            self.density, self.pH, self.sulphates, self.alcohol
        ]
        self.Label = [
            self.label, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, 
            self.label_7, self.label_8, self.label_9, self.label_10, self.label_11
        ]
        self.value = []
        self.Predict.setEnabled(False)
        
    def predictbt(self):
        self.check.clicked.connect(self.inputvalue)
        self.Predict.clicked.connect(self.predictmodel)
        self.Clear.clicked.connect(self.clearLineEdit)
    
    def inputvalue(self):
        
        # Check missing value
        for i in range(0, len(self.LineEditname)):
            if self.LineEditname[i].text() != '':
                pass
            elif self.LineEditname[i].text() == '':
                self.show_popup(self.Label[i].text())
                
        # Check invalid type value
        for i in self.LineEditname:
            try:
                x = float(str(i.text()))
                self.value.append(x)
            except:
                self.show_errorvalue()
                self.value = []
                break
            
        if len(self.value) == 11:
            self.show_Correct_value()
            self.Predict.setEnabled(True)
    
    def clearLineEdit(self): 
        for i in self.LineEditname:
            i.clear()
        self.value = []
        self.quality.setText('0')
        self.Predict.setEnabled(False)
        
    def predictmodel(self):
        status = model.import_model()
        if status:
            model.value = self.value
            self.quality_resposne = model.predictQuality()
            if self.quality_resposne == False:
                self.value = []
                self.show_import_error()
            else:
                
                self.quality.setText(self.quality_resposne)
                self.Predict.setEnabled(False)
                self.value = []
        else:
            self.value = []
            self.show_import_error()
            
        
    def show_popup(self, rec):
        self.rec = rec
        msg = QMessageBox()
        msg.setWindowTitle("Missing {} value!" .format(self.rec))
        msg.setText("Please fill {} box!" .format(self.rec))
        x = msg.exec_()
        
    def show_errorvalue(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid value!")
        msg.setText("Please enter int, float only!!")
        x = msg.exec_()
        
    def show_Correct_value(self):
        msg = QMessageBox()
        msg.setWindowTitle("OK")
        msg.setText("Correct Value!!!")
        x = msg.exec_()
    
    def show_import_error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Module Error!")
        msg.setText("Some model error!")
        x = msg.exec_()

if __name__ == "__main__":
    AppRun = App()
    model = Predict()
    AppRun.predictbt()
    MainWindow.show()
    sys.exit(app.exec_())