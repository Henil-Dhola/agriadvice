from django.contrib import admin
from .models import Crops,Requirements,Users,Services
from .models import ContactMessage

# Register your models here.
admin.site.register(Crops)
admin.site.register(Requirements)
admin.site.register(Users)
admin.site.register(ContactMessage)
admin.site.register(Services)

class CropsAdmin(admin.ModelAdmin):
    list_display = ['name','image']