import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from data.models.users_model import UserModel as UserModel
from data.graphql_models.user_object import User as User


class Query(graphene.ObjectType):
    node = relay.Node.Field()

    users = graphene.List(lambda: User, id=graphene.ID())
    
    def resolve_users(self, info, id=0):
        query = User.get_query(info)
      
        if id:
            query = query.filter(UserModel.id == id)
        return query.all()
