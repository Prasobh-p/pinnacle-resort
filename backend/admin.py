from django.contrib import admin
from backend.models import Accomdb, Roomdb, Fooddb, Fooditeamsdb
from pinnacleinn.models import Condb, Registerdb, Hostdb, Paymentdb

# Register backend models
admin.site.register(Accomdb)
admin.site.register(Roomdb)
admin.site.register(Fooddb)
admin.site.register(Fooditeamsdb)

# Register pinnacleinn models
admin.site.register(Condb)
admin.site.register(Registerdb)
admin.site.register(Hostdb)
admin.site.register(Paymentdb)

