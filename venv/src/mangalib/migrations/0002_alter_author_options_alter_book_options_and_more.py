# Generated by Django 5.0.4 on 2024-05-09 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mangalib", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Auteur", "verbose_name_plural": "Auteurs"},
        ),
        migrations.AlterModelOptions(
            name="book",
            options={
                "permissions": [("apply_promo_code", "Peut appliquer des réductions")],
                "verbose_name": "Livre",
                "verbose_name_plural": "Livres",
            },
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=64, unique=True, verbose_name="Nom"),
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="mangalib.author",
                verbose_name="Auteur",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="quantity",
            field=models.IntegerField(default=1, verbose_name="Quantité"),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=32, unique=True, verbose_name="Titre"),
        ),
    ]
