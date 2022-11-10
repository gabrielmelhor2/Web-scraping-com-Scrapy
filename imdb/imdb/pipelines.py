import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ImdbPipeline(object):
    def process_item(self, item, spider):
        self.conn.execute(
            'insert into series(title, year) values (:title, :year)',
            item
        )
        self.conn.commit()
        return item

    def create_table(self):
        result = self.conn.execute(
            'select name from sqlite_master where type = "table" and name = "series"'
        )
        try:
            value = next(result)
        except StopIteration as ex:
            self.conn.execute(
                'create table series(id integer primary key, title text, year text)'
            )

    def open_spider(self, spider):
        self.conn = sqlite3.connect('db.sqlite3')
        self.create_table()

    def close_spider(self, spider):
        self.conn.close()
