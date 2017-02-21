import utils
import sqlite3
from pecan import expose, redirect

from db_create import engine
from shortener.model import models
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()


class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @expose()
    def link(self, arg):
        origin_link = utils.get_org_link_by_short_link(session, arg)
        redirect(origin_link)

    @index.when(method='POST', template='output.html')
    def index_post(self, o_link):
        s_link = utils.rand()
        record = models.Url(org_link=o_link, short_link=s_link)
        try:
            session.add(record)
            session.commit()
        except Exception:
            s_link = utils.get_short_link_by_org_link(session, o_link)
        return dict(short_link=utils.get_short_url(s_link))




