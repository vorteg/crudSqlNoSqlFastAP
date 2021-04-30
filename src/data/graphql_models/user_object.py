
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from data.models.users_model import UserModel as UserModel


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
