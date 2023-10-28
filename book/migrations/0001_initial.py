from django.db import migrations,  models
from django.core.management import call_command

def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "PagePerfect_Dataset")


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('average_rating', models.FloatField(blank=True, null=True)),
                ('isbn', models.TextField(blank=True, null=True)),
                ('isbn13', models.BigIntegerField(blank=True, null=True)),
                ('language_code', models.TextField(blank=True, null=True)),
                ('num_pages', models.IntegerField(blank=True, null=True)),
                ('ratings_count', models.IntegerField(blank=True, null=True)),
                ('text_reviews_count', models.IntegerField(blank=True, null=True)),
                ('publication_date', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('harga', models.IntegerField(blank=True, null=True)),
                ('jumlah_buku', models.IntegerField(blank=True, null=True)),
                ('jumlah_terjual', models.IntegerField(blank=True, default=0)),
                ('statusAccept', models.CharField(choices=[('ACCEPT', 'Accept'), ('WAITING', 'Waiting'), ('DENIED', 'Denied'), ('NO STATUS', 'No Status')], default='NO STATUS', max_length=10)),
                ('isInCatalog', models.BooleanField(default=False)),
            ],
        ),
        migrations.RunPython(load_my_initial_data),
    ]
