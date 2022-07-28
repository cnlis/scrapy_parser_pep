# Проект парсинга PEP c использованием Scrapy

Требования:
- Python 3.10
- Scrapy 2.5.1

Приложение парсит сайт https://peps.python.org/ для получения 
списка PEP и статистики по статусам документов.

Клонировать исходный код командой
```commandline
git clone https://github.com/cnlis/scrapy_parser_pep.git
```

Установить виртуальное окружение и зависимости
```commandline
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Запуск парсера производить командой
```commandline
scrapy crawl pep
```

Результаты парсинга сохраняются в папке results.