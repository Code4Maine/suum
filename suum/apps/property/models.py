from django.db import models


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
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)


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
