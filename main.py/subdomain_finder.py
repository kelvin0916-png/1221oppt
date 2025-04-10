import requests

def find_subdomains(domain):
    api_key = "4af960e8df6f342b3e43304ccd5a35f44244f7c004e63afd75b71eafa9126b76"  # Replace this with your real key
    url = f"https://www.virustotal.com/api/v3/domains/{domain}/subdomains"
    headers = {
        "x-apikey": api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subdomains = [item['id'] for item in data['data']]
        return subdomains
    else:
        print("Error:", response.status_code, response.text)
        return []
