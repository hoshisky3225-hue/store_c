from typing import Optional

import strawberry
from strawberry.types import Info

from marcus_sdk.context import StoreContext as GraphQLContext
from graphql_types.types import DestinationSummary, Trip, TripConnection
from resolvers.trip_resolver import (
    resolve_destinations,
    resolve_featured_trips,
    resolve_trip,
    resolve_trip_by_slug,
    resolve_trips,
)


@strawberry.type
class Query:
    @strawberry.field(name="storeCPing")
    def store_c_ping(self) -> str:
        return "store_c:ok"

    @strawberry.field
    def trips(
        self,
        info: Info[GraphQLContext, None],
        page: int = 1,
        limit: int = 10,
        destination: Optional[str] = None,
        region: Optional[str] = None,
    ) -> TripConnection:
        return resolve_trips(
            info,
            page=page,
            limit=limit,
            destination=destination,
            region=region,
        )

    @strawberry.field
    def trip(self, info: Info[GraphQLContext, None], id: str) -> Optional[Trip]:
        return resolve_trip(info, id=id)

    @strawberry.field(name="tripBySlug")
    def trip_by_slug(self, info: Info[GraphQLContext, None], slug: str) -> Optional[Trip]:
        return resolve_trip_by_slug(info, slug=slug)

    @strawberry.field(name="featuredTrips")
    def featured_trips(self, info: Info[GraphQLContext, None], limit: int = 6) -> list[Trip]:
        return resolve_featured_trips(info, limit=limit)

    @strawberry.field
    def destinations(self, info: Info[GraphQLContext, None]) -> list[DestinationSummary]:
        return resolve_destinations(info)
