from django.contrib import admin
from company.models import (
    Category,
    Company,
    Facility,
    Benefit,
    CompanyBenefit
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )


class BenefitInline(admin.TabularInline):
    model = CompanyBenefit
    extra = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    search_fields = ('name', 'website')
    inlines = (BenefitInline,)
