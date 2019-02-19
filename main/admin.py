from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Database
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from advanced_filters.admin import AdminAdvancedFiltersMixin


class DatabaseAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('pk', 'tm', 'account', 'symbol', 'position')
    list_filter = (('tm', DateTimeRangeFilter), 'account',
                   'symbol', ('position', SliderNumericFilter))
    search_fields = ['account', 'symbol', 'position']

    def account_query(self, obj):
        return obj.account

    account_query.admin_order_field = 'account_query'
    advanced_filter_fields = (
        'tm',
        'account',
        'symbol',

        # even use related fields as lookup fields
        'position',

    )
    pass


admin.site.register(Database, DatabaseAdmin)
# Register your models here.
