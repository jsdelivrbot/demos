from mysite.polls.models import Poll, Choice
from django.contrib import admin


class PollAdmin(admin.ModelAdmin):
	fields = ['pub_data','question']
admin.site.register(Poll)
