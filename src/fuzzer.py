class APIFuzzer:
    def __init__(self, base_url):
        self.base_url = base_url

    def fuzz_endpoint(self, endpoint, test_cases):
        for case in test_cases:
            response = self.send_request(endpoint, case)
            self.log_response(case, response)

    def send_request(self, endpoint, data):
        import requests
        try:
            response = requests.post(f"{self.base_url}{endpoint}", json=data)
            return response
        except Exception as e:
            return str(e)

    def log_response(self, case, response):
        print(f"Case: {case} - Response: {response.status_code if hasattr(response, 'status_code') else response}")


# Example of how to use APIFuzzer
if __name__ == '__main__':
    fuzzer = APIFuzzer('http://example.com/api')
    test_cases = [
        {'data': 'valid data'},
        {'data': 'invalid data'},
        {'data': ''},  # edge case
        {'malformed': 'malformed'},  # malformed request
    ]
    fuzzer.fuzz_endpoint('/test', test_cases)
