class RequestHandler:
    def __init__(self):
        # Initialize the handler
        self.headers = {}
        self.auth_type = None

    def set_headers(self, headers):
        # Set HTTP headers
        self.headers = headers

    def set_auth(self, auth_type, credentials):
        # Manage authentication
        self.auth_type = auth_type
        self.credentials = credentials

    def handle_request(self, url, method='GET', data=None):
        # Handle HTTP requests
        import requests

        if self.auth_type == 'basic':
            response = requests.request(method, url, headers=self.headers, data=data, auth=self.credentials)
        else:
            response = requests.request(method, url, headers=self.headers, data=data)

        return response

    def handle_content_type(self, content_type, data):
        # Handle different content types
        if content_type == 'application/json':
            import json
            return json.loads(data)
        elif content_type == 'text/xml':
            import xml.etree.ElementTree as ET
            return ET.fromstring(data)
        else:
            return data  # Default case

    def capture_response(self, response):
        # Capture and return the HTTP response
        return {
            'status_code': response.status_code,
            'content': response.content,
            'headers': response.headers,
        }