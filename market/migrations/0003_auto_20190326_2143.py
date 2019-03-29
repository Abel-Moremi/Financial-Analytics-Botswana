# Generated by Django 2.1.7 on 2019-03-26 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auto_20190326_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='BihlDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0)),
                ('volume', models.PositiveIntegerField(default=0)),
                ('low', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('high', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Day')),
                ('identifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Identifier')),
            ],
            options={
                'verbose_name': 'Barclays Daily',
                'verbose_name_plural': 'Barclays Dailies',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='bihldaily',
            unique_together={('date', 'identifier')},
        ),
    ]