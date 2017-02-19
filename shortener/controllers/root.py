from pecan import expose, redirect
from webob.exc import status_map
from shortener.model import models
from sqlalchemy.orm import sessionmaker

from db_create import engine
import utils


Session = sessionmaker(bind=engine)
session = Session()


class RootController(object):

    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @index.when(method='POST', template='json')
    def index_post(self, o_link):
        s_link = utils.rand()
        record = models.Url(org_link=o_link, short_link=s_link)
        try:
            session.add(record)
            session.commit()
        except Exception as e:
            raise e
        return {'short your link': utils.get_short_url(s_link)}

    @expose()
    def link(self, arg):
        origin_link = utils.get_org_link_by_short_link(session, arg)
        redirect(origin_link)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

