from repositories.trip_repository import TripRepository


class TripService:
    def __init__(self, repository: TripRepository | None = None) -> None:
        self._repository = repository or TripRepository()

    def list_trips(
        self,
        *,
        page: int = 1,
        limit: int = 10,
        destination: str | None = None,
        region: str | None = None,
    ):
        trips = self._repository.list_active(destination=destination, region=region)
        trips.sort(key=lambda item: (not item.get("featured", False), item.get("title", "")))
        return self._repository.paginate(trips, page=page, limit=limit)

    def get_trip_by_id(self, trip_id: str):
        trip = self._repository.get_by_id(trip_id)
        if trip is None or trip.get("status", "active") != "active":
            return None
        return trip

    def get_trip_by_slug(self, slug: str):
        trip = self._repository.get_by_slug(slug)
        if trip is None or trip.get("status", "active") != "active":
            return None
        return trip

    def list_featured(self, limit: int = 6):
        trips = self._repository.list_active(featured_only=True)
        trips.sort(key=lambda item: item.get("title", ""))
        return trips[: max(min(limit, 20), 1)]

    def list_destinations(self):
        return self._repository.list_destinations()
