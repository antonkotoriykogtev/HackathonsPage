from django.contrib import admin
from .models import EventsModel, Uzer, Post
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


admin.site.register(EventsModel)

admin.site.register(Post)

class UzerInline(admin.StackedInline):
    model = Uzer
    can_delete = False
    verbose_name_plural = 'INFO'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UzerInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)