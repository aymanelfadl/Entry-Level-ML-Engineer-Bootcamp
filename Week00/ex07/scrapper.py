import requests
from bs4 import BeautifulSoup
import csv
import sys


def scrapper():
    if len(sys.argv) == 2:
        url = "https://data.1337ai.org/"
        res = requests.get(url)
        
        if res.status_code == 200:
            html = BeautifulSoup(res.text, "html.parser")
            
            heads = html.find_all("th")
            headers = [head.get_text(strip=True) for head in heads]

            rows = html.find_all("tr")
            n_rows = []
            
            for row in rows:
                cells = row.find_all("td")
                if cells:
                    n_row = [cell.get_text(strip=True) for cell in cells]
                    n_rows.append(n_row)

            with open(sys.argv[1], mode="w", newline="", encoding="utf-8") as file:
                pen = csv.writer(file)
                pen.writerow(headers) 
                pen.writerows(n_rows)
                print("done")
        else:
            print(f"Failed to retrieve content. Status code: {res.status_code}")
    else:
        print("Error: Please provide the output CSV file path.")


if __name__ == "__main__":
    scrapper()
