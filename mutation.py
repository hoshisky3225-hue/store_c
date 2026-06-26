import strawberry


@strawberry.type
class Mutation:
    @strawberry.mutation
    def echo(self, message: str) -> str:
        return message
