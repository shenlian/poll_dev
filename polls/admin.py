#coding=UTF-8
from polls.models import Poll,Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    #在POLL的Admin中直接添加Choice实体
    model = Choice
    extra = 3 



#在admin中添加Poll模型
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'],'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)