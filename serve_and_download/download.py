# Alexandros I. Metsai
# Download a file over http.

import requests


url = 'http://localhost:8000/empty.csv'
r = requests.get(url)
print('sdfsdfs')
open('../new_file.csv', 'wb').write(r.content)
