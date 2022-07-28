import csv
import datetime as dt
from collections import Counter

from .constants import BASE_DIR, DATETIME_FORMAT, SUMMARY_FILENAME


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
        file_name = f'{SUMMARY_FILENAME}_{now_formatted}.csv'

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(result)
