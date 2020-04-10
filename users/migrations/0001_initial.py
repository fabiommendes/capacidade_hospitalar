# Generated by Django 3.0.5 on 2020-04-09 13:29

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0011_update_proxy_permissions"),
        ("locations", "0002_fill_states_and_cities"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(blank=True, null=True, verbose_name="last login"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Informe o e-mail.",
                        max_length=254,
                        unique=True,
                        verbose_name="E-mail",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Informe o nome completo.",
                        max_length=150,
                        verbose_name="Nome completo",
                    ),
                ),
                (
                    "is_verified_notifier",
                    models.BooleanField(
                        default=False,
                        help_text="ATENÇÃO! O usuário terá permissões para notificar alterações de leitos e utilização hospitalar.",
                        verbose_name="Notificador válido?",
                    ),
                ),
                (
                    "is_state_manager",
                    models.BooleanField(
                        default=False,
                        help_text="Marque explicitamente os gestores estaduais.",
                        verbose_name="Gestor estadual?",
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        help_text="Informe o CPF no formato xxx.xxx.xxx-xx.",
                        max_length=14,
                        unique=True,
                        validators=[users.validators.CPFValidator()],
                        verbose_name="CPF",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "state",
                    models.ForeignKey(
                        blank=True,
                        help_text="É necessário informar o estado.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="locations.State",
                        verbose_name="Estado",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "user", "verbose_name_plural": "users", "abstract": False},
            managers=[("objects", django.contrib.auth.models.UserManager())],
        )
    ]