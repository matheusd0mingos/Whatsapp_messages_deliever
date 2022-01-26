from PyQt5 import QtGui, QtWidgets, QtCore
class CustomTableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(CustomTableModel, self).__init__()
        self.load_data(data)

    def load_data(self, data):
        self.input_Pessoa = data[0].values
        self.input_Telefone = data[1].values
        self.input_Negocio = data[2].values
        self.input_verificacao = data[3].values
        self.input_status=data[4].values

        self.column_count = 5
        self.row_count = len(self.input_Pessoa)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QtCore.QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        if role != QtCore.Qt.DisplayRole:
            return None
        if orientation == QtCore.Qt.Horizontal:
            
            return ("Pessoa", "Telefone", 'Negocio', 'wpp verificado', 'Tentativa envio')[section]
        else:
            return "{}".format(section)

    def data(self, index, role = QtCore.Qt.DisplayRole):
        column = index.column()
        row = index.row()

        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                raw_user = self.input_Pessoa[row]
                
                return raw_user
            elif column == 1:
                return self.input_Telefone[row]
            elif column==2:
                return self.input_Negocio[row]
            elif column==3:
                return self.input_verificacao[row]

            elif column==4:
                return self.input_status[row]

        elif role == QtCore.Qt.BackgroundRole:
            return QtGui.QColor(QtCore.Qt.white)
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignRight

        return None
