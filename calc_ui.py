# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(362, 301)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(11, 13, 341, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_percent = QtWidgets.QPushButton(parent=Form)
        self.pushButton_percent.setGeometry(QtCore.QRect(11, 57, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_percent.setFont(font)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.pushButton_pow = QtWidgets.QPushButton(parent=Form)
        self.pushButton_pow.setGeometry(QtCore.QRect(100, 57, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_pow.setFont(font)
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.pushButton_C = QtWidgets.QPushButton(parent=Form)
        self.pushButton_C.setGeometry(QtCore.QRect(190, 57, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_C.setFont(font)
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_del = QtWidgets.QPushButton(parent=Form)
        self.pushButton_del.setGeometry(QtCore.QRect(279, 57, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_rev = QtWidgets.QPushButton(parent=Form)
        self.pushButton_rev.setGeometry(QtCore.QRect(11, 97, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_rev.setFont(font)
        self.pushButton_rev.setObjectName("pushButton_rev")
        self.pushButton_sqr = QtWidgets.QPushButton(parent=Form)
        self.pushButton_sqr.setGeometry(QtCore.QRect(100, 97, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_sqr.setFont(font)
        self.pushButton_sqr.setObjectName("pushButton_sqr")
        self.pushButton_sqrt = QtWidgets.QPushButton(parent=Form)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(190, 97, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.pushButton_div = QtWidgets.QPushButton(parent=Form)
        self.pushButton_div.setGeometry(QtCore.QRect(279, 97, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_1 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_1.setGeometry(QtCore.QRect(11, 137, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 137, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 137, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_mul = QtWidgets.QPushButton(parent=Form)
        self.pushButton_mul.setGeometry(QtCore.QRect(279, 137, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(11, 177, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 177, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 177, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_minus = QtWidgets.QPushButton(parent=Form)
        self.pushButton_minus.setGeometry(QtCore.QRect(279, 177, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setGeometry(QtCore.QRect(11, 217, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 217, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 217, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_plus = QtWidgets.QPushButton(parent=Form)
        self.pushButton_plus.setGeometry(QtCore.QRect(279, 217, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_neg = QtWidgets.QPushButton(parent=Form)
        self.pushButton_neg.setGeometry(QtCore.QRect(11, 257, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_neg.setFont(font)
        self.pushButton_neg.setObjectName("pushButton_neg")
        self.pushButton_0 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 257, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_dot = QtWidgets.QPushButton(parent=Form)
        self.pushButton_dot.setGeometry(QtCore.QRect(190, 257, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_eq = QtWidgets.QPushButton(parent=Form)
        self.pushButton_eq.setGeometry(QtCore.QRect(279, 257, 70, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        self.pushButton_eq.setFont(font)
        self.pushButton_eq.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_eq.setObjectName("pushButton_eq")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_pow.setText(_translate("Form", "^"))
        self.pushButton_C.setText(_translate("Form", "C"))
        self.pushButton_del.setText(_translate("Form", "DEL"))
        self.pushButton_rev.setText(_translate("Form", "1/x"))
        self.pushButton_sqr.setText(_translate("Form", "x^2"))
        self.pushButton_sqrt.setText(_translate("Form", "x^1/2"))
        self.pushButton_div.setText(_translate("Form", "/"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_mul.setText(_translate("Form", "*"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_neg.setText(_translate("Form", "+/-"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_dot.setText(_translate("Form", "."))
        self.pushButton_eq.setText(_translate("Form", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
