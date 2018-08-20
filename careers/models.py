from django.db import models
from django.utils.translation import ugettext as _
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.core.mail import send_mail
# Create your models here.
COUNTRY = (
    ('Andorra', _('Andorra')),
    ('United Arab Emirates', _('United Arab Emirates')),
    ('Afghanistan', _('Afghanistan')),
    ('Antigua & Barbuda', _('Antigua & Barbuda')),
    ('Albania', _('Albania')),
    ('Armenia', _('Armenia')),
    ('Netherlands', _('Netherlands Antilles')),
    ('Angola', _('Angola')),
    ('Antarctica', _('Antarctica')),
    ('Argentina', _('Argentina')),
    ('American', _('American Samoa')),
    ('Austria', _('Austria')),
    ('Australia', _('Australia')),
    ('Aruba', _('Aruba')),
    ('Azerbaijan', _('Azerbaijan')),
    ('Bosnia', _('Bosnia and Herzegovina')),
    ('Barbados', _('Barbados')),
    ('Bangladesh', _('Bangladesh')),
    ('Belgium', _('Belgium')),
    ('Burkina', _('Burkina Faso')),
    ('Bulgaria', _('Bulgaria')),
    ('Bahrain', _('Bahrain')),
    ('Burundi', _('Burundi')),
    ('Benin', _('Benin')),
    ('Bermuda', _('Bermuda')),
    ('Brunei', _('Brunei Darussalam')),
    ('Bolivia', _('Bolivia')),
    ('Brazil', _('Brazil')),
    ('Bahama', _('Bahama')),
    ('Bhutan', _('Bhutan')),
    ('Bouvet', _('Bouvet Island')),
    ('Botswana', _('Botswana')),
    ('Belarus', _('Belarus')),
    ('Belize', _('Belize')),
    ('Canada', _('Canada')),
    ('Cocos', _('Cocos (Keeling) Islands')),
    ('Central', _('Central African Republic')),
    ('Congo', _('Congo')),
    ('Switzerland', _('Switzerland')),
    ('Ivory', _('Ivory Coast')),
    ('Cook Iislands', _('Cook Iislands')),
    ('Chile', _('Chile')),
    ('Cameroon', _('Cameroon')),
    ('China', _('China')),
    ('Colombia', _('Colombia')),
    ('Costa Rica', _('Costa Rica')),
    ('Cuba', _('Cuba')),
    ('Cape Verde', _('Cape Verde')),
    ('Christmas', _('Christmas Island')),
    ('Cyprus', _('Cyprus')),
    ('Czech Republic', _('Czech Republic')),
    ('Germany', _('Germany')),
    ('Djibouti', _('Djibouti')),
    ('Denmark', _('Denmark')),
    ('Dominica', _('Dominica')),
    ('Dominican', _('Dominican Republic')),
    ('Algeria', _('Algeria')),
    ('Ecuador', _('Ecuador')),
    ('Estonia', _('Estonia')),
    ('Egypt', _('Egypt')),
    ('Western Sahara', _('Western Sahara')),
    ('Eritrea', _('Eritrea')),
    ('Spain', _('Spain')),
    ('Ethiopia', _('Ethiopia')),
    ('Finland', _('Finland')),
    ('Fiji', _('Fiji')),
    ('Falkland', _('Falkland Islands (Malvinas)')),
    ('Micronesia', _('Micronesia')),
    ('Faroe Islands', _('Faroe Islands')),
    ('France', _('France')),
    ('France, Metropolitan', _('France, Metropolitan')),
    ('Gabon', _('Gabon')),
    ('United Kingdom (Great Britain)', _('United Kingdom (Great Britain)')),
    ('Grenada', _('Grenada')),
    ('Georgia', _('Georgia')),
    ('French', _('French Guiana')),
    ('Ghana', _('Ghana')),
    ('Gibraltar', _('Gibraltar')),
    ('Greenland', _('Greenland')),
    ('Gambia', _('Gambia')),
    ('Guinea', _('Guinea')),
    ('Guadeloupe', _('Guadeloupe')),
    ('Equatorial', _('Equatorial Guinea')),
    ('Greece', _('Greece')),
    ('South Georgia and the South Sandwich Islands', _('South Georgia and the South Sandwich Islands')),
    ('Guatemala', _('Guatemala')),
    ('Guam', _('Guam')),
    ('Guinea-Bissau', _('Guinea-Bissau')),
    ('Guyana', _('Guyana')),
    ('Hong Kong', _('Hong Kong')),
    ('Heard & McDonald Islands', _('Heard & McDonald Islands')),
    ('Honduras', _('Honduras')),
    ('Croatia', _('Croatia')),
    ('Haiti', _('Haiti')),
    ('Hungary', _('Hungary')),
    ('Indonesia', _('Indonesia')),
    ('Ireland', _('Ireland')),
    ('Israel', _('Israel')),
    ('India', _('India')),
    ('British Indian Ocean Territory', _('British Indian Ocean Territory')),
    ('Iraq', _('Iraq')),
    ('Islamic Republic of Iran', _('Islamic Republic of Iran')),
    ('Iceland', _('Iceland')),
    ('Italy', _('Italy')),
    ('Jamaica', _('Jamaica')),
    ('Jordan', _('Jordan')),
    ('Japan', _('Japan')),
    ('Kenya', _('Kenya')),
    ('Kyrgyzstan', _('Kyrgyzstan')),
    ('Cambodia', _('Cambodia')),
    ('Kiribati', _('Kiribati')),
    ('Comoros', _('Comoros')),
    ('St. Kitts and Nevis', _('St. Kitts and Nevis')),
    ('Korea', _('Korea, Democratic People\'s Republic of')),
    ('KR', _('Korea, Republic of')),
    ('Kuwait', _('Kuwait')),
    ('Cayman Islands', _('Cayman Islands')),
    ('Kazakhstan', _('Kazakhstan')),
    ('Lao People', _('Lao People\'s Democratic Republic')),
    ('Lebanon', _('Lebanon')),
    ('Saint Lucia', _('Saint Lucia')),
    ('Liechtenstein', _('Liechtenstein')),
    ('Sri Lanka', _('Sri Lanka')),
    ('Liberia', _('Liberia')),
    ('Lesotho', _('Lesotho')),
    ('Lithuania', _('Lithuania')),
    ('Luxembourg', _('Luxembourg')),
    ('Latvia', _('Latvia')),
    ('Libyan Arab Jamahiriya', _('Libyan Arab Jamahiriya')),
    ('Morocco', _('Morocco')),
    ('Monaco', _('Monaco')),
    ('Moldova, Republic of', _('Moldova, Republic of')),
    ('Madagascar', _('Madagascar')),
    ('Marshall Island', _('Marshall Islands')),
    ('Mali', _('Mali')),
    ('Mongolia', _('Mongolia')),
    ('Myanmar', _('Myanmar')),
    ('Macau', _('Macau')),
    ('Northern Mariana Islands', _('Northern Mariana Islands')),
    ('Martinique', _('Martinique')),
    ('Mauritania', _('Mauritania')),
    ('MS', _('Monserrat')),
    ('Malta', _('Malta')),
    ('Mauritius', _('Mauritius')),
    ('Maldives', _('Maldives')),
    ('Malawi', _('Malawi')),
    ('Mexico', _('Mexico')),
    ('Malaysia', _('Malaysia')),
    ('Mozambique', _('Mozambique')),
    ('Namibia', _('Namibia')),
    ('Caledonia', _('New Caledonia')),
    ('Niger', _('Niger')),
    ('Norfolk', _('Norfolk Island')),
    ('Nigeria', _('Nigeria')),
    ('Nicaragua', _('Nicaragua')),
    ('Netherlands', _('Netherlands')),
    ('Norway', _('Norway')),
    ('Nepal', _('Nepal')),
    ('Nauru', _('Nauru')),
    ('Niue', _('Niue')),
    ('Zealand', _('New Zealand')),
    ('Oman', _('Oman')),
    ('Panama', _('Panama')),
    ('Peru', _('Peru')),
    ('French Polynesia', _('French Polynesia')),
    ('Papua New Guinea', _('Papua New Guinea')),
    ('Philippines', _('Philippines')),
    ('Pakistan', _('Pakistan')),
    ('Poland', _('Poland')),
    ('St. Pierre & Miquelon', _('St. Pierre & Miquelon')),
    ('Pitcairn', _('Pitcairn')),
    ('Puerto', _('Puerto Rico')),
    ('Portugal', _('Portugal')),
    ('Palau', _('Palau')),
    ('Paraguay', _('Paraguay')),
    ('Qatar', _('Qatar')),
    ('Reunion', _('Reunion')),
    ('Romania', _('Romania')),
    ('Russian', _('Russian Federation')),
    ('Rwanda', _('Rwanda')),
    ('Saudi Arabia', _('Saudi Arabia')),
    ('Solomon', _('Solomon Islands')),
    ('Seychelles', _('Seychelles')),
    ('Sudan', _('Sudan')),
    ('Sweden', _('Sweden')),
    ('Singapore', _('Singapore')),
    ('St. Helena', _('St. Helena')),
    ('Slovenia', _('Slovenia')),
    ('Svalbard', _('Svalbard & Jan Mayen Islands')),
    ('Slovakia', _('Slovakia')),
    ('Sierra Leone', _('Sierra Leone')),
    ('San Marin', _('San Marino')),
    ('Senegal', _('Senegal')),
    ('Somalia', _('Somalia')),
    ('Suriname', _('Suriname')),
    ('Sao Tome & Principe', _('Sao Tome & Principe')),
    ('El Salvador', _('El Salvador')),
    ('Syrian', _('Syrian Arab Republic')),
    ('Swaziland', _('Swaziland')),
    ('Turks', _('Turks & Caicos Islands')),
    ('Chad', _('Chad')),
    ('French', _('French Southern Territories')),
    ('Togo', _('Togo')),
    ('Thailand', _('Thailand')),
    ('Tajikistan', _('Tajikistan')),
    ('Tokelau', _('Tokelau')),
    ('Turkmenistan', _('Turkmenistan')),
    ('Tunisia', _('Tunisia')),
    ('Tonga', _('Tonga')),
    ('East Timor', _('East Timor')),
    ('Turkey', _('Turkey')),
    ('Trinidad', _('Trinidad & Tobago')),
    ('Tuvalu', _('Tuvalu')),
    ('Taiwan', _('Taiwan, Province of China')),
    ('Tanzania', _('Tanzania, United Republic of')),
    ('Ukraine', _('Ukraine')),
    ('Uganda', _('Uganda')),
    ('Minor Outlying Islands', _('United States Minor Outlying Islands')),
    ('US', _('United States of America')),
    ('Uruguay', _('Uruguay')),
    ('Uzbekistan', _('Uzbekistan')),
    ('Vatican City', _('Vatican City State (Holy See)')),
    ('St. Vincent & the Grenadines', _('St. Vincent & the Grenadines')),
    ('Venezuela', _('Venezuela')),
    ('British Virgin Islands', _('British Virgin Islands')),
    ('United States Virgin Islands', _('United States Virgin Islands')),
    ('Viet', _('Viet Nam')),
    ('Vanuatu', _('Vanuatu')),
    ('Wallis', _('Wallis & Futuna Islands')),
    ('Samoa', _('Samoa')),
    ('Yemen', _('Yemen')),
    ('Mayotte', _('Mayotte')),
    ('Yugoslavia', _('Yugoslavia')),
    ('South Africa', _('South Africa')),
    ('Zambia', _('Zambia')),
    ('Zaire', _('Zaire')),
    ('Zimbabwe', _('Zimbabwe')),
    ('Unknown', _('Unknown or unspecified country')),
)
Related_to = [
	('Medicalwriting', 'Medical Writing'),
	('Assignmentwriting', 'Assignment Writing'),
	('TechnicalWriting ' ,' Technical Writing ' ),
	('ResearchProjectWriting', ' Research Project Writing' ),
  ('Dissertation Writing', 'Dissertation Writing' ),

	]
class CareerModel(models.Model):
    name			= models.CharField(max_length=254)
    timestamp   = models.DateTimeField(auto_now=False,auto_now_add=True)
    file 			= models.FileField(upload_to="file/", null=True, blank=True)
    Applying_For	= models.CharField(max_length=254, choices=Related_to, default=" ")
    email			= models.CharField(max_length=254, null=False, blank=False, default="")
    country 		= models.CharField(max_length=25, choices=COUNTRY,default="")
    Phone_Number 	= models.CharField(max_length=20, default="", null=True, blank=True)
    skype_id			= models.CharField(max_length=254, null=False, blank=False, default="")
    Linkedin_profile			= models.CharField(max_length=254, null=False, blank=False, default="")
    
    Describe_yourself			= models.TextField(max_length=5000, null=False, blank=False, default="")

    def __str__(self):
      return self.name

def order_post_save(sender, instance, *args, **kwargs):
  if instance.name:
    subject = "Order submission on AcademiaBuddy"
    message = "Hi Divya \n A person has applied for the job at AcademiaBuddy. Click the below link to know more about it. \n https://www.academiabuddy.com/admin/careers/careermodel/"
    send_mail(subject,message,'alihunaid185@gmail.com',['alihunaid185@gmail.com@gmail.com'])

post_save.connect(order_post_save, sender=CareerModel)
