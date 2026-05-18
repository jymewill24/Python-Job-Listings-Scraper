import requests
from bs4 import BeautifulSoup
import csv


url = 'https://realpython.github.io/fake-jobs/'

response = requests.get(url)
html_content = ""

# Check if the request was successful (Status code 200)
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to fetch page. Status: {response.status_code}")

print(html_content)  # Print the HTML content to verify it was fetched correctly

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all job listing containers (you'll need to adjust the tag/class based on the actual website)
job_cards = soup.find_all('div', class_='card')

jobs_data = []

for card in job_cards:
    # Extract specific text. Use .strip() to clean up whitespace.
    # Use .text to get the inner text, or .get('href') to get link attributes.

    title = card.find('h2', class_='title is-5').text.strip() or "N/A"
    company = card.find('h3', class_='subtitle is-6 company').text.strip() or "N/A"
    location = card.find('p', class_='location').text.strip() or "N/A"
    job_link = card.find('a', class_='card-footer-item')['href'] or "N/A"

    jobs_data.append([title, company, location, job_link])

# Open a new file in write mode ('w'). 
# newline='' prevents blank lines between rows on Windows.
with open('jobs_export.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row first
    writer.writerow(['Job Title', 'Company', 'Location', 'Job Link'])
    
    # Write the data rows
    writer.writerows(jobs_data)