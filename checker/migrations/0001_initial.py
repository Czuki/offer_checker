# Generated by Django 3.2.13 on 2022-07-15 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Czas utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Czas aktualizacji')),
                ('product_url', models.CharField(max_length=512, verbose_name='Link do produktu')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa produktu')),
                ('previous_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Poprzednia cena produktu')),
                ('current_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Aktualna cena produktu')),
                ('price_change_date', models.DateTimeField(blank=True, null=True, verbose_name='Data zmiany ceny')),
                ('product_image_url', models.CharField(blank=True, max_length=512, null=True, verbose_name='Link do zdjęcia produktu')),
            ],
            options={
                'verbose_name': 'Produkt do śledzenia',
                'verbose_name_plural': 'Produkty do śledzenia',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OriginSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Czas utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Czas aktualizacji')),
                ('name', models.CharField(max_length=32, verbose_name='Nazwa')),
                ('main_url', models.CharField(max_length=256, verbose_name='Strona główna')),
            ],
            options={
                'verbose_name': 'Strona główna',
                'verbose_name_plural': 'Strony główne',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PriceChangeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Czas utworzenia')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Czas aktualizacji')),
                ('previous_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Poprzednia cena produktu')),
                ('new_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Nowa cena produktu')),
                ('price_difference', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Różnica w cenie')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checker.checkerproduct', verbose_name='Produkt')),
            ],
            options={
                'verbose_name': 'Historia zmian cen',
                'verbose_name_plural': 'Historia zmian cen',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='checkerproduct',
            name='origin_site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checker.originsite', verbose_name='Strona źródłowa'),
        ),
        migrations.AddField(
            model_name='checkerproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
    ]