# Generated by Django 4.1.1 on 2022-09-21 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0003_room_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenity",
            options={"verbose_name_plural": "Amenities"},
        ),
    ]
