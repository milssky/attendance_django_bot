# Generated by Django 4.1.6 on 2023-02-03 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=254, verbose_name="Дисциплина")),
                (
                    "lector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Преподаватель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Дисциплина",
                "verbose_name_plural": "Дисциплины",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Group",
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
                    "index",
                    models.CharField(max_length=254, verbose_name="Номер группы"),
                ),
                (
                    "department",
                    models.CharField(max_length=254, verbose_name="Кафедра"),
                ),
            ],
            options={
                "verbose_name": "Группа",
                "verbose_name_plural": "Группы",
                "ordering": ("department",),
            },
        ),
        migrations.CreateModel(
            name="Student",
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
                    "email",
                    models.EmailField(max_length=254, verbose_name="Электронная почта"),
                ),
                ("name", models.CharField(max_length=254, verbose_name="ФИО студента")),
                ("courses", models.ManyToManyField(to="attendance.course")),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="students",
                        to="attendance.group",
                    ),
                ),
            ],
            options={
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Schedule",
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
                    "lecture_datetime",
                    models.DateTimeField(verbose_name="Время проведения пары"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="attendance.course",
                        verbose_name="Курс",
                    ),
                ),
            ],
            options={
                "verbose_name": "Расписание",
                "verbose_name_plural": "Расписания",
                "ordering": ("-course__name",),
            },
        ),
        migrations.CreateModel(
            name="Attendance",
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
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата посещения курса"
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="attendance.course",
                        verbose_name="Дисциплина",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attendances",
                        to="attendance.student",
                        verbose_name="Студент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Посещение",
                "verbose_name_plural": "Посещения",
                "ordering": ("student",),
            },
        ),
    ]
