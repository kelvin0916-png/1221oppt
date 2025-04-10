import requests
from time import sleep

def is_alive(subdomain):
    retries = 3  # Number of retries if the request fails
    timeout = 10  # Timeout in seconds for each request

    for _ in range(retries):
        try:
            for scheme in ['http://', 'https://']:  # Try both HTTP and HTTPS
                url = f"{scheme}{subdomain}"
                # Ignore SSL certificate errors for subdomains with issues
                response = requests.get(url, timeout=timeout, verify=False)
                if response.status_code < 400:  # If status code is less than 400, the subdomain is alive
                    return True
        except requests.RequestException as e:
            print(f"❌ Error: {e}")
            sleep(2)  # Wait 2 seconds before retrying
    return False  # Return False if the subdomain is still not reachable after retries
