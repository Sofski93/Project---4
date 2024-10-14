from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_auto_20220725_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='excerpt',
        ),
    ]