class APIDiscovery:
    """
    A class to handle endpoint discovery from Swagger/OpenAPI specs,
    Postman collections, and direct API exploration.
    """

    def __init__(self):
        pass

    def from_swagger(self, swagger_spec):
        """
        Discover endpoints from a Swagger/OpenAPI specification.
        Parameters:
            swagger_spec (dict): The Swagger/OpenAPI specification as a dictionary.
        """
        # Implementation for endpoint discovery from Swagger spec

    def from_postman(self, postman_collection):
        """
        Discover endpoints from a Postman collection.
        Parameters:
            postman_collection (dict): The Postman collection as a dictionary.
        """
        # Implementation for endpoint discovery from Postman collection

    def explore_api(self, base_url):
        """
        Explore endpoints directly from an API.
        Parameters:
            base_url (str): The base URL of the API.
        """
        # Implementation for direct API exploration

    def discover(self, source):
        """
        Discover endpoints from the provided source, which can be a Swagger spec,
        Postman collection, or an API URL.
        Parameters:
            source (Union[dict, str]): The source for discovery.
        """
        if isinstance(source, dict):
            if 'swagger' in source or 'openapi' in source:
                return self.from_swagger(source)
            else:
                return self.from_postman(source)
        elif isinstance(source, str):
            return self.explore_api(source)
        else:
            raise ValueError('Invalid source type. Must be a dict or str.')
