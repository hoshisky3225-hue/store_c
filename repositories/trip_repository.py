from typing import Any

from storage.paths import COLLECTION_TRIPS
from storage.provider import get_storage_provider


class TripRepository:
    def __init__(self, storage=None) -> None:
        self._storage = storage or get_storage_provider()

    def list_all(self) -> list[dict[str, Any]]:
        return self._storage.load(COLLECTION_TRIPS)

    def get_by_id(self, trip_id: str) -> dict[str, Any] | None:
        return self._storage.get_by_id(COLLECTION_TRIPS, trip_id)

    def get_by_slug(self, slug: str) -> dict[str, Any] | None:
        return self._storage.get_by_slug(COLLECTION_TRIPS, slug)

    def list_active(
        self,
        *,
        destination: str | None = None,
        region: str | None = None,
        featured_only: bool = False,
    ) -> list[dict[str, Any]]:
        items = [trip for trip in self.list_all() if trip.get("status", "active") == "active"]
        if featured_only:
            items = [trip for trip in items if trip.get("featured")]
        if destination:
            needle = destination.strip().lower()
            items = [trip for trip in items if trip.get("destination", "").lower() == needle]
        if region:
            needle = region.strip().lower()
            items = [trip for trip in items if trip.get("region", "").lower() == needle]
        return items

    def paginate(
        self,
        trips: list[dict[str, Any]],
        page: int = 1,
        limit: int = 10,
    ) -> tuple[list[dict[str, Any]], int]:
        page = max(page, 1)
        limit = max(min(limit, 50), 1)
        start = (page - 1) * limit
        end = start + limit
        return trips[start:end], len(trips)

    def list_destinations(self) -> list[dict[str, Any]]:
        counts: dict[str, int] = {}
        for trip in self.list_active():
            destination = trip.get("destination", "").strip()
            if destination:
                counts[destination] = counts.get(destination, 0) + 1
        return [
            {"name": name, "trip_count": count}
            for name, count in sorted(counts.items(), key=lambda item: item[0])
        ]
