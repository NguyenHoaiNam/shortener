# -*- coding: utf8 -*-
import config

from sqlalchemy import create_engine
from shortener.model.models import Base

engine = create_engine(config.DATABASE_URI, echo=True)

if __name__ == '__main__':
    # Create a table with three columns as Url class
    Base.metadata.create_all(engine)
