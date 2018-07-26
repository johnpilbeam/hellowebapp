from django.contrib import admin

# Register your models here.

# import your model 
from collection.models import Thing, Social

# set up automated slug creation 
class ThingAdmin(admin.ModelAdmin): 
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}
    
# our new admin for the Social model
class SocialAdmin(admin.ModelAdmin): 
    model = Social
    list_display = ('network', 'username',)

# and register it
admin.site.register(Thing, ThingAdmin)
admin.site.register(Social, SocialAdmin)