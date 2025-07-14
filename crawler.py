import requests
from bs4 import BeautifulSoup


def get_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")
    return forms

def get_form_details(form):
    details = {}
    action = form.attrs.get("action")
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details['action'] = action
    details['method'] = method
    details['inputs'] = inputs
    return details

# Example usage:
if __name__ == "__main__":
    url = input("Enter URL to scan: ")
    forms = get_forms(url)
    print(f"[+] Found {len(forms)} form(s) on {url}")
    for form in forms:
        details = get_form_details(form)
        print(details)
