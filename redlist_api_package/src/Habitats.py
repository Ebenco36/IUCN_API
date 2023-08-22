from redlist_api_package.RedListApiClient import RedListApiClient

class Habitats (RedListApiClient):

    def __init__(self, api_key:str = ""):
        super().__init__(api_key)



    """
        View organism habitats using name, id and region identifier
    
    """
    def get_species_habitat_by_name(self, species_name):
        endpoint = f"{self.base_url}/habitats/species/name/{species_name}"
        return self._make_request(endpoint)

    def get_species_habitat_by_name_by_region(self, species_name, region_identifier):
        endpoint = f"{self.base_url}/habitats/species/name/{species_name}/region/{region_identifier}"
        return self._make_request(endpoint)

    def get_species_habitat_by_id(self, species_id):
        endpoint = f"{self.base_url}/habitats/species/id/{species_id}"
        return self._make_request(endpoint)

    def get_species_habitat_by_id_by_region(self, species_id, region_identifier):
        endpoint = f"{self.base_url}/habitats/species/id/{species_id}/region/{region_identifier}"
        return self._make_request(endpoint)
    