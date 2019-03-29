from django.contrib import admin
from .models import Day, Identifier, BarclaysDaily, BihlDaily, ChoppiesDaily
from import_export.admin import ImportExportActionModelAdmin
from market.resource import DayResource, IdentifierResource, BarclaysDailyResource, BihlDailyResource, ChoppiesDailyResource
from .forms import DayAdminForm

# Register your models here.


@admin.register(Day)
class DayAdmin(ImportExportActionModelAdmin):
    form = DayAdminForm
    resource_class = DayResource
    search_fields = ('date',)

    actions = ['really_delete_selected']

    def date_display(self, obj):
        return obj.datefield.strftime('%d-%b-%y')

    def get_actions(self, request):
        actions = super(DayAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()

        if queryset.count() == 1:
            message_bit = "1 Date entry was"
        else:
            message_bit = "%s Date entries were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)

    really_delete_selected.short_description = "Delete selected Days"
    date_display.admin_order_field = 'date'
    date_display.short_description = 'date'

    list_display = ('date',)


@admin.register(Identifier)
class IdentifierAdmin(ImportExportActionModelAdmin):
    resource_class = IdentifierResource
    search_fields = ('name',)
    list_display = ('name', )


@admin.register(BarclaysDaily)
class BarclaysDailyAdmin(ImportExportActionModelAdmin):
    resource_class = BarclaysDailyResource

    def date_display(self, obj):
        return obj.datefield.strftime('%d-%b-%y')

    date_display.admin_order_field = 'date'
    date_display.short_description = 'date'

    list_display = ('date', 'price', 'volume', 'low', 'high')


@admin.register(BihlDaily)
class BihlDailyAdmin(ImportExportActionModelAdmin):
    resource_class = BihlDailyResource

    def date_display(self, obj):
        return obj.datefield.strftime('%d-%b-%y')

    date_display.admin_order_field = 'date'
    date_display.short_description = 'date'

    list_display = ('date', 'price', 'volume', 'low', 'high')


@admin.register(ChoppiesDaily)
class ChoppiesDailyAdmin(ImportExportActionModelAdmin):
    resource_class = ChoppiesDailyResource

    def date_display(self, obj):
        return obj.datefield.strftime('%d-%b-%y')

    date_display.admin_order_field = 'date'
    date_display.short_description = 'date'

    list_display = ('date', 'price', 'volume', 'low', 'high')
