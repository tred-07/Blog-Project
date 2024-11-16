from django.contrib import admin
from .models import Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('categoryType',)}
    list_display=['categoryType','slug']

admin.site.register(Category,CategoryAdmin)