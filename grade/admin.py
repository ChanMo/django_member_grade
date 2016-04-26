from django.contrib import admin
from .models import *

class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'growth')

class GradeAdmin(admin.ModelAdmin):
    list_display = ('member', 'grade', 'growth')
    list_per_page = 20
    list_filter = ('grade',)

class LogAdmin(admin.ModelAdmin):
    list_display = ('member', 'type', 'value', 'description', 'created')
    list_per_page = 20
    list_filter = ('type', 'created')
    search_fields = ['description']

admin.site.register(Rule, RuleAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Log, LogAdmin)
