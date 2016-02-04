from django.db import models
from geopy.geocoders.googlev3 import GoogleV3


class Owner(models.Model):
    name = models.CharField(max_length=255)


class MailingAddress(models.Model):
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)


class Assessment(models.Model):
    land = models.FloatField(blank=True, null=True)
    building = models.FloatField(blank=True, null=True)
    exemption = models.FloatField(blank=True, null=True)
    tax_amount = models.FloatField(blank=True, null=True)

    @property
    def total(self):
        return self.land + self.building

    @property
    def net(self):
        return self.total - self.exemption


class Property(models.Model):
    account_number = models.IntegerField()
    street_number = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    map_lot = models.CharField(max_length=255, blank=True, null=True)
    book_page_1 = models.CharField(max_length=255, blank=True, null=True)
    book_page_2 = models.CharField(max_length=255, blank=True, null=True)
    owners = models.ManyToManyField(Owner, blank=True, null=True)
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

    def save(self, *args, **kwargs):
        location = ' '.join([self.street_number, self.street, self.city, self.state])
        if location:
            if not self.latitude or not self.longitude:
                try:
                    g = geocoders.GoogleV3()
                    result = g.geocode(location)
                    self.latitude = result.latitude
                    self.longitude = result.longitude
                except GQueryError:
                    pass
                except Exception as e:
                    print ('%s', e)

        super(BaseGeo, self).save(*args, **kwargs)


class Building(models.Model):
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
    commercial_occupancy_code = models.IntegerField()
    commercial_dwelling_units = models.IntegerField()




class Sale(models.Model):
    property = models.ForeignKey(Property)
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
