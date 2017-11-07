import graphene
from graphene_django.types import DjangoObjectType
from .models import Service

class ServiceType(DjangoObjectType):
    class Meta:
        model = Service

class Query(graphene.ObjectType):
    services = graphene.List(ServiceType)

    def resolve_services(self, info, **kwargs):
        return Service.objects.all()
