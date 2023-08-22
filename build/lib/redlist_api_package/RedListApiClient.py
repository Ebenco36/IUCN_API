import requests

class RedListApiClient:
    def __init__(self, api_key):
        self.base_url = "https://apiv3.iucnredlist.org/api/v3"
        self.api_key = api_key
        self.categories = {
            "DD": "DD", "LC": "LC", "NT": "NT", 
            "VU": "VU", "EN": "EN", "CR": "CR", 
            "EW": "EW", "EX": "EX", "LRlc": "LR/lc", 
            "LRnt": "LR/nt", "LRcd": "LR/cd"
        }

    def _make_request(self, endpoint, params=None):
        params = params or {}
        params["token"] = self.api_key
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()
    
    

    

    
    

    

    

    
    


    

    
    
    
