import graphene
from categories.schema import Query as categories
from subcategories.schema import Query as subcategories
from products.schema import Query as products
from services.schema import Query as services

class Query(categories,
            subcategories,
            products,
            services,
            graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
