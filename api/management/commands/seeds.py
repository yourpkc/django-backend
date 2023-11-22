from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from config import env


class Command(BaseCommand):
    help = 'Seeds were required to initial apps.'

    def create_super_user(self):
        username = env('SUPERUSER_USERNAME', default='admin')
        email = env('SUPERUSER_EMAIL', default='admin@example.com')
        password = env('SUPERUSER_PASSWORD', default='adminpass')
        first_name = env('SUPERUSER_FIRST_NAME', default='admin-first-name')
        last_name = env('SUPERUSER_LAST_NAME', default='admin-last-name')

        superuser = User.objects.filter(username=username,
                                        is_superuser=True).last()
        if not superuser:
            User.objects.create_superuser(username=username,
                                          email=email,
                                          password=password,
                                          first_name=first_name,
                                          last_name=last_name,)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            superuser.username = username
            superuser.email = email
            superuser.set_password(password)
            superuser.first_name = first_name
            superuser.last_name = last_name
            superuser.save()
            self.stdout.write(self.style.SUCCESS('Superuser updated successfully'))

    def handle(self, *args, **options):
        self.create_super_user()
        self.stdout.write(self.style.SUCCESS('Command executed successfully'))