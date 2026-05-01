# DAST Scanner Example

# Import necessary libraries
import requests

# Define the DAST scanner URL and parameters
scanner_url = 'http://localhost:5000/scan'
headers = {'Content-Type': 'application/json'}

# Define the payload for the scan
payload = {
    'url': 'https://example.com',  # Target URL to scan
    'options': {
        'depth': 2,
        'timeout': 60
    }
}

# Make a request to the DAST scanner
try:
    response = requests.post(scanner_url, json=payload, headers=headers)
    response.raise_for_status()  # Raise an error on a bad response
    print('Scan started successfully:', response.json())
except requests.exceptions.RequestException as e:
    print('Error starting scan:', e)