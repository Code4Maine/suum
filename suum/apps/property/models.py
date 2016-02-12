import time
from django.conf import settings
from django.db import models
from geopy.geocoders import Nominatim


class MailingAddress(models.Model):
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)


class Owner(models.Model):
    name = models.CharField(max_length=255)
    name_2 = models.CharField(max_length=255, blank=True, null=True)
    address = models.ForeignKey(MailingAddress, blank=True, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    account_number = models.IntegerField()
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    map_lot = models.CharField(max_length=255, blank=True, null=True)
    book_page_1 = models.CharField(max_length=255, blank=True, null=True)
    book_page_2 = models.CharField(max_length=255, blank=True, null=True)
    owners = models.ManyToManyField(Owner, blank=True)
    acerage = models.FloatField(null=True, blank=True)
    neighborhood = models.IntegerField(null=True, blank=True)
    tree_growth = models.IntegerField(null=True, blank=True)
    zoning = models.IntegerField(null=True, blank=True)
    zoning_secondary = models.IntegerField(null=True, blank=True)
    topography = models.IntegerField(null=True, blank=True)
    utilities = models.IntegerField(null=True, blank=True)
    street_surface = models.IntegerField(null=True, blank=True)
    tif_district = models.IntegerField(null=True, blank=True)
    traffic_flow = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'properties'

    def __str__(self):
        return '{0} {1}, {2}, {3}'.format(self.street_number, self.street,
                                     self.city, self.state)

    def save(self, *args, **kwargs):
        if self.street_number and self.street:
            location = ' '.join([self.street_number, self.street, self.city, self.state])
            # TODO: Check if the location info has changed from the last save
            if not self.latitude:
                try:
                    self.lookup_location(location)
                except Exception as e:
                    print ('%s', e)

        super(Property, self).save(*args, **kwargs)

    @property
    def property_delta(self):
        try:
            assess_15 = self.assessment_set.filter(date__year=2015)[0]
            assess_14 = self.assessment_set.filter(date__year=2014)[0]
            delta = assess_14.land - assess_15.land
        except:
            delta = None
        return delta


    def lookup_location(self, location):
        geocoder = Nominatim()
        result = geocoder.geocode(location)
        self.latitude = result.latitude
        self.longitude = result.longitude
        time.sleep(1)

        return result


class Assessment(models.Model):
    assoc_property = models.ForeignKey(Property)
    land = models.FloatField(blank=True, null=True)
    building = models.FloatField(blank=True, null=True)
    exemption = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return '{0} assessment of {1}'.format(self.date.year, self.assoc_property)

    @property
    def total(self):
        return self.land + self.building

    @property
    def net(self):
        return self.total - self.exemption


class Building(models.Model):
    assoc_property = models.ForeignKey(Property)
    style = models.IntegerField()
    dwelling_units = models.IntegerField()
    other_units = models.IntegerField()
    stories = models.IntegerField()
    exterior_walls = models.IntegerField()
    roof = models.IntegerField()
    sq_footage_masonry_trim = models.FloatField()
    street_setback = models.IntegerField()
    basement_floor = models.IntegerField()
    year_built = models.IntegerField()
    year_remodeled = models.IntegerField()
    foundtion = models.IntegerField()
    basement = models.IntegerField()
    basement_garage_num_cars = models.IntegerField()
    sq_footage_basement_living_area = models.FloatField()
    finished_basement_grade = models.IntegerField()
    finished_basement_factor = models.IntegerField()
    heat_type = models.IntegerField()
    cool_type = models.IntegerField()
    kitchen_style = models.IntegerField()
    bath_style = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    full_baths = models.IntegerField()
    half_baths = models.IntegerField()
    additional_fixtures = models.IntegerField()
    fireplaces = models.IntegerField()
    attic = models.IntegerField()
    insulation = models.IntegerField()
    percent_unfinished = models.FloatField()
    grade = models.FloatField()
    factor = models.IntegerField()
    sq_footage = models.FloatField()
    condition = models.IntegerField()
    sq_living_area = models.FloatField()
    comm_occupancy_code = models.IntegerField()
    comm_dwelling_units = models.IntegerField()
    comm_building_class = models.IntegerField()
    comm_building_quality = models.IntegerField()
    comm_grade_factor = models.IntegerField()
    comm_exterior_walls = models.IntegerField()
    comm_stories = models.IntegerField()
    comm_height = models.IntegerField()
    comm_ground_floor_area = models.IntegerField()
    comm_perimeter = models.IntegerField()
    comm_heating_cooling = models.IntegerField()
    comm_year_built = models.IntegerField()
    comm_year_remodeled = models.IntegerField()
    comm_condition = models.IntegerField()
    comm_sq_footage = models.FloatField()
    model_name_type = models.CharField(max_length=255)
    code = models.IntegerField()
    year = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return 'Building on {0}'.format(self.assoc_property)


class Sale(models.Model):
    assoc_property = models.ForeignKey(Property)
    amount = models.FloatField()
    financing = models.IntegerField(default=0)
    date = models.DateField()
    verified = models.IntegerField()
    validity = models.IntegerField()
    tran_code = models.IntegerField()
    land_code = models.IntegerField()
    book_page = models.CharField(max_length=255)
    previous_owner = models.CharField(max_length=255)
    sale_type = models.IntegerField(default=0)

    def __str__(self):
        return 'Sale of {0}'.format(self.assoc_property)
