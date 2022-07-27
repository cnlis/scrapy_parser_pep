from settings import BASE_DIR

class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        return item

    def close_spider(self, spider):
        pass
