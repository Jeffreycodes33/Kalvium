import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing the election results
url = 'https://results.eci.gov.in/PcResultGenJune2024/index.htm'

# Perform a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the results
table = soup.find('div', class_='rslt-table table-responsive')

# Extract table headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# Extract table rows
rows = []
for tr in table.find_all('tr')[1:]:
    cells = tr.find_all('td')
    row = [cell.text.strip() for cell in cells]
    # Pad the row if it has fewer columns than headers
    while len(row) < len(headers):
        row.append('')
    rows.append(row)

# Create a DataFrame from the extracted data
df = pd.DataFrame(rows, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv('election_results.csv', index=False)

print('Data saved to election_results.csv')
