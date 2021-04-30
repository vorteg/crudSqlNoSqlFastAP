import graphene
from data.graphql_mutations.user_mutations import Mutation
from data.graphql_queries.query import Query


schema = graphene.Schema(query=Query,  mutation=Mutation)
