from django.contrib import admin
from .models import Point, Profile, Announcement, FAQ


admin.site.register(Announcement)
admin.site.register(FAQ)
admin.site.register(Point)

class ProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data Information', {'fields' : ['address']})
    ]
    list_display = ('user', 'address')
admin.site.register(Profile, ProfileAdmin)