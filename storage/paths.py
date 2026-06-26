from pathlib import Path

import config

COLLECTION_TRIPS = "trips"
COLLECTION_SETTINGS = "settings"


def data_dir() -> Path:
    return config.DATA_DIR


def collection_path(name: str) -> Path:
    return data_dir() / f"{name}.json"
