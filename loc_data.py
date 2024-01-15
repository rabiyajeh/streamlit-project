import requests
from bs4 import BeautifulSoup
import csv

# URL
url = 'https://developers.google.com/public-data/docs/canonical/countries_csv' 

response = requests.get(url)

if response.status_code == 200:
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table
    table = soup.find('table')

    # Extract table headers
    headers = [header.text.lower() for header in table.find_all('th')]

    # Extract table rows
    rows = []
    for row in table.find_all('tr')[1:]:
        data = [cell.text for cell in row.find_all('td')]
        rows.append(data)

    # Write to CSV
    with open('country_loc.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    print("CSV file 'country_loc.csv' has been created.")
else:
    print("Failed to retrieve data from the website.")
