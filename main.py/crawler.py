import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import csv

def crawl(url, depth=2, retries=3, timeout=5, output_file=None):
    if depth == 0:
        return

    for _ in range(retries):
        try:
            response = requests.get(url, timeout=timeout)
            soup = BeautifulSoup(response.text, "html.parser")
            
            links = []
            print(f"\n🔍 Links found on: {url}")
            for link in soup.find_all("a"):
                href = link.get("href")
                if href:
                    absolute_url = urljoin(url, href)
                    # Filter only HTTP/HTTPS links
                    if absolute_url.startswith(("http", "https")):
                        print(absolute_url)
                        links.append(absolute_url)
                        # Recursively crawl the link
                        crawl(absolute_url, depth=depth - 1, retries=retries, timeout=timeout, output_file=output_file)

            # Save to CSV if output file is specified
            if output_file:
                with open(output_file, "a", newline="") as file:
                    writer = csv.writer(file)
                    for link in links:
                        writer.writerow([link])
            
            break  # ✅ Success, so break the retry loop

        except requests.RequestException as e:
            print(f"⚠️ Error crawling {url}: {e}. Retrying...")
            sleep(2)  # Wait before retrying
    else:
        print(f"❌ Failed to crawl {url} after {retries} attempts.")
