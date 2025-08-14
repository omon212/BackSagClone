import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        base_dir = settings.BASE_DIR

        db_path = os.path.join(base_dir, "db.sqlite3")
        if os.path.exists(db_path):
            os.remove(db_path)
            self.stdout.write(self.style.SUCCESS(f"✅ Database deleted: {db_path}"))
        else:
            self.stdout.write(self.style.WARNING("⚠ Database file not found"))

        for root, dirs, files in os.walk(base_dir):
            if "migrations" in dirs:
                migration_path = os.path.join(root, "migrations")
                for file in os.listdir(migration_path):
                    if file != "__init__.py" and file.endswith(".py"):
                        os.remove(os.path.join(migration_path, file))
                for file in os.listdir(migration_path):
                    if file.endswith(".pyc"):
                        os.remove(os.path.join(migration_path, file))
        self.stdout.write(self.style.SUCCESS("✅ Migrations cleared"))

        uploads_path = os.path.join(base_dir, "uploads")
        if os.path.exists(uploads_path):
            shutil.rmtree(uploads_path)
            self.stdout.write(self.style.SUCCESS(f"✅ Uploads folder deleted: {uploads_path}"))
        else:
            self.stdout.write(self.style.WARNING("⚠ Uploads folder not found"))

        self.stdout.write(self.style.SUCCESS("🎯 Project reset completed!"))
