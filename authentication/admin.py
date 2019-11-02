from django.contrib import admin
from .models import DaemonStar_User
from  item_view.models import Item, Comments

# Register your models here.

admin.site.register(DaemonStar_User)
admin.site.register(Item)
admin.site.register(Comments)