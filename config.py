"""Store configuration — patched at runtime by Marcus store_runtime."""

from pathlib import Path
from typing import Any

from marcus_sdk.config import StoreConfig
from marcus_sdk.storage import JsonStorageProvider, StorageProvider

STORE_ID = "store_lab"
DATA_DIR = Path("data")
STORAGE: StorageProvider | None = None
DEFAULT_CURRENCY = "VND"
MAX_LIST_ITEMS = 50


def configure(store_config: StoreConfig, storage: JsonStorageProvider) -> None:
    global DATA_DIR, STORAGE, DEFAULT_CURRENCY

    DATA_DIR = store_config.data_dir
    STORAGE = storage
    DEFAULT_CURRENCY = store_config.default_currency

    from storage.provider import reset_storage_provider

    reset_storage_provider()
