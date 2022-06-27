from django.contrib import admin
from home.models import firstTerm
from home.models import secondTerm
from home.models import DefaultValues
from home.models import DefaultMinValues
from home.models import ObtainedMarks



# Register your models here.
admin.site.register(firstTerm)
admin.site.register(secondTerm)
admin.site.register(DefaultValues)
admin.site.register(DefaultMinValues)
admin.site.register(ObtainedMarks)