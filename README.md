# Open URL Finder

**Open URL Finder** is a Python script designed to scan a domain to find and list all accessible URLs and file paths. The script fetches the HTML content of the specified domain, parses it using BeautifulSoup, and extracts and prints all discovered sub-URLs and file paths.

## Features

- **Sub-URL Extraction:** Identifies all the anchor tags (`<a>`) with valid `href` attributes pointing to sub-URLs within the same domain.
- **File and Path Detection:** Detects files and paths, including those linked through `<img>`, `<script>`, and `<link>` tags.
- **HTML Parsing:** Utilizes BeautifulSoup to parse HTML content, ensuring robust and accurate extraction.

## Prerequisites

To run the Open URL Finder script, ensure you have Python 3 installed along with the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4
