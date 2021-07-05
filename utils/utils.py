# Alexandros I. Metsai
# alexmetsai@gmail.com

import requests
import xmltodict

def load_xml_from_url(url):
    response = requests.get(url)
    return xmltodict.parse(response.content)
