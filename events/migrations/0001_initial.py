# Generated by Django 3.0.4 on 2020-03-08 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=100)),
                ('priority_level', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('te_lead', models.CharField(choices=[('Hailey', 'Hailey'), ('Sean', 'Sean'), ('Keith', 'Keith'), ('Lucy', 'Lucy')], max_length=6)),
                ('number_of_registered', models.IntegerField()),
                ('previous_number_registered', models.IntegerField()),
                ('revenue_goal', models.DecimalField(decimal_places=2, max_digits=8)),
                ('revenue_raised', models.DecimalField(decimal_places=2, max_digits=8)),
                ('webpage', models.URLField()),
                ('sponsor_link_created', models.BooleanField(default=False)),
                ('oc_call_completed', models.BooleanField(default=False)),
                ('prospectus_completed', models.BooleanField(default=False)),
                ('indsutrial_oc_outreach_completed', models.BooleanField(default=False)),
                ('all_previous_sponsors_contacted', models.BooleanField(default=False)),
                ('contacted_industrial_attendees', models.BooleanField(default=False)),
                ('developed_list_with_oc', models.BooleanField(default=False)),
                ('deployed_marketing_email', models.BooleanField(default=False)),
                ('competetive_events_list', models.BooleanField(default=False)),
                ('additional_list_with_te_lead', models.BooleanField(default=False)),
                ('additional_research', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('is_chair', models.BooleanField()),
                ('conference', models.ManyToManyField(to='events.Conference')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('conferences_sponsoring', models.ManyToManyField(blank=True, to='events.Conference')),
                ('organizers', models.ManyToManyField(blank=True, to='events.Organizer')),
            ],
        ),
    ]
