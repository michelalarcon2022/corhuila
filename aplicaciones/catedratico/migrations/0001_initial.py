# Generated by Django 4.2 on 2023-04-28 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("geografico", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PerfilCatedratico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("state", models.BooleanField(default=True, verbose_name="Estado")),
                (
                    "created_date",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "modified_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Modificación"
                    ),
                ),
                (
                    "deleted_date",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Eliminación"
                    ),
                ),
                ("avatar", models.ImageField(upload_to="cate/avatar/%Y/%m/%d/")),
                (
                    "cv_pdf",
                    models.FileField(max_length=1000, upload_to="cate/cv/%Y/%m/%d/"),
                ),
                (
                    "tipo_documento",
                    models.CharField(
                        choices=[(1, "DPI"), (2, "Certificado")],
                        max_length=1,
                        verbose_name="Tipo Documento",
                    ),
                ),
                ("numero_documento", models.CharField(max_length=30)),
                ("nombre", models.CharField(max_length=100, verbose_name="Nombre")),
                ("apellido", models.CharField(max_length=50, verbose_name="Apellido")),
                ("f_nacimiento", models.DateField(verbose_name="Fecha de Nacimiento")),
                ("ciu_nacimiento", models.CharField(max_length=100)),
                (
                    "genero",
                    models.CharField(
                        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
                        max_length=1,
                        verbose_name="Genero",
                    ),
                ),
                (
                    "e_civil",
                    models.CharField(
                        choices=[
                            (1, "SOLTERO (A)"),
                            (2, "CASADO (A)"),
                            (3, "UNIÓN LIBRE"),
                        ],
                        max_length=1,
                        verbose_name="Estado Civil",
                    ),
                ),
                (
                    "direccion",
                    models.CharField(max_length=150, verbose_name="Dirección"),
                ),
                (
                    "zona",
                    models.CharField(max_length=5, verbose_name="Zona de Residencia"),
                ),
                ("titulo_obtenido", models.CharField(max_length=100)),
                (
                    "telefono_1",
                    models.CharField(max_length=12, verbose_name="Telefono 1"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "tel_contacto",
                    models.CharField(max_length=12, verbose_name="Telefono Contacto"),
                ),
                (
                    "discapacidad",
                    models.CharField(max_length=250, verbose_name="Discapacidad"),
                ),
                ("notas", models.TextField()),
                (
                    "ciudad",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Ciudad",
                        to="geografico.ciudad",
                    ),
                ),
                (
                    "conocimiento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geografico.conocimiento",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_creation",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "departamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="departamento",
                        to="geografico.departamento",
                    ),
                ),
                (
                    "formacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geografico.formacion",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pais",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pais",
                        to="geografico.pais",
                    ),
                ),
            ],
            options={
                "verbose_name": "PerfilCatedratico",
                "verbose_name_plural": "PerfilCatedraticos",
            },
        ),
    ]
