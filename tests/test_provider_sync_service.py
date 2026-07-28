"""
ComicMetadataHub Provider Sync Service Test
"""

import sys
import os


PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


sys.path.insert(
    0,
    PROJECT_ROOT
)


from src.services.provider_sync_service import (
    ProviderSyncService
)



class MockUpdater:

    def update(
        self,
        records
    ):

        return len(records)



def test_provider_sync_service():

    print(
        "Testing provider sync service..."
    )


    service = ProviderSyncService()


    count = service.sync(
        [
            {
                "name": "Batman"
            }
        ],
        MockUpdater()
    )


    assert count == 1


    print(
        "Provider sync service test passed"
    )



if __name__ == "__main__":

    test_provider_sync_service()
