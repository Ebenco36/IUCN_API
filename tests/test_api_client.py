from Exceptions.APIKeyException import APIKeyException
import pytest
from IUCN_API.modules.Groups import Groups
import logging

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture
def api_client():
    return Groups()

def test_get_species_info(api_client):
    group_list = api_client.get_species_group_list()
    assert group_list
