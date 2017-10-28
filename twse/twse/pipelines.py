from sqlalchemy.orm import sessionmaker

from twse.models import Trades, create_trades_table, db_connect


class TwsePipeline(object):
    def __init__(self):
        engine = db_connect()
        create_trades_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        deal = Trades(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
