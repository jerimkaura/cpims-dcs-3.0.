# Generated by Django 4.0.2 on 2022-03-26 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_main', '0002_initial'),
        ('cpovc_registry', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OVCAggregate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator_name', models.CharField(max_length=100)),
                ('project_year', models.IntegerField()),
                ('reporting_period', models.CharField(max_length=50)),
                ('cbo', models.CharField(max_length=255)),
                ('subcounty', models.CharField(max_length=100)),
                ('county', models.CharField(max_length=100)),
                ('ward', models.CharField(max_length=100)),
                ('implementing_partnerid', models.IntegerField()),
                ('implementing_partner', models.CharField(max_length=200)),
                ('indicator_count', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('county_active', models.IntegerField()),
                ('subcounty_active', models.IntegerField()),
                ('ward_active', models.IntegerField()),
                ('created_at', models.DateField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'OVC aggregate data',
                'verbose_name_plural': 'OVC aggregate data',
                'db_table': 'ovc_aggregate',
            },
        ),
        migrations.CreateModel(
            name='OVCCluster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cluster_name', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'OVC Cluster',
                'verbose_name_plural': 'OVC Clusters',
                'db_table': 'ovc_cluster',
            },
        ),
        migrations.CreateModel(
            name='OVCFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_code', models.CharField(max_length=10, null=True)),
                ('facility_name', models.CharField(max_length=200)),
                ('is_void', models.BooleanField(default=False)),
                ('sub_county', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.setupgeography')),
            ],
            options={
                'verbose_name': 'OVC Facility',
                'verbose_name_plural': 'OVC Facilities',
                'db_table': 'ovc_facility',
            },
        ),
        migrations.CreateModel(
            name='OVCUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('implementing_partnerid', models.IntegerField()),
                ('project_year', models.IntegerField()),
                ('reporting_period', models.CharField(max_length=50)),
                ('ovc_filename', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'verbose_name': 'OVC upload data',
                'verbose_name_plural': 'OVC upload data',
                'db_table': 'ovc_upload',
            },
        ),
        migrations.CreateModel(
            name='OVCSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_level', models.CharField(choices=[('SLEC', 'ECD'), ('SLPR', 'Primary'), ('SLSE', 'Secondary'), ('SLUN', 'University'), ('SLTV', 'Tertiary / Vocational')], default='1', max_length=5)),
                ('school_name', models.CharField(max_length=200)),
                ('is_void', models.BooleanField(default=False)),
                ('sub_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_main.setupgeography')),
            ],
            options={
                'verbose_name': 'OVC school',
                'verbose_name_plural': 'OVC Schools',
                'db_table': 'ovc_school',
            },
        ),
        migrations.CreateModel(
            name='OVCRegistration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('registration_date', models.DateField(default=django.utils.timezone.now)),
                ('has_bcert', models.BooleanField(default=False)),
                ('is_disabled', models.BooleanField(default=False)),
                ('hiv_status', models.CharField(max_length=4, null=True)),
                ('school_level', models.CharField(max_length=4, null=True)),
                ('immunization_status', models.CharField(max_length=4, null=True)),
                ('org_unique_id', models.CharField(max_length=15, null=True)),
                ('exit_reason', models.CharField(max_length=4, null=True)),
                ('exit_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_void', models.BooleanField(default=False)),
                ('caretaker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ctaker', to='cpovc_registry.regperson')),
                ('child_cbo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
                ('child_chv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chv', to='cpovc_registry.regperson')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'OVC Registration',
                'verbose_name_plural': 'OVC Registration',
                'db_table': 'ovc_registration',
            },
        ),
        migrations.CreateModel(
            name='OVCHouseHold',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('head_identifier', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('head_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'OVC Registration',
                'verbose_name_plural': 'OVC Registration',
                'db_table': 'ovc_household',
            },
        ),
        migrations.CreateModel(
            name='OVCHHMembers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hh_head', models.BooleanField(default=False)),
                ('member_type', models.CharField(max_length=4)),
                ('member_alive', models.CharField(default='AYES', max_length=4)),
                ('death_cause', models.CharField(max_length=4, null=True)),
                ('hiv_status', models.CharField(max_length=4, null=True)),
                ('date_linked', models.DateField(default=django.utils.timezone.now)),
                ('date_delinked', models.DateField(null=True)),
                ('is_void', models.BooleanField(default=False)),
                ('house_hold', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovchousehold')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'OVC Registration',
                'verbose_name_plural': 'OVC Registration',
                'db_table': 'ovc_household_members',
            },
        ),
        migrations.CreateModel(
            name='OVCHealth',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('art_status', models.CharField(max_length=4)),
                ('date_linked', models.DateField()),
                ('ccc_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovcfacility')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'OVC Care Health',
                'verbose_name_plural': 'OVC Care Health',
                'db_table': 'ovc_care_health',
            },
        ),
        migrations.CreateModel(
            name='OVCEligibility',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('criteria', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
            ],
            options={
                'verbose_name': 'OVC Eligibility',
                'verbose_name_plural': 'OVC Eligibility',
                'db_table': 'ovc_eligibility',
            },
        ),
        migrations.CreateModel(
            name='OVCEducation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_level', models.CharField(max_length=4)),
                ('school_class', models.CharField(max_length=4)),
                ('admission_type', models.CharField(max_length=4)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovcschool')),
            ],
            options={
                'verbose_name': 'OVC Care Education',
                'verbose_name_plural': 'OVC Care Education',
                'db_table': 'ovc_care_education',
            },
        ),
        migrations.CreateModel(
            name='OVCClusterCBO',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_void', models.BooleanField(default=False)),
                ('cbo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regorgunit')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_ovc.ovccluster')),
            ],
            options={
                'verbose_name': 'OVC Cluster CBO',
                'verbose_name_plural': 'OVC Cluster CBOs',
                'db_table': 'ovc_cluster_cbo',
            },
        ),
    ]
