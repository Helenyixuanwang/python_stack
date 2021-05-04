
#from django.urls import path
#from . import views
#urlpatterns = [
#    path('', views.index)
#]



from django.urls import path     
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:number>', views.show, name='my_show'),
    path('<int:number>/edit', views.edit, name='my_edit'),
    path('<int:number>/delete', views.destroy, name='my_delete')
]