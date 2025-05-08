from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Region(Base):
    __tablename__ = "dim_region"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    comment = Column(String)

    nations = relationship("Nation", back_populates="region")

class Nation(Base):
    __tablename__ = "dim_nation"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    region_key = Column(Integer, ForeignKey("dim_region.id"))
    comment = Column(String)

    region = relationship("Region", back_populates="nations")
    customers = relationship("Customer", back_populates="nation")

class Customer(Base):
    __tablename__ = "dim_customer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    nation_key = Column(Integer, ForeignKey("dim_nation.id"))
    phone_number = Column(String)
    account_balance = Column(Float)
    market_segment = Column(String)
    comment = Column(String)

    nation = relationship("Nation", back_populates="customers") 