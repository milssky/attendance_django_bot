import csv

from django.core.management.base import BaseCommand


from attendance.models import Course, Group, Student, User


class Command(BaseCommand):
    help = "Add students emails to DB"

    def handle(self, *args, **options):
        with open(options["emails"], encoding="utf8") as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                name, surname, _n, group_index, _m, department, email, username = row
                if ("отчислен" in group_index) or ("филиал" in group_index): continue
                group, _ = Group.objects.get_or_create(
                    index=group_index,
                    department=department
                )
                course, _ = Course.objects.get_or_create(
                    name=options["course"],
                    lector=User.objects.get(pk=int(options["lector"]))
                )
                student, _ = Student.objects.get_or_create(
                    email=email,
                    name=f"{surname} {name}",
                    group=group
                )
                student.courses.add(course)

    def add_arguments(self, parser):
        parser.add_argument(
            "-e",
            "--emails",
            action="store",
            help="Path to email .csv file",
            required=True
        )
        parser.add_argument(
            "-c",
            "--course",
            action="store",
            help="Course name",
            required=True
        )
        parser.add_argument(
            "-l",
            "--lector",
            action="store",
            help="Course lector",
            required=True
        )