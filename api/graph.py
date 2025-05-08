import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List
import common.models
from common.database import get_db
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper, StrawberrySQLAlchemyLoader

mapper = StrawberrySQLAlchemyMapper()

@mapper.type(common.models.Region)
class Region:
    pass

@mapper.type(common.models.Nation)
class Nation:
    pass

@mapper.type(common.models.Customer)
class Customer:
    pass

def get_db_with_loader(info: strawberry.Info):
        db = next(get_db(bearer=info.context["request"].headers.get("X-Forwarded-Access-Token")))
        info.context["sqlalchemy_loader"] = StrawberrySQLAlchemyLoader(bind=db)
        return db
    
@strawberry.type
class Query:
    @strawberry.field
    def customers(self, info: strawberry.Info) -> List[Customer]:
        db = get_db_with_loader(info)
        return db.query(common.models.Customer).all()

    @strawberry.field
    def customer(self, id: int, info: strawberry.Info) -> Customer:
        db = get_db_with_loader(info)
        return db.query(common.models.Customer).filter(common.models.Customer.id == id).first()

    @strawberry.field
    def nations(self, info: strawberry.Info) -> List[Nation]:
        db = get_db_with_loader(info)
        return db.query(common.models.Nation).all()

    @strawberry.field
    def nation(self, id: int, info: strawberry.Info) -> Nation:
        db = get_db_with_loader(info)
        return db.query(common.models.Nation).filter(common.models.Nation.id == id).first()

    @strawberry.field
    def regions(self, info: strawberry.Info) -> List[Region]:
        db = get_db_with_loader(info)
        return db.query(common.models.Region).all()

    @strawberry.field
    def region(self, id: int, info: strawberry.Info) -> Region:
        db = get_db_with_loader(info)
        return db.query(common.models.Region).filter(common.models.Region.id == id).first()

mapper.finalize()
schema = strawberry.federation.Schema(query=Query)
router = GraphQLRouter(schema=schema)
