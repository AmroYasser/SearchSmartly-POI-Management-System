import csv
import json
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from poi.models import PoI
import xml.etree.ElementTree as ET


class Command(BaseCommand):
    help = 'Import PoI data from CSV, JSON, or XML files'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        for file_path in options['file_path']:
            if file_path.endswith('.csv'):
                self.import_csv(file_path)
            elif file_path.endswith('.json'):
                self.import_json(file_path)
            elif file_path.endswith('.xml'):
                self.import_xml(file_path)
            else:
                self.stdout.write(self.style.ERROR(f'Unsupported file format: {file_path}'))
                
    def import_csv(self, file_path):
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                ratings = row[5].strip('{}').split(',')
                ratings = [int(float(rating.strip())) for rating in ratings]
                PoI.objects.update_or_create(
                    external_id=row['poi_id'],
                    defaults={
                        'name': row['poi_name'],
                        'category': row['poi_category'],
                        'coordinates': Point(
                            float(row['poi_longitude']),
                            float(row['poi_latitude'])
                        ),
                        'ratings': ratings
                    }
                )
                
    def import_json(self, file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            for poi_data in data:
                PoI.objects.update_or_create(
                    external_id=poi_data['id'],
                    defaults={
                        'name': poi_data['name'],
                        'category': poi_data['category'],
                        'coordinates': Point(
                            poi_data['coordinates'][1],
                            poi_data['coordinates'][0]
                        ),
                        'ratings': [int(rating) for rating in poi_data['ratings']]
                    }
                )
                
    def import_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for poi_element in root.findall('DATA_RECORD'):
            ratings = poi_element.find('pratings').text.split(',')
            ratings = [int(rating.strip()) for rating in ratings]
            PoI.objects.update_or_create(
                external_id=poi_element.find('pid').text,
                defaults={
                    'name': poi_element.find('pname').text,
                    'category': poi_element.find('pcategory').text,
                    'coordinates': Point(
                        float(poi_element.find('plongitude').text),
                        float(poi_element.find('platitude').text)
                    ),
                    'ratings': ratings
                }
            )