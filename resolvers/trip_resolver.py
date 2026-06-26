from typing import Optional

from strawberry.types import Info

from marcus_sdk.context import StoreContext as GraphQLContext
from graphql_types.types import DestinationSummary, Trip, TripConnection
from services.trip_service import TripService

_trip_service = TripService()


def resolve_trips(
    info: Info[GraphQLContext, None],
    page: int = 1,
    limit: int = 10,
    destination: Optional[str] = None,
    region: Optional[str] = None,
) -> TripConnection:
    _ = info.context
    rows, total = _trip_service.list_trips(
        page=page,
        limit=limit,
        destination=destination,
        region=region,
    )
    items = [Trip.from_dict(row) for row in rows]
    return TripConnection.from_page(items, total, page, limit)


def resolve_trip(info: Info[GraphQLContext, None], id: str) -> Optional[Trip]:
    _ = info.context
    row = _trip_service.get_trip_by_id(id)
    return Trip.from_dict(row) if row else None


def resolve_trip_by_slug(info: Info[GraphQLContext, None], slug: str) -> Optional[Trip]:
    _ = info.context
    row = _trip_service.get_trip_by_slug(slug)
    return Trip.from_dict(row) if row else None


def resolve_featured_trips(info: Info[GraphQLContext, None], limit: int = 6) -> list[Trip]:
    _ = info.context
    return [Trip.from_dict(row) for row in _trip_service.list_featured(limit=limit)]


def resolve_destinations(info: Info[GraphQLContext, None]) -> list[DestinationSummary]:
    _ = info.context
    return [DestinationSummary.from_dict(row) for row in _trip_service.list_destinations()]
