from import_export import resources
from .models import Day, Identifier, BarclaysDaily, BihlDaily, ChoppiesDaily


# ModelResources to describe import and export

class DayResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = Day
        report_skipped = True
        fields = ('date',)
        raise_errors = True
        export_order = ('date', )
        import_id_fields = ['date']


class IdentifierResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = Identifier
        report_skipped = True
        fields = ('name',)
        raise_errors = True
        import_id_fields = ['name']


class BarclaysDailyResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = BarclaysDaily
        report_skipped = True
        fields = ('date', 'identifier', 'price', 'volume', 'low', 'high',)
        raise_errors = True
        import_id_fields = ['date', 'identifier']


class BihlDailyResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = BihlDaily
        report_skipped = True
        fields = ('date', 'identifier', 'price', 'volume', 'low', 'high',)
        raise_errors = True
        import_id_fields = ['date', 'identifier']


class ChoppiesDailyResource(resources.ModelResource):

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = ChoppiesDaily
        report_skipped = True
        fields = ('date', 'identifier', 'price', 'volume', 'low', 'high',)
        raise_errors = True
        import_id_fields = ['date', 'identifier']



