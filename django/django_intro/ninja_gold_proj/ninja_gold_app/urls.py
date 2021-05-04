
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index),
#     path('process_money', views.get_gold_farm),
#     path('reset', views.reset)
# ]

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('gold', views.process_gold)
]