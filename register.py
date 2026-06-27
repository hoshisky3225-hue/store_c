from marcus_sdk.registration import StoreRegistration


def register() -> StoreRegistration:
    return StoreRegistration(
        store_id="store_c",
        version="1.2.0",
        metadata={
            "name": "Store C Travel",
            "description": "Experimental travel store — trip catalog queries",
            "category": "travel",
        },
        hosts=[
            "store-c.localhost",
            "store-c.hoshisky.com",
        ],
    )
