import graphene

from graphene_django.types import DjangoObjectType

from website.models import IncentiveModel

class IncentiveModelType(DjangoObjectType):
    class Meta:
        model = IncentiveModel

class Query(graphene.AbstractType):
    all_incentive_models = graphene.List(IncentiveModelType)

    incentive_model = graphene.Field(IncentiveModelType,
                                    id=graphene.Int())

    incentive_model_by_supplier = graphene.List(IncentiveModelType,
                                                supplier=graphene.String())

    def resolve_all_incentive_models(self, args, context, info):
        return IncentiveModel.objects.all()

    def resolve_incentive_model(self, args, context, info):
        id = args.get('id')
        supplier = args.get('supplier')

        if id is not None:
            return IncentiveModel.objects.get(pk=id)

        if supplier is not None:
            return IncentiveModel.objects.filter(supplier=supplier)

        return None

    def resolve_incentive_model_by_supplier(self, args, context, info):
        supplier = args.get('supplier')

        if supplier is not None:
            return IncentiveModel.objects.filter(supplier=supplier)

        return None
