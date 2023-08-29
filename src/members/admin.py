from django.contrib import admin
from .models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "joinded_date",
    )
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering = ("joinded_date",)


admin.site.register(Member, MemberAdmin)
