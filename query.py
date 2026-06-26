import strawberry


@strawberry.type
class Query:
    @strawberry.field(name="storeLabPing")
    def store_lab_ping(self) -> str:
        return "store_lab:ok"

    @strawberry.field(name="storeLabInfo")
    def store_lab_info(self) -> str:
        return "Experimental lab store — Marcus ingestion contract v1"
