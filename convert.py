import xml.etree.ElementTree as ET
import csv
import requests

URL = 'http://www.culturegrid.org.uk/index/select/?q=dcterms.isPartOf:MLAInstitutions&version=2.2&start=0&rows=100000&indent=on'


def run():
    # Commented out but would be used to get a fresh copy of the XML
    # req = requests.get(URL)
    # file = open('./culture_data.xml', 'w', encoding='utf-8')
    # file.write(req.text)
    # file.close()
    tree = ET.parse('culture_data.xml')
    root = tree.getroot()
    output_csv = open('culture_data.csv', 'w', encoding='utf-8')
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
            'postcode': '',
            'longitude': '',
            'latitude': '',
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
            if prop.get('name') == 'aggregator.internal.id':
                inst['internal_id'] = prop.text
            if prop.get('name') == 'aggregator.internal_record_link':
                inst['internal_record_link'] = prop.text
            if prop.get('name') == 'authority':
                inst['authority'] = prop.text
            if prop.get('name') == 'authority_name':
                inst['authority_name'] = prop.text
            if prop.get('name') == 'cg_original_record_prefix':
                inst['cg_original_record_prefix'] = prop.text
            if prop.get('name') == 'cg_schema_id':
                inst['cg_schema_id'] = prop.text
            if prop.get('name') == 'cg_schema_name':
                inst['cg_schema_name'] = prop.text
            if prop.get('name') == 'cg_schema_type':
                inst['cg_schema_type'] = prop.text
            if prop.get('name') == 'dc.identifier':
                inst['identifier'] = prop.text
            if prop.get('name') == 'dc.related.link':
                inst['related_link'] = prop.text
            if prop.get('name') == 'dc.titleString':
                inst['title'] = prop.text
            if prop.get('name') == 'dcterms.isPartOf_AllIDs':
                inst['is_part_of_all_ids'] = prop.text
            if prop.get('name') == 'dcterms.isPartOf_AllNames':
                inst['is_part_of_all_names'] = prop.text
            if prop.get('name') == 'disabledAccess':
                inst['disabled_access'] = prop.text
            if prop.get('name') == 'institution_address':
                inst['institution_address'] = prop.text
            if prop.get('name') == 'institution_sector':
                inst['institution_sector'] = prop.text
            if prop.get('name') == 'institution_type':
                inst['institution_type'] = prop.text
            if prop.get('name') == 'oai_is.alternativeName':
                inst['alternative_name'] = prop.text
            if prop.get('name') == 'oai_is.jurisdiction':
                inst['jurisdiction'] = prop.text
            if prop.get('name') == 'oai_is.mlaRegion':
                inst['region'] = prop.text
            if prop.get('name') == 'oai_is.referral':
                inst['referral'] = prop.text
            if prop.get('name') == 'oai_is.website':
                inst['website'] = prop.text
            if prop.get('name') == 'pndsterms.thumbnail':
                inst['thumbnail'] = prop.text
            if prop.get('name') == 'record_type':
                inst['record_type'] = prop.text
            if prop.get('name') == 'restp':
                inst['service_provider'] = prop.text
            if prop.get('name') == 'vcard.email':
                inst['email'] = prop.text
            if prop.get('name') == 'vcard.fax':
                inst['fax'] = prop.text
            if prop.get('name') == 'vcard.voice':
                inst['voice'] = prop.text

        for prop in institution.findall('arr'):
            if prop.get('name') == 'dc.description':
                inst['description'] = prop[0].text
            if prop.get('name') == 'dcmi.type':
                inst['type'] = prop[0].text
            if prop.get('name') == 'oai_is.alternativeName':
                inst['alternative_name'] = prop[0].text
            if prop.get('name') == 'vcard.email':
                inst['email'] = prop[0].text
            if prop.get('name') == 'unparsed.postcode':
                inst['postcode'] = prop[0].text

        for prop in institution.findall('date'):
            if prop.get('name') == 'timestamp':
                inst['timestamp'] = prop[0].text

        for prop in institution.findall('double'):
            if prop.get('name') == 'lat':
                inst['latitude'] = prop[0].text
            if prop.get('name') == 'lng':
                inst['longitude'] = prop[0].text

        row = [
            inst['internal_id'],
            inst['internal_record_link'],
            inst['authority'],
            inst['authority_name'],
            inst['cg_original_record_prefix'],
            inst['cg_schema_id'],
            inst['cg_schema_name'],
            inst['cg_schema_type'],
            inst['description'],
            inst['identifier'],
            inst['related_link'],
            inst['title'],
            inst['dcmi_type'],
            inst['is_part_of_all_ids'],
            inst['is_part_of_all_names'],
            inst['disabled_access'],
            inst['institution_address'],
            inst['postcode'],
            inst['longitude'],
            inst['latitude'],
            inst['sector'],
            inst['institution_type'],
            inst['usage_conditions'],
            inst['administrative_status'],
            inst['alternative_name'],
            inst['jurisdiction'],
            inst['region'],
            inst['referral'],
            inst['website'],
            inst['thumbnail'],
            inst['record_type'],
            inst['service_provider'],
            inst['timestamp'],
            inst['email'],
            inst['fax'],
            inst['voice']
        ]
        csv_writer.writerow(row)

    output_csv.close()

run()
