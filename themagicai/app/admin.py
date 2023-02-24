from django.contrib import admin

from themagicai.app.models import Skill


@admin.register(Skill)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    search_fields = ["name"]
    list_filter = ["is_active"]
