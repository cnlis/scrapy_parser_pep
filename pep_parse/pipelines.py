import datetime as dt
from collections import Counter
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        self.counter[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)

        with open(
                BASE_DIR / 'results' / f'status_summary_{now_formatted}.csv',
                'w', encoding='utf-8'
        ) as f:
            f.write('Статус,Количество\n')
            for key, value in self.counter.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{sum(self.counter.values())}\n')
