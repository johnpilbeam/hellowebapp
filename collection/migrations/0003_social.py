# Generated by Django 2.0.4 on 2018-07-24 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_thing_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('twitter', 'Twitter'), ('facebook', 'Facebook'), ('pinterest', 'Pinterest'), ('instagram', 'Instagram')], max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('thing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to='collection.Thing')),
            ],
        ),
    ]