# Generated by Django 3.1.1 on 2020-09-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=255)),
                ('blogAuthor', models.CharField(max_length=122)),
                ('blogContent', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Show',
        ),
    ]