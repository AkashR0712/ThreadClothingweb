from django.contrib import admin

# Register your models here.
from .models import MenTshirt, WomenTshirt, MenOversizedTshirt, WomenOversizedTshirt

admin.site.register(MenTshirt)
admin.site.register(WomenTshirt)
admin.site.register(MenOversizedTshirt)
admin.site.register(WomenOversizedTshirt)