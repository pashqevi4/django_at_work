from django.core.management.base import BaseCommand
from tst_02_app.models import User


class Command(BaseCommand):
    help = 'Get all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        self.stdout.write(f'{users}')

