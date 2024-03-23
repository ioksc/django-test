import graphene
from graphene_django import DjangoObjectType
from api.models import bin_data
class binType(DjangoObjectType):
    class Meta:
        model = bin_data
        fields = ('bin_id','bin_code', 'bin_country', 'bin_type')
        


class Query(graphene.ObjectType):
    hello = graphene.String(tarjeta=graphene.Int(), expiracion=graphene.String())
    bins = graphene.List(binType)

    binid = graphene.Field(binType, bincode=graphene.ID())
    nom = graphene.List(binType, country=graphene.String())
    def resolve_bins(self, info):
        return bin_data.objects.all()
    def resolve_binid(self, info, bincode):
        return bin_data.objects.get(pk=bincode)
    
    def resolve_nom(self, info, country):
        return bin_data.objects.filter(bin_country=country)
    
    def resolve_hello(self, info):

        c = a+b
        return c


schema = graphene.Schema(query=Query)