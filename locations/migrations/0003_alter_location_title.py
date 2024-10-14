from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_location_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]