from django.contrib import admin
from .models import *
from store.models import *

# Register your models here.
admin.site.register(Juma_User)
admin.site.register(Item_Type)
admin.site.register(Item)
admin.site.register(History)