# Alexandros I. Metsai
# alexmetsai@gmail.com

import requests
import xmltodict

def xml_to_dict_from_url(url):
    response = requests.get(url)
    return xmltodict.parse(response.content)
