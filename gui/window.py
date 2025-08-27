from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 635)
        MainWindow.setStyleSheet("\n"
"QMainWindow { background: #F4F6F8; color: #1F2937; }\n"
"QWidget { font-family: -apple-system, \"Segoe UI\", Roboto, Arial; font-size: 10.5pt; }\n"
"\n"
"#leftPanel {\n"
"  background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #5C7EBE, stop:1 #2E5C9A);\n"
"  padding: 14px;\n"
"}\n"
"#leftPanel QLabel {\n"
"  color: #EAF1FF;\n"
"  font-weight: 700;\n"
"  font-size: 18px;\n"
"  margin-bottom: 6px;\n"
"}\n"
"#leftPanel QPushButton {\n"
"  color: #EAF1FF;\n"
"  background: rgba(255,255,255,0.08);\n"
"  border: 1px solid rgba(255,255,255,0.18);\n"
"  border-radius: 10px;\n"
"  height: 40px;\n"
"  text-align: left;\n"
"  padding-left: 12px;\n"
"  font-weight: 600;\n"
"}\n"
"#leftPanel QPushButton:hover { background: rgba(255,255,255,0.16); }\n"
"#leftPanel QPushButton:pressed { background: rgba(255,255,255,0.24); }\n"
"\n"
"QGroupBox {\n"
"  background: #FFFFFF;\n"
"  border: 1px solid #E5E7EB;\n"
"  border-radius: 12px;\n"
"  margin-top: 8px;\n"
"  padding-top: 16px;\n"
"  font-weight: 600;\n"
"}\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  left: 10px; top: -6px;\n"
"  background: transparent;\n"
"  padding: 0 6px;\n"
"}\n"
"\n"
"QLabel { color: #1F2937; }\n"
"QLineEdit, QTextEdit {\n"
"  background: #FFFFFF;\n"
"  border: 1px solid #E5E7EB;\n"
"  border-radius: 8px;\n"
"  padding: 6px 10px;\n"
"}\n"
"QLineEdit:focus, QTextEdit:focus { border: 1px solid #5C7EBE; }\n"
"\n"
"#btnRun {\n"
"  background: #E6784A;\n"
"  color: #FFFFFF;\n"
"  border: 1px solid #E6784A;\n"
"  border-radius: 10px;\n"
"  height: 40px;\n"
"  font-weight: 700;\n"
"  padding: 6px 14px;\n"
"}\n"
"#btnRun:hover { background: #D96A3D; }\n"
"#btnRun:pressed { background: #C65E36; }\n"
"\n"
"QTabBar::tab {\n"
"  background: #FFFFFF;\n"
"  border: 1px solid #E5E7EB;\n"
"  border-bottom-color: #FFFFFF;\n"
"  padding: 6px 10px;\n"
"  border-top-left-radius: 8px;\n"
"  border-top-right-radius: 8px;\n"
"  margin-right: 6px;\n"
"}\n"
"QTabBar::tab:selected { background: #F9FAFB; }\n"
"QTabWidget::pane {\n"
"  border: 1px solid #E5E7EB;\n"
"  border-radius: 8px;\n"
"  top: -1px;\n"
"}\n"
"QHeaderView::section {\n"
"  background: #F3F4F6;\n"
"  border: 1px solid #E5E7EB;\n"
"  padding: 6px 8px;\n"
"  font-weight: 600;\n"
"  border-radius: 4px;\n"
"}\n"
"QTableWidget {\n"
"  background: #FFFFFF;\n"
"  border: 1px solid #E5E7EB;\n"
"  border-radius: 8px;\n"
"}\n"
"QTableWidget::item:selected { background: #DBEAFE; color: #111827; }\n"
"QToolTip {\n"
"  color: #111827;\n"
"  background-color: #FFFFFF;\n"
"  border: 1px solid #E5E7EB;\n"
"  padding: 6px 8px;\n"
"  border-radius: 8px;\n"
"}\n"
"   ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.rootLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName("rootLayout")
        self.leftLayout = QtWidgets.QVBoxLayout()
        self.leftLayout.setContentsMargins(-1, -1, 10, -1)
        self.leftLayout.setSpacing(10)
        self.leftLayout.setObjectName("leftLayout")
        self.lblOperations = QtWidgets.QLabel(self.centralwidget)
        self.lblOperations.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblOperations.setObjectName("lblOperations")
        self.leftLayout.addWidget(self.lblOperations)
        self.btnCopy = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopy.setMaximumSize(QtCore.QSize(249, 42))
        self.btnCopy.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnCopy.setObjectName("btnCopy")
        self.leftLayout.addWidget(self.btnCopy)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnDelete.setObjectName("btnDelete")
        self.leftLayout.addWidget(self.btnDelete)
        self.btnCount = QtWidgets.QPushButton(self.centralwidget)
        self.btnCount.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnCount.setObjectName("btnCount")
        self.leftLayout.addWidget(self.btnCount)
        self.btnFind = QtWidgets.QPushButton(self.centralwidget)
        self.btnFind.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnFind.setObjectName("btnFind")
        self.leftLayout.addWidget(self.btnFind)
        self.btnAddDate = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddDate.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnAddDate.setObjectName("btnAddDate")
        self.leftLayout.addWidget(self.btnAddDate)
        self.btnAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnalyze.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.leftLayout.addWidget(self.btnAnalyze)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.leftLayout.addItem(spacerItem)
        self.rootLayout.addLayout(self.leftLayout)
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setSpacing(14)
        self.rightLayout.setObjectName("rightLayout")
        self.groupParams = QtWidgets.QGroupBox(self.centralwidget)
        self.groupParams.setTitle("")
        self.groupParams.setObjectName("groupParams")
        self.paramsGrid = QtWidgets.QGridLayout(self.groupParams)
        self.paramsGrid.setSpacing(8)
        self.paramsGrid.setObjectName("paramsGrid")
        self.lblPath = QtWidgets.QLabel(self.groupParams)
        self.lblPath.setObjectName("lblPath")
        self.paramsGrid.addWidget(self.lblPath, 0, 0, 1, 1)
        self.lePath = QtWidgets.QLineEdit(self.groupParams)
        self.lePath.setObjectName("lePath")
        self.paramsGrid.addWidget(self.lePath, 0, 1, 1, 1)
        self.browseLayout = QtWidgets.QHBoxLayout()
        self.browseLayout.setSpacing(6)
        self.browseLayout.setObjectName("browseLayout")
        self.btnBrowseFile = QtWidgets.QPushButton(self.groupParams)
        self.btnBrowseFile.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnBrowseFile.setObjectName("btnBrowseFile")
        self.browseLayout.addWidget(self.btnBrowseFile)
        self.paramsGrid.addLayout(self.browseLayout, 0, 2, 1, 1)
        self.lblDest = QtWidgets.QLabel(self.groupParams)
        self.lblDest.setObjectName("lblDest")
        self.paramsGrid.addWidget(self.lblDest, 1, 0, 1, 1)
        self.leDest = QtWidgets.QLineEdit(self.groupParams)
        self.leDest.setObjectName("leDest")
        self.paramsGrid.addWidget(self.leDest, 1, 1, 1, 1)
        self.btnBrowseDest = QtWidgets.QPushButton(self.groupParams)
        self.btnBrowseDest.setStyleSheet("QPushButton {\n"
"    background-color: #5C7EBE;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4969A6;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #324A80;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnBrowseDest.setObjectName("btnBrowseDest")
        self.paramsGrid.addWidget(self.btnBrowseDest, 1, 2, 1, 1)
        self.lblPattern = QtWidgets.QLabel(self.groupParams)
        self.lblPattern.setObjectName("lblPattern")
        self.paramsGrid.addWidget(self.lblPattern, 2, 0, 1, 1)
        self.lePattern = QtWidgets.QLineEdit(self.groupParams)
        self.lePattern.setObjectName("lePattern")
        self.paramsGrid.addWidget(self.lePattern, 2, 1, 1, 2)
        self.chkRecursive = QtWidgets.QCheckBox(self.groupParams)
        self.chkRecursive.setObjectName("chkRecursive")
        self.paramsGrid.addWidget(self.chkRecursive, 3, 0, 1, 1)
        self.runRow = QtWidgets.QHBoxLayout()
        self.runRow.setObjectName("runRow")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.runRow.addItem(spacerItem1)
        self.btnRun = QtWidgets.QPushButton(self.groupParams)
        self.btnRun.setStyleSheet("QPushButton {\n"
"    background-color: #ff7f00;   /* обычное состояние */\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e66900;   /* при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #993d00;   /* при клике */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #A0AEC0;   /* неактивная */\n"
"    color: #E2E8F0;\n"
"}")
        self.btnRun.setObjectName("btnRun")
        self.runRow.addWidget(self.btnRun)
        self.paramsGrid.addLayout(self.runRow, 3, 1, 1, 2)
        self.rightLayout.addWidget(self.groupParams)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabTable = QtWidgets.QWidget()
        self.tabTable.setObjectName("tabTable")
        self.tableLayout = QtWidgets.QVBoxLayout(self.tabTable)
        self.tableLayout.setObjectName("tableLayout")
        self.tableResults = QtWidgets.QTableWidget(self.tabTable)
        self.tableResults.setObjectName("tableResults")
        self.tableResults.setColumnCount(4)
        self.tableResults.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableResults.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResults.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResults.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableResults.setHorizontalHeaderItem(3, item)
        self.tableResults.horizontalHeader().setStretchLastSection(True)
        self.tableResults.verticalHeader().setStretchLastSection(True)
        self.tableLayout.addWidget(self.tableResults)
        self.tabWidget.addTab(self.tabTable, "")
        self.tabLogs = QtWidgets.QWidget()
        self.tabLogs.setObjectName("tabLogs")
        self.logsLayout = QtWidgets.QVBoxLayout(self.tabLogs)
        self.logsLayout.setObjectName("logsLayout")
        self.txtLog = QtWidgets.QTextEdit(self.tabLogs)
        self.txtLog.setReadOnly(True)
        self.txtLog.setObjectName("txtLog")
        self.logsLayout.addWidget(self.txtLog)
        self.tabWidget.addTab(self.tabLogs, "")
        self.rightLayout.addWidget(self.tabWidget)
        self.rootLayout.addLayout(self.rightLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FileManager GUI"))
        self.lblOperations.setText(_translate("MainWindow", "Операции"))
        self.btnCopy.setText(_translate("MainWindow", "Копирование"))
        self.btnDelete.setText(_translate("MainWindow", "Удаление"))
        self.btnCount.setText(_translate("MainWindow", "Подсчёт файлов"))
        self.btnFind.setText(_translate("MainWindow", "Поиск файлов"))
        self.btnAddDate.setText(_translate("MainWindow", "Добавить дату"))
        self.btnAnalyze.setText(_translate("MainWindow", "Анализ папки"))
        self.lblPath.setText(_translate("MainWindow", "Путь:"))
        self.lePath.setPlaceholderText(_translate("MainWindow", "Введите путь или выберите…"))
        self.btnBrowseFile.setText(_translate("MainWindow", "Файл/Папка…"))
        self.lblDest.setText(_translate("MainWindow", "Директория назначения:"))
        self.leDest.setPlaceholderText(_translate("MainWindow", "Директория назначения…"))
        self.btnBrowseDest.setText(_translate("MainWindow", "Выбрать…"))
        self.lblPattern.setText(_translate("MainWindow", "Шаблон:"))
        self.lePattern.setPlaceholderText(_translate("MainWindow", "например: *.log"))
        self.chkRecursive.setText(_translate("MainWindow", "Рекурсивный"))
        self.btnRun.setText(_translate("MainWindow", "Выполнить команду"))
        item = self.tableResults.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "№"))
        item = self.tableResults.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Путь"))
        item = self.tableResults.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Имя файла"))
        item = self.tableResults.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Размер"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTable), _translate("MainWindow", "Таблица"))
        self.txtLog.setPlaceholderText(_translate("MainWindow", "Здесь появляются сообщения и результаты…"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLogs), _translate("MainWindow", "Логи"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
