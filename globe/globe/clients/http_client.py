import requests


class HttpClient:
    """
    This class expects the clients to handle errors. It doesn't do that for any kind of calls.
    """

    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers

    def get(self):
        """
        return the fetched results as json
        """
        r = requests.get(url=self.url, headers=self.headers)
        return r.json()
    
    def set_url(self, url):
        """
        Update the url for future calls
        """
        self.url = url
    
    def set_headers(self, headers):
        """
        update the headers for future calls
        """
        self.headers = headers
    
    def post(self, body):
        """
        make a post call and return response as result
        """
        r = requests.post(url=self.url, headers=self.headers, body=body)
        return r.json()
    
    def put(self, body):
        """
        make an update call and return response as result
        """
        r = requests.put(url=self.url, headers=self.headers, body=body)
        return r.json()
    
    def delete(self):
        """
        make a delete call and return response as result
        """
        r = requests.delete(url=self.url, headers=self.headers)
        return r.json()