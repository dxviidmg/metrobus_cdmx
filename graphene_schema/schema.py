import graphene
from graphene_django import DjangoObjectType
from alcaldias.models import State, TownHall
from metrobuses.models import Metrobus


class StateType(DjangoObjectType):
    class Meta:
        model = State
        fields = ("id", "name")

class TownHallType(DjangoObjectType):
    class Meta:
        model = TownHall
        fields = ('__all__')

class MetrobusType(DjangoObjectType):
    class Meta:
        model = Metrobus
        fields = ('id', 'number', 'townhall', 'latitude', 'longitude')

class Query(graphene.ObjectType):
    all_townhalls = graphene.List(TownHallType)
    townhall = graphene.Field(TownHallType, id=graphene.Int())
    all_metrobuses = graphene.List(MetrobusType)
    metrobus = graphene.Field(MetrobusType, id=graphene.Int())

    def resolve_townhall(root, info, id):
        try: 
            return TownHall.objects.get(id=id) 
        except TownHall.DoesNotExist:
            return None
        except Exception as e:
            print(e)
            return None
            
    def resolve_all_townhalls(root, info):
        return TownHall.objects.select_related("state").all()


    def resolve_metrobus(root, info, id):
        try: 
            return Metrobus.objects.get(id=id) 
        except Metrobus.DoesNotExist:
            return None
        except Exception as e:
            print(e)
            return None

    def resolve_all_metrobuses(root, info, **kwargs):
        return Metrobus.objects.all()




schema = graphene.Schema(query=Query)