from django.contrib import admin

from rent_company.models import Customer
from rent_company.models import Private_owener
from rent_company.models import Enterprise_owner
from rent_company.models import Branch_Office
from rent_company.models import Staff
from rent_company.models import House_property
from rent_company.models import Advertisement
from rent_company.models import News
from rent_company.models import Record
from rent_company.models import Rent_contract
from rent_company.models import Ad_details

admin.site.register(Customer)
admin.site.register(Private_owener)
admin.site.register(Enterprise_owner)
admin.site.register(Branch_Office)
admin.site.register(Staff)
admin.site.register(House_property)
admin.site.register(Advertisement)
admin.site.register(News)
admin.site.register(Record)
admin.site.register(Rent_contract)
admin.site.register(Ad_details)






