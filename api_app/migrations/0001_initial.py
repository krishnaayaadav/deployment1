
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
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('expense_date', models.DateField(auto_now_add=True)),
                ('expense_amount', models.FloatField()),
                ('expense_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
