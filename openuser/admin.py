from .forms import CustomAppUserCreationForm, CustomAppUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from .models import User, OpenuserCreator
from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_header = "Open User Data Administration"


class OpenusercreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'cid', 'username')
    list_display_links = ('id', 'cid', 'username')
    readonly_fields = ('cid', 'username')


class AppUserAdmin(UserAdmin):
    add_form = CustomAppUserCreationForm
    form = CustomAppUserChangeForm

    list_display = ('id', 'uid', 'username', 'email', 'cid', 'app_name')
    list_display_links = ('uid', 'username', 'email')
    list_filter = ('cid', "app_name")

    add_fieldsets = (
        ("Identification", {"fields": ("username", "email", "app_name")}),
        ("Security", {"fields": ("password1", "password2")}),
    )

    fieldsets = (
        ("Creators Details", {"fields": ("cid", "app_name",  "aid")}),
        ("Identification", {"fields": ("id", "uid", "username", "email", "password"), }),
        ("Bio", {"fields": ("first_name", "last_name", "other_name", "dob", "gender", "mugshot", "about"), }),
        ("Status", {"fields": ("is_active", "is_staff", "is_superuser"), }),
        ("Groups & Permissions", {"fields": ("groups", "user_permissions"), }),
        ("Important Dates", {"fields": ("date_joined", "last_login"), }),
    )

    readonly_fields = ('id', 'uid', 'cid', 'aid', 'password', 'date_joined', 'last_login')
    ordering = ('cid',)
    # radio_fields = {"gender": admin.HORIZONTAL}
    # inlines = [AddressAdmin, ]


admin_site = MyAdminSite(name='admin')
admin_site.register(Group)
admin_site.register(Site)
# admin_site.register(Address)
admin_site.register(User, AppUserAdmin)
admin_site.register(OpenuserCreator, OpenusercreatorAdmin)
