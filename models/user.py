from sqlalchemy import Column, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship

from utils.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    user_name = Column(String, nullable=True)
    tg_id = Column(BigInteger, nullable=True)


class Category(Base):
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(String, nullable=False)

    #####################
    # Relationships
    #####################
    products = relationship("Products", back_populates="category")


class Products(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(String, nullable=True)
    category_id = Column(BigInteger, ForeignKey("categories.id"), onupdate="SET NULL")

    #####################
    # Relationships
    #####################
    category = relationship("Category", back_populates="products")
    image = relationship("Images", back_populates="product")


class Images(Base):
    __tablename__ = "images"
    id = Column(BigInteger, primary_key=True, unique=True)
    url = Column(String, nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.id"), onupdate="SET NULL")

    #####################
    # Relationships
    #####################
    product = relationship("Products", back_populates="image")
