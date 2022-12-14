# Generated by Django 4.1.1 on 2022-10-11 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmstu_lab', '0008_alter_case_end_date_alter_case_ward_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='photo',
            field=models.FileField(default='1.jpg', upload_to='static/photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='case',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='cases', to='bmstu_lab.patient'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='doctors', to='bmstu_lab.speciality'),
        ),
    ]
