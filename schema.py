"""Optional GraphQL types for store_lab (manifest.schema)."""

import strawberry


@strawberry.type
class LabStatus:
    store_id: str
    version: str
    healthy: bool = True
