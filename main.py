import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets


class ParameterValueIsWrong(Exception):
    pass


class IdDoesntExistError(Exception):
    pass


class RoastingDegreeDoesntExistError(Exception):
    pass


class GroundAndInGrainsDoesntExistError(Exception):
    pass


class Ui_CoffeeTable(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        MainWindow.setMaximumSize(QtCore.QSize(800, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.coffee_table = QtWidgets.QTableWidget(self.centralwidget)
        self.coffee_table.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(0)
        self.coffee_table.setRowCount(0)
        self.make_or_change_coffee_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_or_change_coffee_button.setGeometry(QtCore.QRect(10, 560, 171, 41))
        self.make_or_change_coffee_button.setObjectName("make_or_change_coffee_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Эспрессо"))
        self.make_or_change_coffee_button.setText(_translate("MainWindow", "Добавить / изменить запись"))


class Ui_ChangeForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 423)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(534, 423))
        MainWindow.setMaximumSize(QtCore.QSize(534, 423))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id_input_label = QtWidgets.QLabel(self.centralwidget)
        self.id_input_label.setGeometry(QtCore.QRect(30, 20, 481, 16))
        self.id_input_label.setObjectName("id_input_label")
        self.id_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_input.setGeometry(QtCore.QRect(30, 50, 471, 20))
        self.id_input.setObjectName("id_input")
        self.info_input_label = QtWidgets.QLabel(self.centralwidget)
        self.info_input_label.setGeometry(QtCore.QRect(30, 90, 181, 16))
        self.info_input_label.setObjectName("info_input_label")
        self.sort_name_label = QtWidgets.QLabel(self.centralwidget)
        self.sort_name_label.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.sort_name_label.setObjectName("sort_name_label")
        self.roasting_degree_label = QtWidgets.QLabel(self.centralwidget)
        self.roasting_degree_label.setGeometry(QtCore.QRect(30, 150, 141, 16))
        self.roasting_degree_label.setObjectName("roasting_degree_label")
        self.ground_and_in_grains_label = QtWidgets.QLabel(self.centralwidget)
        self.ground_and_in_grains_label.setGeometry(QtCore.QRect(30, 180, 141, 16))
        self.ground_and_in_grains_label.setObjectName("ground_and_in_grains_label")
        self.taste_description_label = QtWidgets.QLabel(self.centralwidget)
        self.taste_description_label.setGeometry(QtCore.QRect(30, 210, 141, 16))
        self.taste_description_label.setObjectName("taste_description_label")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(30, 280, 141, 16))
        self.price_label.setObjectName("price_label")
        self.volume_of_packet_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_of_packet_label.setGeometry(QtCore.QRect(30, 310, 141, 16))
        self.volume_of_packet_label.setObjectName("volume_of_packet_label")
        self.sort_name = QtWidgets.QLineEdit(self.centralwidget)
        self.sort_name.setGeometry(QtCore.QRect(180, 120, 321, 20))
        self.sort_name.setObjectName("sort_name")
        self.roasting_degree = QtWidgets.QLineEdit(self.centralwidget)
        self.roasting_degree.setGeometry(QtCore.QRect(180, 150, 321, 20))
        self.roasting_degree.setObjectName("roasting_degree")
        self.ground_or_in_grains = QtWidgets.QLineEdit(self.centralwidget)
        self.ground_or_in_grains.setGeometry(QtCore.QRect(180, 180, 321, 20))
        self.ground_or_in_grains.setObjectName("ground_or_in_grains")
        self.taste_description = QtWidgets.QTextEdit(self.centralwidget)
        self.taste_description.setGeometry(QtCore.QRect(180, 210, 321, 61))
        self.taste_description.setObjectName("taste_description")
        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(180, 280, 321, 20))
        self.price.setObjectName("price")
        self.volume_of_packet = QtWidgets.QLineEdit(self.centralwidget)
        self.volume_of_packet.setGeometry(QtCore.QRect(180, 310, 321, 20))
        self.volume_of_packet.setObjectName("volume_of_packet")
        self.make_changes_button = QtWidgets.QPushButton(self.centralwidget)
        self.make_changes_button.setGeometry(QtCore.QRect(380, 342, 121, 31))
        self.make_changes_button.setObjectName("make_changes_button")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(30, 350, 331, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cappucino"))
        self.id_input_label.setText(_translate("MainWindow", "Введите ID заменяемой записи (если хотите только создать новую, оставьте поле пустым):"))
        self.info_input_label.setText(_translate("MainWindow", "Введите данные новой записи:"))
        self.sort_name_label.setText(_translate("MainWindow", "Название кофе:"))
        self.roasting_degree_label.setText(_translate("MainWindow", "Степень обжарки (id):"))
        self.ground_and_in_grains_label.setText(_translate("MainWindow", "Молотый/в зёрнах (id):"))
        self.taste_description_label.setText(_translate("MainWindow", "Описание вкуса:"))
        self.price_label.setText(_translate("MainWindow", "Цена:"))
        self.volume_of_packet_label.setText(_translate("MainWindow", "Объём упаковки:"))
        self.make_changes_button.setText(_translate("MainWindow", "Создать"))


class CoffeeTable(QMainWindow, Ui_CoffeeTable):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.coffee_info = None
        self.change_form = None
        self.fill_table()
        self.make_or_change_coffee_button.clicked.connect(self.init_change_form)

    def init_change_form(self):
        self.change_form = ChangeForm(self)
        self.change_form.show()
        self.hide()

    def fill_table(self):
        self.get_coffee_info()

        self.coffee_info = self.insert_names_of_properties(self.coffee_info)

        self.coffee_table.setColumnCount(len(self.coffee_info[0]))
        self.coffee_table.setRowCount(len(self.coffee_info))

        for i, row in enumerate(self.coffee_info):
            for j, elem in enumerate(row):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(row[j])))
                self.coffee_table.item(i, j).setFlags(Qt.ItemIsEditable)

        self.make_header_of_table()

    def get_coffee_info(self):
        cur = self.con.cursor()
        self.coffee_info = cur.execute("""SELECT * FROM Coffee""").fetchall()

    def insert_names_of_properties(self, coffee_info):
        cur = self.con.cursor()
        roasting_degree, ground_or_in_grains = cur.execute("""SELECT name FROM Roasting_degrees""").fetchall(), \
                                               cur.execute("""SELECT name FROM Ground_and_in_grains""").fetchall()

        for i, coffee in enumerate(coffee_info):
            new_coffee = list(coffee)
            new_coffee[2] = roasting_degree[new_coffee[2]][0]
            new_coffee[3] = ground_or_in_grains[new_coffee[3]][0]

            coffee_info[i] = new_coffee

        return coffee_info

    def make_header_of_table(self):
        self.coffee_table.setHorizontalHeaderLabels(('ID', 'Название кофе', 'Степень обжарки', 'Молотый/в зёрнах',
                                                     'Описание вкуса', 'Цена', 'Объём упаковки'))

        header = self.coffee_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)

    def closeEvent(self, event):
        self.con.close()


class ChangeForm(QMainWindow, Ui_ChangeForm):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.con = sqlite3.connect('data/coffee.sqlite')
        self.make_changes_button.clicked.connect(self.make_changes)

    def make_changes(self):
        try:
            changed_id = self.read_id()
            new_data = self.read_data()

            cur = self.con.cursor()

            if changed_id:
                cur.execute("""UPDATE Coffee
                SET sort_name = ?, roasting_degree = ?, ground_or_in_grains = ?, taste_description = ?, 
                price = ?, volume_of_packet = ?
                WHERE ID = ?""",
                            (new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5], changed_id))
            else:
                cur.execute("""INSERT INTO Coffee(sort_name,roasting_degree,ground_or_in_grains,taste_description,
                price,volume_of_packet) VALUES(?, ?, ?, ?, ?, ?)""",
                            (new_data[0], new_data[1], new_data[2], new_data[3], new_data[4], new_data[5]))

            self.con.commit()
            self.error_label.setText('Данные успешно изменены')
        except ParameterValueIsWrong as err:
            self.error_label.setText(f'Ошибка: {err}')

    def read_id(self):
        cur = self.con.cursor()
        changed_id = self.id_input.text()

        if changed_id == '':
            return changed_id

        if not changed_id.isdigit():
            raise ParameterValueIsWrong('введённый id - не число')
        if not (int(changed_id) in map(lambda x: x[0], cur.execute("""SELECT ID FROM Coffee""").fetchall())):
            raise ParameterValueIsWrong('введённый id не существует')

        return changed_id

    def read_data(self):
        sort_name = self.sort_name.text()
        roasting_degree = self.roasting_degree.text()
        ground_or_in_grains = self.ground_or_in_grains.text()
        taste_description = self.taste_description.toPlainText()
        price = self.price.text()
        volume_of_packet = self.volume_of_packet.text()

        self.check_if_correct_roasting_degree(roasting_degree)
        self.check_if_correct_ground_or_in_grains(ground_or_in_grains)
        self.check_if_correct_price(price)
        self.check_if_correct_volume_of_packet(volume_of_packet)

        return sort_name, int(roasting_degree), int(ground_or_in_grains), taste_description, float(price), float(
            volume_of_packet)

    def check_if_correct_roasting_degree(self, roasting_degree):
        cur = self.con.cursor()
        if not roasting_degree.isdigit():
            raise ParameterValueIsWrong('введённая степень обжарки - не число')
        if not (int(roasting_degree) in map(lambda x: x[0],
                                            cur.execute("""SELECT ID FROM Roasting_degrees""").fetchall())):
            raise ParameterValueIsWrong('введённая степень обжарки не существует')

    def check_if_correct_ground_or_in_grains(self, ground_or_in_grains):
        cur = self.con.cursor()
        if not ground_or_in_grains.isdigit():
            raise ParameterValueIsWrong('введённое молотый / в зёрнах - не число')
        if not (int(ground_or_in_grains) in map(lambda x: x[0],
                                                cur.execute("""SELECT ID FROM Ground_and_in_grains""").fetchall())):
            raise ParameterValueIsWrong('введённое молотый / в зёрнах не существует')

    def check_if_correct_price(self, price):
        if self.is_float(price) is None:
            raise ParameterValueIsWrong('введённая цена не число')

    def check_if_correct_volume_of_packet(self, volume_of_packet):
        if self.is_float(volume_of_packet) is None:
            raise ParameterValueIsWrong('введённый объём упаковки не число')

    def is_float(self, n):
        try:
            x = float(n)
            return x
        except ValueError:
            return None

    def closeEvent(self, event):
        self.con.close()
        self.parent.show()
        self.parent.fill_table()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee_table = CoffeeTable()
    coffee_table.show()
    sys.exit(app.exec())
