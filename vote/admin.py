from django.contrib import admin

# Register your models here.
from solo.admin import SingletonModelAdmin
from vote.models import VoteConfiguration

admin.site.register(VoteConfiguration, SingletonModelAdmin)
