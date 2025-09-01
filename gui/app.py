import os, sys, PyQt5

from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, \
    QFileDialog, QMenu, QTableWidgetItem, QHeaderView

from filemanager.file_manager import FileManager
from window import Ui_MainWindow

base = os.path.dirname(PyQt5.__file__)
for p in (os.path.join(base, "Qt5", "plugins", "platforms"),
          os.path.join(base, "Qt", "plugins", "platforms")):
    if os.path.isdir(p):
        os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = p
        break


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Интерфейс из Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Кнопка источника файла/папки
        self.ui.btnBrowseFile.setText("Источник…")
        
        # Указываем обработчик на кнопку «Копирование»
        self.ui.btnCopy.clicked.connect(self.copy_clicked)
        self.ui.txtLog.append("Режим: копирование файла/папки")
        
        # Указываем обработчик на кнопку «Удаление»
        self.ui.btnDelete.clicked.connect(self.delete_clicked)
        self.ui.txtLog.append("Режим: удаление")

        # Указываем обработчик на кнопку «Подсчёт файлов»
        self.ui.btnCount.clicked.connect(self.num_files_clicked)
        self.ui.txtLog.append("Режим: подсчёт файлов")

        # Указываем обработчик на кнопку «Поиск файлов»
        self.ui.btnFind.clicked.connect(self.find_file_clicked)
        self.ui.txtLog.append("Режим: поиск файлов")
        
        # ----- Кнопки выбора файлов/директории -----
        # Кнопка-источник: меню «файл / папка»
        self.ui.btnBrowseFile.clicked.connect(self.open_source_menu)
        
        # Кнопка «Директория назначения»
        self.ui.btnBrowseDest.clicked.connect(self.pick_dest_dir)
    
    # ----- обработчики кликов на кнопки -----
    
    def copy_clicked(self):
        """Обрабатывает событие при нажатие на кнопку Копировать"""
        src_path = self.ui.lePath.text().strip()  # из кнопки источник: файл ИЛИ папка
        dest_dir = self.ui.leDest.text().strip()  # директория назначения
        
        if not src_path:
            QMessageBox.information(self, "Копирование",
                                    "Выберите источник (файл или папку).")
            return
        
        try:
            new_path = FileManager.copy_file(src_path, dest_dir or None)
            self.ui.txtLog.append(f"✓ Скопировано в: {new_path}")
            QMessageBox.information(self, "Готово",
                                    f"Скопировано в:\n{new_path}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка копирования", str(e))
            self.ui.txtLog.append(f"[Ошибка] {e}")
    
    def delete_clicked(self):
        """Обрабатывает событие при нажатие на кнопку Удалить"""
        path = self.ui.lePath.text().strip()
        
        if not path:
            QMessageBox.information(self, "Удаление",
                                    "Укажите путь к файлу или директории!")
            return
        
        try:
            FileManager.delete(path)
            self.ui.txtLog.append(f"Удалено: {os.path.basename(path)}!")
            QMessageBox.information(self, "Удаление",
                                    f"Объект {os.path.basename(path)} удалён")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка удаления!", str(e))
            self.ui.txtLog.append(f"[Ошибка] {e}")
    
    def num_files_clicked(self):
        """Обрабатывает событие при нажатие на кнопку Подсчёт файлы"""
        path_dir = self.ui.lePath.text().strip()
        
        if not path_dir:
            QMessageBox.information(self, "Подсчёт файлов",
                                    "Укажите путь к директории!")
            return
        
        try:
            count_files = FileManager.num_files(path_dir)
            self.ui.txtLog.append(
                f"Количество файлов в папке {os.path.basename(path_dir)}: {count_files}")
            QMessageBox.information(self, "Подсчёт файлов",
                                    f"Количество файлов в папке: {count_files}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка подсчёта!", str(e))
            self.ui.txtLog.append(f"[Ошибка подсчёта] {e}")
            
    def find_file_clicked(self):
        """Обрабатывает событие при нажатие на кнопку Поиск файлов"""
        path_dir = self.ui.lePath.text().strip()
        pattern = self.ui.lePattern.text().strip()
        
        if not path_dir:
            QMessageBox.information(self, "Поиск файлов",
                                    "Укажите путь к директории!")
            return
        
        if not pattern:
            QMessageBox.information(self, "Поиск файлов",
                                    "Укажите шаблон для поиска!")
            
        try:
            files = FileManager.find_file(path_dir, pattern)

            # Очистим таблицу
            self.ui.tableResults.clearContents()
            self.ui.tableResults.setRowCount(0)

            if not files:
                self.ui.txtLog.append(
                    f"Совпадений по шаблону «{pattern}» не найдено.")
                QMessageBox.information(self, "Результат поиска",
                                        "Совпадений не найдено.")
                return

            self.ui.tableResults.setRowCount(len(files))

            for row, item in enumerate(files):
                _, dir_path, filename = item
                self.ui.tableResults.setItem(row, 0, QTableWidgetItem(str(row + 1)))
                self.ui.tableResults.setItem(row, 1, QTableWidgetItem(dir_path))
                self.ui.tableResults.setItem(row, 2, QTableWidgetItem(filename))
                self.ui.tableResults.setItem(row, 3, QTableWidgetItem(""))
    
            # Равномерно растягиваем колонки
            header = self.ui.tableResults.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)

            # Переключаем на вкладку «Таблица»
            self.ui.tabWidget.setCurrentWidget(self.ui.tabTable)

            self.ui.txtLog.append(
                f"Выполнен поиск файлов по шаблону: {pattern}")

        except Exception as e:
            QMessageBox.critical(self, "Ошибка поиска!", str(e))
            self.ui.txtLog.append(f"[Ошибка поиска] {e}")
            
        
        
    # -------- пикеры --------
    
    def open_source_menu(self):
        """Выпадающее меню: выбрать файл или папку."""
        menu = QMenu(self)
        act_file = menu.addAction("Выбрать файл…")
        act_dir = menu.addAction("Выбрать папку…")
        
        chosen = menu.exec_(QCursor.pos())
        if chosen is None:
            return
        
        if chosen == act_file:
            self.pick_file()
        elif chosen == act_dir:
            self.pick_dir()
    
    def pick_file(self):
        """Выборать файл"""
        path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл")
        if path:
            self.ui.lePath.setText(path)
    
    def pick_dir(self):
        """Выбрать директорию"""
        path = QFileDialog.getExistingDirectory(self, "Выбрать папку")
        if path:
            self.ui.lePath.setText(path)
    
    def pick_dest_dir(self):
        """Выбрать директорию назначения"""
        path = QFileDialog.getExistingDirectory(self,
                                                "Выбрать директорию назначения")
        if path:
            self.ui.leDest.setText(path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # base_dir = os.path.dirname(os.path.abspath(__file__))
    # icon_path = os.path.join(base_dir, "icons", "icon.ico")
    # app.setWindowIcon(QIcon(icon_path))
    w = MainWindow()
    w.setWindowTitle("Файл менеджер")
    w.resize(900, 600)
    w.show()
    sys.exit(app.exec_())
