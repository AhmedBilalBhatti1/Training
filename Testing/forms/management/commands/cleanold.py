from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from forms.models import MyModel

class Command(BaseCommand):
    help = "Delete records older than given days"

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, default=365)

    def handle(self, *args, **options):
        days = options['days']
        cutoff = timezone.now() - timedelta(days=days)

        old_records = MyModel.objects.filter(created_at__lt=cutoff)
        count = old_records.count()

        if count == 0:
            self.stdout.write(self.style.SUCCESS("No old records found"))
            return

        old_records.delete()

        self.stdout.write(self.style.SUCCESS(f"Deleted {count} records older than {days} days"))