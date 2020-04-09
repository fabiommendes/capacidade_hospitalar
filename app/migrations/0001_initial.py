# Generated by Django 3.0.5 on 2020-04-09 13:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("locations", "0003_auto_20200409_1329"),
    ]

    operations = [
        migrations.CreateModel(
            name="HealthcareUnity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "cnes_id",
                    models.CharField(
                        max_length=15,
                        validators=[django.core.validators.RegexValidator("[0-9]+")],
                        verbose_name="Registro CNES",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Unidade está ativa?"),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Nome do estabelecimento de saúde",
                        max_length=100,
                        verbose_name="Estabelecimento",
                    ),
                ),
                (
                    "municipality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="healthcare_unities",
                        to="locations.Municipality",
                        verbose_name="Município",
                    ),
                ),
                (
                    "notifiers",
                    models.ManyToManyField(related_name="unities", to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Estabelecimento de Saúde",
                "verbose_name_plural": "Estabelecimentos de Saúde",
            },
        ),
        migrations.CreateModel(
            name="LogEntry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        help_text="De quando é este dado?",
                        verbose_name="Data",
                    ),
                ),
                (
                    "sari_cases_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Informe total de pacientes SRAG", verbose_name="Adulto"
                    ),
                ),
                (
                    "covid_cases_adults",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Destes casos, quantos foram confirmados como COVID?",
                        verbose_name="Casos COVID confirmados",
                    ),
                ),
                (
                    "sari_cases_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Informe total de pacientes SRAG", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "covid_cases_pediatric",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Destes casos, quantos foram confirmados como COVID?",
                        verbose_name="Casos COVID confirmados",
                    ),
                ),
                (
                    "icu_sari_cases_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Informe total de pacientes SRAG", verbose_name="Adulto"
                    ),
                ),
                (
                    "icu_covid_cases_adults",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Destes casos, quantos foram confirmados como COVID?",
                        verbose_name="Casos COVID confirmados",
                    ),
                ),
                (
                    "icu_sari_cases_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Informe total de pacientes para SRAG", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "icu_covid_cases_pediatric",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        help_text="Destes casos, quantos foram confirmados como COVID?",
                        verbose_name="Casos COVID confirmados",
                    ),
                ),
                (
                    "regular_cases_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Informe o total de pacientes.", verbose_name="Adulto"
                    ),
                ),
                (
                    "regular_cases_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Informe o total de pacientes.", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "regular_icu_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Informe o total de pacientes.", verbose_name="Adulto"
                    ),
                ),
                (
                    "regular_icu_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Informe o total de pacientes.", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "notifier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="daily_notifications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário notificador",
                    ),
                ),
                (
                    "unity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.HealthcareUnity"
                    ),
                ),
            ],
            options={"verbose_name": "Informe diário", "verbose_name_plural": "Informes diários"},
        ),
        migrations.CreateModel(
            name="Capacity",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=django.utils.timezone.now,
                        help_text="Quando ocorreu a alteração na capacidade hospitalar?",
                        verbose_name="Data",
                    ),
                ),
                (
                    "beds_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Quantos leitos deste tipo você tem?", verbose_name="Adulto"
                    ),
                ),
                (
                    "beds_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Quantos leitos deste tipo você tem?", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "icu_adults",
                    models.PositiveSmallIntegerField(
                        help_text="Quantos leitos deste tipo você tem?", verbose_name="Adulto"
                    ),
                ),
                (
                    "icu_pediatric",
                    models.PositiveSmallIntegerField(
                        help_text="Quantos leitos deste tipo você tem?", verbose_name="Pediátrico"
                    ),
                ),
                (
                    "notifier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="capacity_notifications",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário notificador",
                    ),
                ),
                (
                    "unity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="capacity_notifications",
                        to="app.HealthcareUnity",
                        verbose_name="Unidade de saúde",
                    ),
                ),
            ],
            options={
                "verbose_name": "Alteração na capacidade",
                "verbose_name_plural": "Alterações de capacidade hospitalar",
            },
        ),
    ]
