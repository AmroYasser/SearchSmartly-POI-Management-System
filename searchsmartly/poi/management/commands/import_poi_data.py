from django.core.management.base import BaseCommand

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