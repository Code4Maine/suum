from datetime import datetime
from csv import DictReader
from django.core.management.base import BaseCommand, CommandError
from property.models import Property, Owner, MailingAddress, Assessment, Building, Sale

class Command(BaseCommand):
    help = 'Imports property from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('path')

        parser.add_argument('--assessment-date',
            dest='adate',
            default=False,
            help='Assessment date for the document (yyyy-mm-dd format)')

    def convert_to_float(self, string):
        try:
            value = float(string.strip(' ').replace('$', '').replace(',',''))
        except ValueError:
            value = None
        return value

    def handle(self, *args, **options):
        file_path = options['path']
        adate = datetime.strptime(options['adate'], '%Y-%m-%d')

        f = open(file_path)
        items = DictReader(f)
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
            p.book_page_1=d['Book & Page']
            p.save()

            a,created = Assessment.objects.get_or_create(assoc_property=p, date=adate)
            if created:
                print('Adding assessment for {0}'.format(adate.year))
                a.land=self.convert_to_float(d['Land Value'])
                a.building=self.convert_to_float(d['Building Value'])
                a.exemption=self.convert_to_float(d['Exemption'])
                a.tax_amount=self.convert_to_float(d['Tax Amount'])
                a.date=adate
                a.save()


            o, created = Owner.objects.get_or_create(name=d["Owner's Name"])

            try:
                o.name_2=d["Owner's Name Part 2"]
                o.save()
            except:
                pass

            p.owners.add(o)
            p.save()

