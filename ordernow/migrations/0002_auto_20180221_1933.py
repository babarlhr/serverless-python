# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-21 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ordernow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='Academic_Level',
            field=models.CharField(choices=[('High School', 'High School'), ('College', 'College'), ('University', ' University'), ('Master', 'Master'), ('PhD', ' PhD')], default='Master', help_text='Academic_Level to', max_length=35),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Have_a_Budget',
            field=models.CharField(blank=True, default=' $ xx', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Number_of_Pages',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Order_Deadline',
            field=models.CharField(blank=True, default='xx/xx/2018', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Paper_Details',
            field=models.TextField(blank=True, max_length=5999, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Phone_Number',
            field=models.CharField(default='+91 9876543210', max_length=20),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Sources',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Subject',
            field=models.CharField(choices=[('Art & Humanities', 'Art & Humanities'), ('Anthropology', ' Anthropology'), ('Archaeology', 'Archaeology'), ('Culture', ' Culture'), ('English', 'English'), ('Ethics', ' Ethics'), ('History and Anthropology', 'History and Anthropology'), ('Linguistics', ' Linguistics'), ('Literature', 'Literature'), ('Music', ' Music'), ('Psychology', 'Psychology'), ('Religion and Theology', ' Religion and Theology'), ('Visual Arts and Film Studies', 'Visual Arts and Film Studies'), ('Gender & Sexual Studies', ' Gender & Sexual Studies'), ('Geography', 'Geography'), ('Human Resources (HR)', ' Human Resources (HR)'), ('International Relations', 'International Relations'), ('Journalism, mass media and communication', ' Journalism, mass media and communicatio'), ('Political Science', 'Political Science'), ('Philosophy', ' Philosophy'), ('Sociology', 'Sociology'), ('Sciences', ' Sciences'), ('Astronomy', 'Astronomy'), ('Biology', ' Biology'), ('Chemistry', ' Chemistry'), ('Earth and Space Sciences', 'Earth and Space Sciences'), ('Mathematics', ' Mathematics'), ('Microbiology', 'Microbiology'), ('Physics', ' Physics'), ('Statistics', 'Statistics'), ('Information Technology', ' Information Technology'), ('Computer Sciences and Information Technology', 'Computer Sciences and Information Technology'), ('Logic and Programming', ' Logic and Programming'), ('Systems Science', 'Systems Science'), ('Applied Sciences', ' Applied Sciences'), ('Agriculture', 'Agriculture'), ('Architecture', ' Architecture'), ('Design and Technology', 'Design and Technology'), ('Education', ' Education'), ('Engineering and Construction', 'Engineering and Construction'), ('Environmental Studies', ' Environmental Studies'), ('Family and Consumer Science', 'Family and Consumer Science'), ('Health Sciences and Medicine', ' Health Sciences and Medicine'), ('Military Sciences', 'Military Sciences'), ('Healthcare and Nursing', ' Healthcare and Nursing'), ('Economics', 'Economics'), ('Business', ' Business'), ('E-commerce', 'E-commerce'), ('Finance and Accounting', ' Finance and Accounting'), ('Logistics', 'Logistics'), ('Macro & Micro Economics', ' Macro & Micro Economics'), ('Management', 'Management'), ('Tourism', ' Tourism'), ('Marketing', 'Marketing'), ('Law and International Law', ' Law and International Law'), ('Law and International Law', 'Law and International Law')], default='English', max_length=45),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='Type_of_Paper',
            field=models.CharField(choices=[('Essay (Any Type)', 'Essay (Any Type)'), ('Research Paper', 'Research Paper'), ('Course Work', ' Course Work'), ('Team Paper', 'Team Paper'), ('Case Study', 'Case Study'), ('Book Review', 'Book Review'), ('Movie Review', 'Movie Review'), ('Annotated Bibliography', ' Annotated Bibliography'), ('Article', 'Article'), ('Assignment', 'Assignment'), ('Dissertation', 'Dissertation'), ('Lab Report', 'Lab Report'), ('Math Problem', ' Math Problem'), ('Speech', 'Speech'), ('Statistics Report', 'Statistics Report')], default='Research Paper', max_length=45),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='spacing',
            field=models.CharField(choices=[('Single_Space', 'Single Space'), ('Double_Space', 'Double Space')], default='Single Space', max_length=15),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='title',
            field=models.CharField(blank=True, default='Write a Title', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]