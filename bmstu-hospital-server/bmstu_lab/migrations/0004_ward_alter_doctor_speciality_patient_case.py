# Generated by Django 4.1.1 on 2022-10-10 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bmstu_lab', '0003_doctor_first_name_doctor_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='bmstu_lab.speciality'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('patronymic', models.CharField(max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bmstu_lab.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='bmstu_lab.patient')),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bmstu_lab.ward')),
            ],
        ),
    ]
