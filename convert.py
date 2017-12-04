import xml.etree.ElementTree as ET
import csv
import requests

URL = 'http://www.culturegrid.org.uk/index/select/?q=dcterms.isPartOf:MLAInstitutions&version=2.2&start=0&rows=100000&indent=on'

def run():
    req = requests.get(URL)
    file = open('culturedata.xml', 'w')
    file.write(req.text)
    file.close()
    tree = ET.parse("resident_data.xml")
    root = tree.getroot()
    output_csv = open('/culture_data.csv', 'w')
    csv_writer = csv.writer(output_csv)
    for institution in root.findall('doc'):
        csv_writer.writerow([])
    output_csv.close()
