from django.urls import path
from . import views


urlpatterns = [
    path ('e',views.e,name='e'),
    path('insert',views.insert,name='insert'),
    path('get',views.get,name='get'),
    path('edit/<int:eid>',views.edit,name='edit'),
    path('update/<int:eid>',views.update,name='update'),
     path('delete/<int:eid>',views.delete,name='delete')


]