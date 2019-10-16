from django.conf.urls import url
from . import views


urlpatterns = [
    url (r'^$',views.home),
    url (r'^main$',views.main),
    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url (r'^weight$',views.weight_index),
    url (r'^strength$',views.strength_index),
    url (r'^exercise$',views.exercise_index),
]
