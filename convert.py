import xml.etree.ElementTree as ET
import csv
import requests

URL = 'http://www.culturegrid.org.uk/index/select/?q=dcterms.isPartOf:MLAInstitutions&version=2.2&start=0&rows=100000&indent=on'

def run():
    # req = requests.get(URL)
    # file = open('./culture_data.xml', 'w', encoding='utf-8')
    # file.write(req.text)
    # file.close()
    tree = ET.parse('culture_data.xml')
    root = tree.getroot()
    output_csv = open('culture_data.csv', 'w')
    csv_writer = csv.writer(output_csv)
    for institution in root[1].findall('doc'):
        # loop through the strings
        inst = {
            'internal_id': '',
            'internal_record_link': '',
            'authority': '',
            'authority_name': '',
            'cg_original_record_prefix': '',
            'cg_schema_id': '',
            'cg_schema_name': '',
            'cg_schema_type': '',
            'description': '',
            'identifier': '',
            'related_link': '',
            'title': '',
            'dcmi_type': '',
            'is_part_of_all_ids': '',
            'is_part_of_all_names': '',
            'disabled_access': '',
            'institution_address': '',
            'sector': '',
            'institution_type': '',
            'usage_conditions': '',
            'administrative_status': '',
            'alternative_name': '',
            'jurisdiction': '',
            'region': '',
            'referral': '',
            'website': '',
            'thumbnail': '',
            'record_type': '',
            'service_provider': '',
            'timestamp': '',
            'email': '',
            'fax': '',
            'voice': ''
        }
        for prop in institution.findall('str'):
            if prop.get('name') == 'institution_sector':
                inst.sector = prop.text
            if prop.get('name') == 'institution_type':
                inst.type = prop.text
    output_csv.close()

run()
