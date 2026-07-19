from io import StringIO
import re
import requests
import pandas as pd

URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
headers = {'User-Agent': 'Mozilla/5.0 (learning-project; manoj@example.com)'}
resp = requests.get(URL, headers=headers, timeout=30)
resp.raise_for_status()
print(URL)

# strip non-digit junk from rowspan/colspan values
html = re.sub(
    r'(rowspan|colspan)\s*=\s*"(\d+)[^"]*"',
    r'\1="\2"',
    resp.text,
    flags=re.IGNORECASE,
)

tables = pd.read_html(StringIO(html))
print(len(tables))
df = tables[0]
print(df.head())