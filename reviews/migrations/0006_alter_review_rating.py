# Generated by Django 4.1.1 on 2022-09-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0005_alter_review_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
