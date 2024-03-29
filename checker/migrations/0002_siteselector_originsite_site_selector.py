# Generated by Django 4.0.3 on 2023-02-23 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSelector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Czas utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Czas aktualizacji')),
                ('price_selector_xpath', models.TextField()),
                ('image_selector_xpath', models.TextField()),
                ('price_selector_css', models.TextField()),
                ('image_selector_css', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='originsite',
            name='site_selector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='checker.siteselector', verbose_name='Selektory strony'),
        ),
    ]
