from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models



class Course(models.Model):
    name = models.CharField(
        verbose_name="Дисциплина",
        max_length=254
    )
    lector = models.ForeignKey(
        User,
        verbose_name="Преподаватель",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    def __str__(self):
        return f"{self.name} - {self.lector}"


class Schedule(models.Model):
    lecture_datetime = models.DateTimeField(
        verbose_name="Время проведения пары"
    )
    course = models.ForeignKey(
        Course,
        verbose_name="Курс",
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('-course__name',)
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Group(models.Model):
    index = models.CharField(
        verbose_name="Номер группы",
        max_length=254
    )
    department = models.CharField(
        verbose_name="Кафедра",
        max_length=254
    )

    class Meta:
        ordering = ("department",)
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.index


class Student(models.Model):
    email = models.EmailField(
        verbose_name="Электронная почта"
    )
    name = models.CharField(
        verbose_name="ФИО студента",
        max_length=254
    )
    courses = models.ManyToManyField(
        Course
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="students"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return f"{self.name} - {self.group.index}"


class Attendance(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="attendances",
        on_delete=models.CASCADE,
        verbose_name="Студент"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата посещения курса"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Дисциплина",
        related_name="attendances"
    )

    class Meta:
        ordering = ("student",)
        verbose_name = "Посещение"
        verbose_name_plural = "Посещения"

    def __str__(self):
        return f"{self.student.name} на {self.course.name} от {self.date:%d.%m.%Y}"
