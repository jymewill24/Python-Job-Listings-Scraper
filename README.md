# Python-Job-Listings-Scraper
A Python web scraper that collects job listings from the Fake Python Jobs website. The scraper will extract information such as the job title, company name, location, and a link to the full job description.

## Features
- Fetches HTML content using the `requests` library.
- Parses job titles, company names, locations, and application links using `BeautifulSoup4`.
- Implements Pythonic fallback mechanisms (`or "N/A"`) to handle missing data gracefully.
- Exports the structured data into a clean, Windows-friendly `jobs_export.csv` file.

---

## Prerequisites

Before running the script, ensure you have Python installed on your machine. You will also need to install the required third-party libraries.

### Installation

Clone this repository or download the script file, then install the dependencies using pip:

```bash
pip install requests beautifulsoup4