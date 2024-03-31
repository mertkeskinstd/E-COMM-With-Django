# Generated by Django 4.2.7 on 2023-11-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("Baden-Wurttemberg", "Baden-Wurttemberg"),
                    ("Bavaria", "Bavaria"),
                    ("Berlin", "Berlin"),
                    ("Brandenburg", "Brandenburg"),
                    ("Bremen", "Bremen"),
                    ("Hamburg", "Hamburg"),
                    ("Hesse", "Hesse"),
                    ("Lower Saxony", "Lower Saxony"),
                    ("Mecklenburg-Vorpommern", "Mecklenburg-Vorpommern"),
                    ("North Rhine-Westphalia", "North Rhine-Westphalia"),
                    ("Rhineland-Palatinate", "Rhineland-Palatinate"),
                    ("Saarland", "Saarland"),
                    ("Saxony", "Saxony"),
                    ("Saxony-Anhalt", "Saxony-Anhalt"),
                    ("Schleswig-Holstein", "Schleswig-Holstein"),
                    ("Thuringia", "Thuringia"),
                ],
                default="Istanbul",
                max_length=100,
            ),
        ),
    ]
