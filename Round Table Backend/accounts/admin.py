from django.contrib import admin
from .models import Announcement

# REGISTER MODELS IN DJANGO ADMIN PANEL
admin.site.register(Announcement)

# CUSTOM DJANGO ADMIN BRANDING
admin.site.site_header = "LeTip Round Table Admin"
admin.site.site_title = "LeTip Portal"
admin.site.index_title = "Member Portal Management"