# Generated by Django 2.2.3 on 2019-07-26 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pariListe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePari', models.CharField(max_length=120)),
                ('montantMin', models.CharField(max_length=200)),
                ('montantMax', models.CharField(max_length=200)),
                ('pourcentage', models.CharField(max_length=200)),
                ('dateDebut', models.CharField(max_length=200)),
                ('dateFin', models.CharField(max_length=200)),
                ('nbreEquipeMin', models.CharField(max_length=200)),
                ('nbreEquipeMax', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('surname', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('nbr_joueur', models.EmailField(max_length=100)),
                ('password', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='userPari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePari', models.CharField(max_length=120)),
                ('nameUser', models.CharField(max_length=200)),
                ('montantParier', models.CharField(max_length=200)),
                ('idPari', models.CharField(max_length=200)),
            ],
        ),
    ]
