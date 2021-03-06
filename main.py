# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys,math

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject,Property,Signal,Slot


class Calculator(QObject):
    display_changed = Signal()
    def __init__(self):
        super(Calculator, self).__init__()
        self._display = ""

    @staticmethod
    def coerce(x):
        a = float(x)
        try:
            b = int(x)
        except:
            return a

        return b

    @Slot(str)
    def set_display(self,value):
        if value == "C":
            self._clear_display()
            return
        if value == "=":
            self._calc()
            return
        if value == "+/-":
            self._change_sign()
            return




        self._display += value
        self.display_changed.emit()


    def _get_display(self):

        return self._display

    def _clear_display(self):
        self._display = ""
        self.display_changed.emit()

    def _percentage(self,current_text):
        current_display  = current_text
        values = current_display.split("%")
        if len(values) != 2:
            raise ValueError("This implementation only supports a single % operation")

        num1 = values[0]
        num2 = values[1]
        num1 =self.coerce(num1)
        num2 = self.coerce(num2)


        print(num1,num2)

        return num1 * (num2/100)



    def _calc(self):
        current_text = self._display
        if "%" in self._display:
            self._percentage(current_text)
            self.result = self._percentage(current_text)
            self._display = str(int(self.result))
            self.display_changed.emit()


        self._display = str(eval(self._display))
        self.display_changed.emit()


    display = Property(str,_get_display,notify=display_changed)

    def _change_sign(self):
        current_display = self._display
        if current_display:
            if current_display[0] == "-":
                self._display = current_display[1:]  # kihagyuk az els??(-) elemet
            else:
                self._display =  f"-{current_display}"

        self.display_changed.emit()




class CalculatorWindow:
    def __init__(self):
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

        self.context = self.engine.rootContext()

        self.calculator = Calculator()

        self.context.setContextProperty("Calculator", self.calculator)



        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)
        sys.exit(self.app.exec())


if __name__ == "__main__":
    CalculatorWindow()