# Generated by Django 3.0.10 on 2020-09-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0029_profile_stripe_payment_method_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=True),
        ),
    ]
