from marcus_sdk.registration import StoreRegistration


def register() -> StoreRegistration:
    return StoreRegistration(
        store_id="store_lab",
        version="1.1.0",
        metadata={
            "name": "Store Lab Travel",
            "description": "Experimental travel store — trip catalog queries",
            "category": "travel",
        },
        hosts=[
            "store-lab.localhost",
            "store-lab.hoshisky.com",
        ],
    )
