from sqlalchemy import Column, Integer, ForeignKey, DateTime
from data_base.dbcore import Base
from sqlalchemy.orm import relationship, backref  # для связки таблиц
from models.product import Products  # импорт модели продукто


class Order(Base):
    __table__ = "orders"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    data = Column(DateTime)
    product_id = Column(Integer, ForeignKey("products.id"))
    user_id = Column(Integer)

    products = relationship(Products, backref=backref('orders', uselist=True, cascade="delete,all"))

    def __str__(self):
        return f"{self.quantity} {sel.data}"
