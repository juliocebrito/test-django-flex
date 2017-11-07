import graphene
from graphene_django.types import DjangoObjectType
from .models import Subcategory

class SubcategoryType(DjangoObjectType):
    class Meta:
        model = Subcategory

class Query(graphene.ObjectType):
    subcategories = graphene.List(SubcategoryType)

    def resolve_subcategories(self, info, **kwargs):
        return Subcategory.objects.all()
