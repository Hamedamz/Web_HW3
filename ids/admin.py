from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('remote_address', 'user_agent', 'date_time')


admin.site.register(Report, ReportAdmin)
