import graphene


from data.graphql_models.user_object import User as User
from data.models.users_model import UserModel as UserModel
from services import database


class UserMutation(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        hashedPassword = graphene.String()
        isActive = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, info, email, *args):
        user = UserModel(email=email)
        database.SessionLocal.add(user)
        database.SessionLocal.commit()
        return UserMutation(user=user)


class Mutation(graphene.ObjectType):
    mutate_user = UserMutation.Field()
