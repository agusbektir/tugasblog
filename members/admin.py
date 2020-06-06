from django.contrib import admin
from members.models import Member

class MemberAdminPage(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Member, MemberAdminPage)