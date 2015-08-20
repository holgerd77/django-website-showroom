# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website_showroom.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Only used in admin context, not displayed on site (edition specific category names)', max_length=40)),
                ('color', models.CharField(help_text=b'Format: #ffffff', max_length=7)),
                ('active_color', models.CharField(help_text=b'Format: #ffffff', max_length=7)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(help_text=b'Main title shown on page', max_length=40)),
                ('country', models.CharField(help_text=b"2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site.", max_length=2)),
                ('order', models.IntegerField(help_text=b'Numeric value for edition order. Tip: Use 100-200-300-... steps for easy reordering. Edition first in order will be used as edition default.')),
                ('short_description', models.CharField(help_text=b"Something like 'English version', used for mouseover on flag", max_length=40)),
                ('html_title', models.CharField(help_text=b'Used for html title tag', max_length=100)),
                ('site_subtitle', models.CharField(help_text=b'Subtitle (HTML tags possible)', max_length=125)),
                ('rss_title', models.CharField(help_text=b'Title for rss feed', max_length=100)),
                ('rss_description', models.CharField(help_text=b'Description for rss feed', max_length=200)),
                ('facebook_url', models.CharField(help_text=b'Optional, link to Facebook page', max_length=90, null=True, blank=True)),
                ('twitter_url', models.CharField(help_text=b'Optional, link to Twitter page', max_length=90, null=True, blank=True)),
                ('google_plus_url', models.CharField(help_text=b'Optional, link to Google+ page', max_length=90, null=True, blank=True)),
                ('home_menu_title', models.CharField(help_text=b"Something like - e.g. - 'Home'", max_length=40)),
                ('home_menu_color', models.CharField(help_text=b"HTML color code, e.g. '#003300", max_length=7)),
                ('home_menu_active_color', models.CharField(help_text=b"HTML color code, e.g. '#006600", max_length=7)),
                ('home_num_websites', models.IntegerField(help_text=b'Number of websites for home category')),
                ('footer_left', models.CharField(help_text=b'Left footer (HTML tags possible)', max_length=200)),
                ('footer_right', models.CharField(help_text=b'Right footer (HTML tags possible)', max_length=200)),
                ('contact_title', models.CharField(help_text=b'Title of contact navi', max_length=40)),
                ('contact_html', models.TextField()),
                ('comments', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EditionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Edition specific category name', max_length=40)),
                ('url_name', models.SlugField(help_text=b"Every url-conform string except 'contact'", max_length=40)),
                ('order', models.IntegerField(help_text=b'Numeric value for category order. Tip: Use 100-200-300-... steps for easy reordering.')),
                ('category', models.ForeignKey(to='website_showroom.Category')),
                ('edition', models.ForeignKey(to='website_showroom.Edition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EditionWebsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Edition specific title, if left empty, generic title is used', max_length=50, null=True, blank=True)),
                ('desc', models.TextField(help_text=b'Edition specific description')),
                ('order', models.IntegerField(help_text=b'Numeric value for website order. Tip: Use 100-200-300-... steps for easy reordering.')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('edition', models.ForeignKey(to='website_showroom.Edition')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Generic title, used if no extra edition specific title is provided', max_length=50)),
                ('country', models.CharField(help_text=b"Optional, 2-letter-country-code for showing a corresponding flag (e.g. 'de', 'en'). Careful, not existing code will break site.", max_length=2, null=True, blank=True)),
                ('screenshot', models.ImageField(help_text=b'Image file, size: 300x200, name will be unified. Larger file image will be resized. Greater height will be cropped (making screen capture with website width and height generously higher than aspect ratio is easiest)', upload_to=website_showroom.models.get_path)),
                ('url', models.CharField(max_length=90)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('category', models.ForeignKey(to='website_showroom.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='editionwebsite',
            name='website',
            field=models.ForeignKey(to='website_showroom.Website'),
            preserve_default=True,
        ),
    ]
