# Generated by Django 3.0.6 on 2020-06-04 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_number', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(choices=[('MSK', 'Mask'), ('GWN', 'Gown'), ('GOG', 'Goggle'), ('CPS', 'Cap')], default='MSK', max_length=3)),
                ('qty_per_package', models.IntegerField()),
                ('condition_upon_received', models.CharField(choices=[('GOOD', 'Good'), ('BAD', 'Bad')], default='GOOD', max_length=6)),
                ('supplier', models.CharField(choices=[('LG', 'Local Government Unit'), ('DN', 'Donation')], default='LG', max_length=2)),
                ('received_by', models.CharField(max_length=200)),
                ('checked_by', models.CharField(max_length=200)),
                ('date_of_receipt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Used',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_being_used', models.DateField()),
                ('qty_to_be_used', models.IntegerField()),
                ('is_used', models.BooleanField(default=True)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Disposed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_disposed', models.DateField(auto_now_add=True)),
                ('qty_to_be_disposed', models.IntegerField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.Equipment')),
                ('used', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='stocks.Used')),
            ],
        ),
    ]
