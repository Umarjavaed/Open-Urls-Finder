import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re

def find_sub_urls_and_files(domain):
    # Normalize the domain URL
    if not domain.startswith('http'):
        domain = 'http://' + domain

    try:
        response = requests.get(domain)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        sub_urls = set()
        files_and_paths = set()

        # Extract and handle anchor tags (<a>)
        for link in soup.find_all('a', href=True):
            href = link.get('href')
            full_url = urljoin(domain, href)
            if urlparse(full_url).netloc == urlparse(domain).netloc:
                sub_urls.add(full_url)
                files_and_paths.update(extract_files_and_paths(href))

        # Extract and handle image tags (<img>)
        for img in soup.find_all('img', src=True):
            src = img.get('src')
            full_url = urljoin(domain, src)
            files_and_paths.add(full_url)

        # Extract and handle script tags (<script>)
        for script in soup.find_all('script', src=True):
            src = script.get('src')
            full_url = urljoin(domain, src)
            files_and_paths.add(full_url)

        # Extract and handle link tags (<link>) for CSS
        for link in soup.find_all('link', href=True):
            href = link.get('href')
            full_url = urljoin(domain, href)
            if 'stylesheet' in link.get('rel', []):
                files_and_paths.add(full_url)

        return sub_urls, files_and_paths

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return set(), set()

def extract_files_and_paths(url):
    # Regex to match files with extensions or paths after domain
    pattern = r'/[^/]+(?:\.[a-zA-Z0-9]+)?(?:/[^/]*)*$'
    matches = re.findall(pattern, url)
    return set(matches)

# Usage
domain = "blsitalypakistan.com"
sub_urls, files_and_paths = find_sub_urls_and_files(domain)

print(f"Found {len(sub_urls)} sub-URLs on {domain}:")
for url in sub_urls:
    print(url)

print(f"\nFound {len(files_and_paths)} files or paths on {domain}:")
for path in files_and_paths:
    print(path)
