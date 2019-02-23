from django.conf.urls import url
from services import views

app_name = 'services'

urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^vision/$', views.vision, name='vision'),
    url(r'^industry-structure/$', views.ind_str, name='ind_str'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^saving/$', views.saving, name='saving'),
    url(r'^recurring/$', views.recurring, name='recurring'),
    url(r'^monthlyincome/$', views.monthly, name='monthly'),
    url(r'^fixedDeposit/$', views.fixed, name='fixed'),
    url(r'^dailyDeposit/$', views.daily, name='daily'),
    url(r'^goldloan/$', views.gold, name='gold'),
    url(r'^grouploan/$', views.group, name='group'),
    url(r'^loan-against-deposit/$', views.loanagainstdeposit, name='loanagainstdeposit'),
    url(r'^loan-against-govt-securities/$', views.loanagainstgovtsec, name='loanagainstgovtsec'),
    url(r'^mortgage/$', views.mortgage, name='mortgage'),
    url(r'^personal/$', views.personal, name='personal'),
]
