
# Generated by Django 4.2 on 2023-05-21 20:26


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turma', '0002_remove_presenca_aluno_remove_presenca_aula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turma.turma')),
            ],
        ),
    ]
