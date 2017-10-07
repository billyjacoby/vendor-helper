import graphene

from graphene_django.types import DjangoObjectType

from website.models import IncentiveModel

class IncentiveModelType(DjangoObjectType):
    class Meta:
        model = IncentiveModel

class Query(graphene.AbstractType):
    all_incentive_models = graphene.List(IncentiveModelType)

    def resolve_all_incentive_models(self, args, context, info):
        return IncentiveModel.objects.all()
