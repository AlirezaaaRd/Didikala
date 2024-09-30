from django.contrib import admin
from .models import (
    Comment, Point, IsUseful, 
    Image
)

admin.site.register(IsUseful)
admin.site.register(Point)
admin.site.register(Comment)
admin.site.register(Image)
