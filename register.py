from marcus_sdk.registration import StoreRegistration


def register() -> StoreRegistration:
    return StoreRegistration(
        store_id="store_lab",
        version="1.0.0",
        metadata={
            "name": "Store Lab",
            "description": "Minimal experimental store for Marcus ingestion tests",
        },
        hosts=[
            "store-lab.localhost",
            "store-lab.hoshisky.com",
        ],
    )
