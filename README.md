# FileManager

**Утилита для управления файлами и папками через командную строку.**

Работает с копированием, удалением, подсчётом файлов, поиском по шаблону, добавлением даты к имени файла и анализом размера содержимого.

---

## Установка

```bash
git clone https://github.com/VladimirUstinov5690/cli_manager
cd <папка_проекта>
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
# Использование

Запускается через командную строку:

```bash
python main.py <команда> [аргументы]
```

### Копирование файла
```bash
python main.py copy путь_к_файлу [путь_к_директории_назначения]
```

### Удаление файла или папки
```bash
python main.py delete путь_к_файлу_или_папке
```

### Подсчёт количества файлов в папке
```bash
python main.py num_files путь_к_директории
```

### Поиск файлов по шаблону
```bash
python main.py find путь_к_директории шаблон
Шаблон поддерживает * и ? (как в fnmatch).
python main.py find ./logs *.log
```

### Добавить дату к имени файла
```bash
python main.py add_date путь_к_файлу_или_папке [--recursive]
```

### Анализ папки (размер содержимого)
```bash
python main.py analyze [путь_к_директории]
```