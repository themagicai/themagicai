from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class User(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if len(str(obj.password)) < 30:
            obj.set_password(obj.password)
        super(User, self).save_model(request, obj, form, change)

