# Generated by Django 4.2.7 on 2023-11-29 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50)),
                ('is_tail', models.BooleanField(default=False)),
                ('head', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='kanban.column')),
                ('kanban', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kanban_columns', to='kanban.kanban')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
