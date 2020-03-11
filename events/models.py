from django.db import models
from django.utils import timezone
from django import forms
from bs4 import BeautifulSoup
import requests
# Create your models here.

class Conference(models.Model):
    title                                           = models.CharField(max_length=100)
    start_date                                      = models.DateField(default=timezone.now)
    end_date                                        = models.DateField(default=timezone.now)
    location                                        = models.CharField(max_length=100)
    PRIORITY_LEVEL_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        )
    priority_level = models.IntegerField(choices=PRIORITY_LEVEL_CHOICES)
    TE_LEAD_CHOICES = (
        ("Hailey", "Hailey"),
        ("Sean", "Sean"),
        ("Keith", "Keith"),
        ("Lucy", "Lucy"),
        )
    te_lead = models.CharField(choices=TE_LEAD_CHOICES, max_length=6)
    prospectus                                      = forms.FileField()
    number_of_registered                            = models.IntegerField()
    previous_number_registered                      = models.IntegerField()
    revenue_goal                                    = models.DecimalField(max_digits=8, decimal_places=2)
    revenue_raised                                  = models.DecimalField(max_digits=8, decimal_places=2)
    webpage                                         = models.URLField()
    # task related fields
    sponsor_link_created                            = models.BooleanField(default=False)
    oc_call_completed                               = models.BooleanField(default=False)
    prospectus_completed                            = models.BooleanField(default=False)
    indsutrial_oc_outreach_completed                = models.BooleanField(default=False)
    all_previous_sponsors_contacted                 = models.BooleanField(default=False)
    #Priority 4
    contacted_industrial_attendees                  = models.BooleanField(default=False)
    developed_list_with_oc                           = models.BooleanField(default=False)
    deployed_marketing_email                        = models.BooleanField(default=False)
    #Priority 3
    competetive_events_list                         = models.BooleanField(default=False)
    #Priority 2
    additional_list_with_te_lead                    = models.BooleanField(default=False)
    #Priority 1
    additional_research                             = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']

    @property
    def speakers(self):
      page = requests.get(self.webpage)
      page_content = BeautifulSoup(page.content, "html.parser")

      TEXT_TO_TRY = ['Keynote Speakers:','Keynote Speakers','Invited Speakers:','Invited Speakers',]
      TAGS_TO_TRY = ['h3', 'h2']

      speaker_list = []
      for key_text in TEXT_TO_TRY:
        for html_tag in TAGS_TO_TRY:
          if str(page_content.find(html_tag, text=key_text)) == ("<{h}>{text}</{h}>".format(h=html_tag, text=key_text)):
            speaker_item = page_content.find(html_tag, text= key_text)
            for nextSibling in speaker_item.findNextSiblings():
              if nextSibling.name == 'ul':
                EXTRACT_EACH_LI_ITEM_INTO_LIST = None
                lis = nextSibling.find_all("li")
                lis_text = [i.text for i in lis]

              if nextSibling.name != 'ul':
                  break

            return(lis_text)



class Person(models.Model):
    name                                            = models.CharField(max_length=100)
    conference                                      = models.ManyToManyField('Conference')
    email                                           = models.EmailField()
    is_chair                                        = models.BooleanField()
    is_on_oc                                        = models.BooleanField()

    def __str__(self):
        return self.name



class Company(models.Model):
    name                                           = models.CharField(max_length=100)
    people                                         = models.ManyToManyField('Person', blank = True)
    conferences_sponsoring                         = models.ManyToManyField('Conference', blank = True)
    #conferences_interested_in_sponsoring           = models.ManyToManyField('Conference', blank = True)
    #contacted_regarding_event                      = models.BooleanField()
    #delete above
    #can get events sponsored through querysets

    def __str__(self):
        return self.name
