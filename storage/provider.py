from typing import Any

from marcus_sdk.storage import JsonStorageProvider

from storage.paths import data_dir


class TripStorageProvider:
    def __init__(self, raw: JsonStorageProvider | None = None) -> None:
        self._raw = raw or JsonStorageProvider(data_dir())

    def load(self, collection: str) -> list[dict[str, Any]]:
        return self._raw.load(collection)

    def get_by_id(self, collection: str, item_id: str) -> dict[str, Any] | None:
        return next((item for item in self.load(collection) if item.get("id") == item_id), None)

    def get_by_slug(self, collection: str, slug: str) -> dict[str, Any] | None:
        normalized = slug.strip().lower()
        return next(
            (item for item in self.load(collection) if item.get("slug", "").lower() == normalized),
            None,
        )


_default_provider: TripStorageProvider | None = None


def get_storage_provider() -> TripStorageProvider:
    global _default_provider
    if _default_provider is None:
        import config as store_config

        data_dir().mkdir(parents=True, exist_ok=True)
        raw = store_config.STORAGE
        if raw is not None and isinstance(raw, JsonStorageProvider):
            _default_provider = TripStorageProvider(raw)
        else:
            _default_provider = TripStorageProvider()
    return _default_provider


def reset_storage_provider() -> None:
    global _default_provider
    _default_provider = None
