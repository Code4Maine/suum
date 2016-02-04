from csv import DictReader
from django.core.management.base import BaseCommand, CommandError
from property.models import Property, Owner, MailingAddress, Assessment, Building, Sale

class Command(BaseCommand):
    help = 'Imports property from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('path')


    def handle(self, *args, **options):
        file_path = options['path']

        f = open(file_path)
        items = DictReader(f)
        csv_troop_numbers = []
        for d in items:
            print('Checking for existing property with ID #{0} at {1} {2}'.format(d['Account Number'],
                                                                                  d['Street Number'],
                                                                                  d['Street Name']))
            (p, created) = Property.objects.get_or_create(account_number=d['Account Number'])
            if created:
                print('Created new property')
            else:
                print('Updating existing property')

            p.account_number=d['Account Number']
            p.street_number=d['Street Number']
            p.street=d['Street Name']
            p.city='Bangor'
            p.state='Maine'
            p.map_lot=d['Map/Lot']
            p.save()

            o, created = Owner.objects.get_or_create(name=d["Owner's Name"])

            try:
                o.name_2=d["Owner's Name Part 2"]
                o.save()
            except:
                pass

            p.owners.add(o)
            p.save()

