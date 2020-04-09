# Generated by Django 3.0.5 on 2020-04-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200408_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'verbose_name': 'Informe diário', 'verbose_name_plural': 'Informes diários'},
        ),
        migrations.AlterField(
            model_name='logentry',
            name='covid_cases_adults',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Destes casos, quantos foram confirmados como COVID?', verbose_name='Casos COVID confirmados'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='covid_cases_pediatric',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Destes casos, quantos foram confirmados como COVID?', verbose_name='Casos COVID confirmados'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='icu_covid_cases_adults',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Destes casos, quantos foram confirmados como COVID?', verbose_name='Casos COVID confirmados'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='icu_covid_cases_pediatric',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Destes casos, quantos foram confirmados como COVID?', verbose_name='Casos COVID confirmados'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='icu_sari_beds_adults',
            field=models.PositiveSmallIntegerField(help_text='Informe total de pacientes SRAG', verbose_name='Adulto'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='icu_sari_beds_pediatric',
            field=models.PositiveSmallIntegerField(help_text='Informe total de pacientes para SRAG', verbose_name='Pediátrico'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='regular_beds_adults',
            field=models.PositiveSmallIntegerField(help_text='Informe o total de pacientes.', verbose_name='Adulto'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='regular_beds_pediatric',
            field=models.PositiveSmallIntegerField(help_text='Informe o total de pacientes.', verbose_name='Pediátrico'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='regular_icu_adults',
            field=models.PositiveSmallIntegerField(help_text='Informe o total de pacientes.', verbose_name='Adulto'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='regular_icu_pediatric',
            field=models.PositiveSmallIntegerField(help_text='Informe o total de pacientes.', verbose_name='Pediátrico'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='sari_beds_adults',
            field=models.PositiveSmallIntegerField(help_text='Informe total de pacientes SRAG', verbose_name='Adulto'),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='sari_beds_pediatric',
            field=models.PositiveSmallIntegerField(help_text='Informe total de pacientes SRAG', verbose_name='Pediátrico'),
        ),
    ]