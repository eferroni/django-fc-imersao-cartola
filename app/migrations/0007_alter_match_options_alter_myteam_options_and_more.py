# Generated by Django 4.1.3 on 2022-12-03 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_match_match_date_alter_match_team_a_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='match',
            options={'verbose_name': 'Jogo', 'verbose_name_plural': 'Jogos'},
        ),
        migrations.AlterModelOptions(
            name='myteam',
            options={'verbose_name': 'Meu Time', 'verbose_name_plural': 'Meus Times'},
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Jogador', 'verbose_name_plural': 'Jogadores'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Time', 'verbose_name_plural': 'Times'},
        ),
    ]
