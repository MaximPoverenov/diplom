# Generated by Django 4.2 on 2024-11-20 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Table",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "number",
                    models.CharField(max_length=10, verbose_name="Номер столика"),
                ),
                (
                    "seats",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Количество мест"
                    ),
                ),
            ],
            options={
                "verbose_name": "Столик",
                "verbose_name_plural": "Столики",
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="Дата бронирования")),
                ("time", models.TimeField(verbose_name="Время бронирования")),
                ("guests", models.IntegerField(verbose_name="Количество гостей")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "В ожидании"),
                            ("confirmed", "Подтверждено"),
                            ("canceled", "Отменено"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "duration_hours",
                    models.IntegerField(
                        default=1, verbose_name="Продолжительность брони в часах"
                    ),
                ),
                (
                    "table",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="booking_app.table",
                        verbose_name="Стол",
                    ),
                ),
            ],
        ),
    ]