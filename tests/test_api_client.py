import pytest
from redlist_api_package.src.Groups import Groups
import logging

logging.basicConfig(level=logging.DEBUG)

API_KEY = "9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee"

@pytest.fixture
def api_client():
    return Groups(API_KEY)

def test_get_species_info(api_client):
    group_list = api_client.get_species_group_list()
    assert group_list

