import requests
from crawler import get_forms, get_form_details
from urllib.parse import urljoin

# Payloads to test
xss_payload = "<script>alert('XSS')</script>"
sqli_payload = "' OR '1'='1"

def scan(url):
    forms = get_forms(url)
    for form in forms:
        details = get_form_details(form)
        data = {}
        
        # Fill in each input with a test payload
        for input in details["inputs"]:
            if input["name"]:
                data[input["name"]] = xss_payload + sqli_payload

        
        target_url = urljoin(url, details["action"])
        print(f"\n[🔎] Scanning form: {target_url}")
        print(f"[📨] Payload sent: {data}")

        try:
            if details["method"] == "post":
                res = requests.post(target_url, data=data)
            else:
                res = requests.get(target_url, params=data)

            content = res.text.lower()

            # Simple checks for reflected payloads or SQL errors
            if xss_payload.lower() in content:
                print("❗ XSS Vulnerability Detected!")
            elif "sql" in content or "syntax error" in content or "mysql" in content:
                print("❗ SQL Injection Vulnerability Detected!")
            else:
                print("✅ No obvious vulnerabilities found.")
        except Exception as e:
            print("❌ Error scanning:", e)

# Run the scanner
if __name__ == "__main__":
    url = input("Enter URL to scan: ")
    scan(url)
