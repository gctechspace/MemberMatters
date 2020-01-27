# Generated by Django 2.0 on 2018-10-06 04:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('access', '0001_initial'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('password_reset_key', models.UUIDField(blank=True, default=None, null=True)),
                ('password_reset_expire', models.DateTimeField(blank=True, default=None, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logtype', models.CharField(choices=[('generic', 'Generic log entry'), ('usage', 'Generic usage access'), ('stripe', 'Stripe related event'), ('spacebucks', 'Spacebucks related event'), ('profile', 'Member profile edited'), ('interlock', 'Interlock related event'), ('door', 'Door related event'), ('email', 'Email send event'), ('admin', 'Generic admin event'), ('error', 'Some event that causes an error'), ('xero', 'Generic xero log entry')], max_length=30, verbose_name='Type of action/event')),
                ('description', models.CharField(max_length=500, verbose_name='Description of action/event')),
                ('data', models.TextField(verbose_name='Extra data for debugging action/event')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MemberTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Member Type Name')),
                ('conditions', models.CharField(max_length=100, verbose_name='Membership Conditions')),
                ('cost', models.IntegerField(verbose_name='Monthly Cost')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('screen_name', models.CharField(max_length=30, verbose_name='Screen Name')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '0417123456'. Up to 12 characters allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('state', models.CharField(choices=[('noob', 'New Member'), ('active', 'Active Member'), ('inactive', 'Inactive Member')], default='noob', max_length=8)),
                ('rfid', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='RFID Tag')),
                ('spacebucks_balance', models.FloatField(default=0.0)),
                ('last_spacebucks_purchase', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_seen', models.DateTimeField(blank=True, default=None, null=True)),
                ('last_invoice', models.DateTimeField(blank=True, default=None, null=True)),
                ('stripe_customer_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('stripe_card_expiry', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('stripe_card_last_digits', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('xero_account_id', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('xero_account_number', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('group', models.ManyToManyField(to='group.Group')),
                ('doors', models.ManyToManyField(blank=True, to='access.Doors')),
                ('interlocks', models.ManyToManyField(blank=True, to='access.Interlock')),
                ('member_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='member_type', to='profile.MemberTypes')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profile.Log')),
            ],
            bases=('profile.log',),
        ),
        migrations.CreateModel(
            name='UserEventLog',
            fields=[
                ('log_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profile.Log')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('profile.log',),
        ),
    ]
