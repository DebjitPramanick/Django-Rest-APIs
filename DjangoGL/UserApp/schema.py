import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "name", "age")

class Query(graphene.ObjectType):
    all_users = DjangoListField(UserType)
    def resolve(root, info):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
    def mutate(self, info, name, age):
        user = User(name = name, age = age)
        user.save()
        return CreateUser(user=user)

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)
        age = graphene.Int(required=True)
    def mutate(self, info, id, name, age):
        user = User.objects.get(id=id)
        user.name = name
        user.age = age
        user.save()
        return UpdateUser(user=user)

class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        id = graphene.Int(required=True)
    def mutate(self, info, name, age):
        user = User.objects.get(id=id)
        user.delete()
        return DeleteUser(message="Deleted")

class Mutation(graphene.ObjectType):
    createUser = CreateUser.Field()
    updateUser = UpdateUser.Field()
    deleteUser = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)