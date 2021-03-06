from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from core import models

class UserAdmin(BaseUserAdmin):
	ordering = ['id']
	list_display = ['email', 'name']
	fieldsets = (
		(None, {'fields': ('password','email')}),
		(_('Personal info'), {'fields': ('name',)}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
										'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login',)}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2', 'name')
		}),
	)


admin.site.register(models.User, UserAdmin)
