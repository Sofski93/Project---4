from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_rename_county_location_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_approved',
        ),
        migrations.AlterField(
            model_name='location',
            name='region',
            field=models.CharField(blank=True, choices=[('Connaught', 'Connaught'), ('Leinster', 'Leinster'), ('Munster', 'Munster'), ('Ulster', 'Ulster')], max_length=20),
        ),
    ]