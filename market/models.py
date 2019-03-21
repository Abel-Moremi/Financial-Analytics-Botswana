from django.db import models

# Create your models here.


class Day(models.Model):
    date = models.DateField(primary_key=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Day'
        verbose_name_plural = 'Days'
        ordering = ['-date']

    def __str__(self):
        return str(self.date)


class Identifier(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    class Meta:
        verbose_name = 'Identifier'
        verbose_name_plural = 'Identifiers'
        ordering = ['name']

    def __str__(self):
        return self.name


class BarclaysDaily(models.Model):
    date = models.ForeignKey(
        Day, on_delete=models.CASCADE
    )
    identifier = models.ForeignKey(
        Identifier, on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField(default=0)
    volume = models.PositiveIntegerField(default=0)
    low = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    high = models.DecimalField(decimal_places=2, max_digits=6, null=True)

    class Meta:
        verbose_name = 'Barclays Daily'
        verbose_name_plural = 'Barclays Dailies'
        unique_together = (('date', 'identifier'),)
        ordering = ['-date']

    def __str__(self):
        return str(self.date)
