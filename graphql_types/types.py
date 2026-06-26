import strawberry


@strawberry.type
class TripDay:
    day: int
    title: str
    description: str
    activities: list[str]


@strawberry.type
class Trip:
    id: str
    slug: str
    title: str
    destination: str
    region: str
    duration_days: int = strawberry.field(name="durationDays")
    duration_nights: int = strawberry.field(name="durationNights")
    price_from: float = strawberry.field(name="priceFrom")
    currency: str
    rating: float
    review_count: int = strawberry.field(name="reviewCount")
    cover_image: str = strawberry.field(name="coverImage")
    summary: str
    highlights: list[str]
    itinerary: list[TripDay]
    included: list[str]
    excluded: list[str]
    departure_cities: list[str] = strawberry.field(name="departureCities")
    featured: bool
    status: str

    @classmethod
    def from_dict(cls, data: dict) -> "Trip":
        itinerary = [
            TripDay(
                day=day.get("day", 0),
                title=day.get("title", ""),
                description=day.get("description", ""),
                activities=list(day.get("activities", [])),
            )
            for day in data.get("itinerary", [])
        ]
        return cls(
            id=data["id"],
            slug=data["slug"],
            title=data["title"],
            destination=data["destination"],
            region=data.get("region", ""),
            duration_days=data.get("duration_days", 1),
            duration_nights=data.get("duration_nights", 0),
            price_from=float(data.get("price_from", 0)),
            currency=data.get("currency", "VND"),
            rating=float(data.get("rating", 0)),
            review_count=int(data.get("review_count", 0)),
            cover_image=data.get("cover_image", ""),
            summary=data.get("summary", ""),
            highlights=list(data.get("highlights", [])),
            itinerary=itinerary,
            included=list(data.get("included", [])),
            excluded=list(data.get("excluded", [])),
            departure_cities=list(data.get("departure_cities", [])),
            featured=bool(data.get("featured", False)),
            status=data.get("status", "active"),
        )


@strawberry.type
class TripConnection:
    items: list[Trip]
    total: int
    page: int
    limit: int
    has_next_page: bool = strawberry.field(name="hasNextPage")

    @classmethod
    def from_page(cls, items: list[Trip], total: int, page: int, limit: int) -> "TripConnection":
        start = (page - 1) * limit
        return cls(
            items=items,
            total=total,
            page=page,
            limit=limit,
            has_next_page=start + limit < total,
        )


@strawberry.type
class DestinationSummary:
    name: str
    trip_count: int = strawberry.field(name="tripCount")

    @classmethod
    def from_dict(cls, data: dict) -> "DestinationSummary":
        return cls(name=data["name"], trip_count=int(data.get("trip_count", 0)))
