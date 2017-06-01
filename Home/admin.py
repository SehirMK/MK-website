from django.contrib import admin
from Home.models import Topic, People, AccessRecord
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(People)