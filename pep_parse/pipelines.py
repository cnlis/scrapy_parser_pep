import csv
import datetime as dt
from collections import Counter
from pathlib import Path

from scrapy.exceptions import DropItem

BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        status = item.get('status')
        if not status:
            raise DropItem('Нет ключа "status" в результатах парсинга')
        self.counter[status] += 1
        return item

    def close_spider(self, spider):
        result = [('Статус', 'Количество')]
        result.extend(self.counter.items())
        result.append(('Total', sum(self.counter.values())))

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)

        with open(
                BASE_DIR / 'results' / f'status_summary_{now_formatted}.csv',
                'w', encoding='utf-8'
        ) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(result)
