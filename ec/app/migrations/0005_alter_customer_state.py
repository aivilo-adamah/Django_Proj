# Generated by Django 4.1.4 on 2023-02-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_rename_user_customer_user_alter_customer_mobile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("Accra", "GHANA"),
                    ("Lagos", "NIGERIA"),
                    ("Johannesburg", "AFRIQUE DU SUD"),
                    ("Niamey", "NIGER"),
                    ("Nairobi", "KENYA"),
                    ("Rabat", "MAROC"),
                    ("Alger", "ALGÉRIE"),
                    ("Caire", "EGYPTE"),
                ],
                max_length=100,
            ),
        ),
    ]
