# Alexandros I. Metsai
# alexmetsai@gmail.com

import requests
import xmltodict
import xml.etree.ElementTree as ET

def xml_to_dict_from_url(url):
    """
    Return ordered dict with XML contents.
    
    :param url: The url of the xml document.
    """
    response = requests.get(url)
    return xmltodict.parse(response.content)

def xml_tree_from_url(url):
    """
    Return root using the Element Tree XML API.
    
    :param url: The url of the xml document.
    """
    response = requests.get(url)
    return ET.fromstring(response.content)
