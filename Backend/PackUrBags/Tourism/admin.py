from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Tourism.models import (
    UserData, Booking, Monument, City, GuideData,
    MonumentInfo, Payment, UserHistory, )
from Tourism.forms import UserDataCreationForm, UserDataChangeForm


class AccountAdmin(UserAdmin):
    add_form = UserDataCreationForm
    form = UserDataChangeForm
    fieldsets = (
        (None, {'fields': ('password', 'email', 'username', 'first_name', 'last_name', 'phone_number', 'profile_pic', 'dob', )}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'phone_number', 'dob', 'password1', 'password2',)}
         ),
    )
    list_display = ('email', 'username', 'is_admin', 'is_staff',)
    search_fields = ('email', 'username',)
    filter_horizontal = ()
    list_filter = ()


admin.site.register(UserData, AccountAdmin)
admin.site.register(Booking)
admin.site.register(Monument)
admin.site.register(City)
admin.site.register(GuideData)
admin.site.register(MonumentInfo)
admin.site.register(Payment)
admin.site.register(UserHistory)
