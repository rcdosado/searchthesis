from django.contrib import admin

from search.models import Thesis 

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'authors','posted_by','publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'posted_by')
    search_fields = ('title', 'abstract')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('posted_by',)
    date_hierarchy = 'publish'
