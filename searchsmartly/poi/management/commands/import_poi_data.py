import csv
import json
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand
from poi.models import PoI


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
                PoI.objects.update_or_create(
                    external_id=row['poi_id'],
                    defaults={
                        'name': row['poi_name'],
                        'category': row['poi_category'],
                        'coordinates': Point(
                            float(row['poi_longitude']),
                            float(row['poi_latitude'])
                        ),
                        'ratings': row['poi_ratings'].split(',')
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
                        'ratings': poi_data['ratings']
                    }
                )