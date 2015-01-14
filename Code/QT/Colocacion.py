# -*- coding: latin-1 -*-

from PyQt4 import QtCore, QtGui

class V(QtGui.QVBoxLayout):
    """
    Acomodaci�n en vertical.
    """

    # def __init__(self):
        # QtGui.QVBoxLayout.__init__(self)

    def control(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        return self

    def controlc(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        self.setAlignment(QtCore.Qt.AlignCenter)
        return self

    def controld(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        self.setAlignment(control, QtCore.Qt.AlignRight)
        return self

    def controli(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        self.setAlignment(control, QtCore.Qt.AlignLeft)
        return self

    def otro(self, layout):
        """
        A�ade otro layout.
        """
        self.addLayout(layout)
        return self

    def espacio(self, espacio):
        """
        A�ade espacio fijo.
        """
        self.addSpacing(espacio)
        return self

    def margen(self, n):
        """
        Margen exterior.
        """
        self.setContentsMargins(n, n, n, n)
        return self

    def relleno(self, factor=1):
        """
        A�ade espacio de relleno, que ocupa lo que puede seg�n un factor = stretch.
        """
        self.addStretch(factor)
        return self

class H(QtGui.QHBoxLayout):
    """
    Acomodaci�n en horizontal.
    """

    # def __init__(self):
        # QtGui.QHBoxLayout.__init__(self)

    def control(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        return self

    def controld(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        self.setAlignment(control, QtCore.Qt.AlignRight)
        return self

    def controli(self, control):
        """
        A�ade un control.
        """
        self.addWidget(control)
        self.setAlignment(control, QtCore.Qt.AlignLeft)
        return self

    def otro(self, layout):
        """
        A�ade otro layout.
        """
        self.addLayout(layout)
        return self

    def otroi(self, layout):
        """
        A�ade otro layout.
        """
        self.addLayout(layout)
        self.setAlignment(layout, QtCore.Qt.AlignLeft)
        return self

    def otroc(self, layout):
        """
        A�ade otro layout.
        """
        self.addLayout(layout)
        self.setAlignment(layout, QtCore.Qt.AlignCenter)
        return self

    def espacio(self, espacio):
        """
        A�ade espacio fijo.
        """
        self.addSpacing(espacio)
        return self

    def ponSeparacion(self, tam):
        """
        Separaci�n entre controles
        """
        self.setSpacing(tam)
        return self

    def margen(self, n):
        """
        Margen exterior.
        """
        self.setContentsMargins(n, n, n, n)
        return self

    def relleno(self, factor=1):
        """
        A�ade espacio de relleno, que ocupa lo que puede seg�n un factor = stretch.
        """
        self.addStretch(factor)
        return self

class G(QtGui.QGridLayout):
    """
    Acomodaci�n en tabla.
    """

    # def __init__(self):
        # QtGui.QGridLayout.__init__(self)

    dicAlineacion = {None: QtCore.Qt.AlignLeft, "d": QtCore.Qt.AlignRight, "c": QtCore.Qt.AlignCenter}

    def control(self, control, fila, columna, numFilas=1, numColumnas=1, alineacion=None):
        """
        A�ade un control.
        """
        self.addWidget(control, fila, columna, numFilas, numColumnas, self.dicAlineacion[alineacion])
        return self

    def controld(self, control, fila, columna, numFilas=1, numColumnas=1):
        """
        A�ade un control.
        """
        self.addWidget(control, fila, columna, numFilas, numColumnas, self.dicAlineacion["d"])
        return self

    def controlc(self, control, fila, columna, numFilas=1, numColumnas=1):
        """
        A�ade un control.
        """
        self.addWidget(control, fila, columna, numFilas, numColumnas, self.dicAlineacion["c"])
        return self

    def otro(self, layout, fila, columna, numFilas=1, numColumnas=1, alineacion=None):
        """
        A�ade otro layout.
        """
        self.addLayout(layout, fila, columna, numFilas, numColumnas, self.dicAlineacion[alineacion])
        return self

    def otroc(self, layout, fila, columna, numFilas=1, numColumnas=1):
        """
        A�ade otro layout.
        """
        self.addLayout(layout, fila, columna, numFilas, numColumnas, self.dicAlineacion["c"])
        return self

    def otrod(self, layout, fila, columna, numFilas=1, numColumnas=1):
        """
        A�ade otro layout.
        """
        self.addLayout(layout, fila, columna, numFilas, numColumnas, self.dicAlineacion["d"])
        return self

    def margen(self, n):
        """
        Margen exterior.
        """
        self.setContentsMargins(n, n, n, n)
        return self

    def rellenoColumna(self, col, factor):
        """
        A�ade espacio de relleno, que ocupa lo que puede seg�n un factor = stretch.
        """
        self.setColumnStretch(col, factor)
        return self

    def columnaVacia(self, column, minSize):
        self.setColumnMinimumWidth(column, minSize)
        return self

    def filaVacia(self, row, minSize):
        self.setRowMinimumHeight(row, minSize)
        return self

# class FlowLayout(QtGui.QLayout):
    # def __init__(self, parent=None, margin=0, spacing=-1):
        # super(FlowLayout, self).__init__(parent)

        # if parent is not None:
            # self.setMargin(margin)

        # self.setSpacing(spacing)

        # self.itemList = []

    # def __del__(self):
        # item = self.takeAt(0)
        # while item:
            # item = self.takeAt(0)

    # def addItem(self, item):
        # self.itemList.append(item)

    # def count(self):
        # return len(self.itemList)

    # def itemAt(self, index):
        # if 0 <= index < len(self.itemList):
            # return self.itemList[index]

        # return None

    # def takeAt(self, index):
        # if 0 <= index < len(self.itemList):
            # return self.itemList.pop(index)

        # return None

    # def expandingDirections(self):
        # return QtCore.Qt.Orientations(QtCore.Qt.Orientation(0))

    # def hasHeightForWidth(self):
        # return True

    # def heightForWidth(self, width):
        # height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        # return height

    # def setGeometry(self, rect):
        # super(FlowLayout, self).setGeometry(rect)
        # self.doLayout(rect, False)

    # def sizeHint(self):
        # return self.minimumSize()

    # def minimumSize(self):
        # size = QtCore.QSize()

        # for item in self.itemList:
            # size = size.expandedTo(item.minimumSize())

        # size += QtCore.QSize(2 * self.margin(), 2 * self.margin())
        # return size

    # def doLayout(self, rect, testOnly):
        # x = rect.x()
        # y = rect.y()
        # lineHeight = 0

        # for item in self.itemList:
            # wid = item.widget()
            # spaceX = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton,
                                                                # QtGui.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            # spaceY = self.spacing() + wid.style().layoutSpacing(QtGui.QSizePolicy.PushButton,
                                                                # QtGui.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            # nextX = x + item.sizeHint().width() + spaceX
            # if nextX - spaceX > rect.right() and lineHeight > 0:
                # x = rect.x()
                # y = y + lineHeight + spaceY
                # nextX = x + item.sizeHint().width() + spaceX
                # lineHeight = 0

            # if not testOnly:
                # item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))

            # x = nextX
            # lineHeight = max(lineHeight, item.sizeHint().height())

        # return y + lineHeight - rect.y()

# def juntaH(control1, control2):
    # return H().control(control1).control(control2).relleno()
