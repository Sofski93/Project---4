from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_location_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='county',
            new_name='region',
        ),
    ]