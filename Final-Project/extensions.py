from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# base for new mappings(key value pairs) makes new declared bases
# compatible with type checkers
class Base(DeclarativeBase):
    pass

# initailize db object
db = SQLAlchemy(model_class=Base)