# -*- coding: utf8 -*-
from sqlalchemy import create_engine
from shortener.model.models import Base
import config

engine = create_engine(config.DATABASE_URI, echo=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
