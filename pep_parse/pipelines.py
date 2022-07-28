import csv
import datetime as dt
from collections import Counter

from .constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        self.counter[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        result = [('Статус', 'Количество')]
        result.extend(self.counter.items())
        result.append(('Total', self.counter.total()))

        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)

        with open(
                BASE_DIR / 'results' / f'status_summary_{now_formatted}.csv',
                'w', encoding='utf-8'
        ) as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(result)
