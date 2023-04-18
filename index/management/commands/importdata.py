from django.core.management.base import BaseCommand
from index.models import District, Taluka, Block, Sector,Village, AWC
import csv

class Command(BaseCommand):
    help = 'Imports AWC data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', help='Path to CSV file')

    def handle(self, *args, **options):
        filename = options['filename']
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader)
            for row in reader:
                print(row)
                district, created = District.objects.get_or_create(name=row['District_name'])
                taluka, created = Taluka.objects.get_or_create(name=row['Taluka_name'], district=district)
                block, created = Block.objects.get_or_create(name=row['Block_name'], taluka=taluka)
                sector, created = Sector.objects.get_or_create(name=row['Sector_name'], block=block)
                village, created = Village.objects.get_or_create(name=row['Village'], sector=sector)
                awc = AWC.objects.create(name=row['Awc_Name'], village=village, sector=sector, awccode =row['Awc_ Code'])
                self.stdout.write(self.style.SUCCESS(f'Successfully imported AWC {awc.name}'))

