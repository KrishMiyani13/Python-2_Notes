from django.urls import path
<<<<<<< HEAD
from api1.views import public_view,private_view
urlpatterns = [
    path('public/',public_view,name="public_view"),
    path('private/',private_view,name="private_view")
=======
from api1.views import public_view,privet_view

urlpatterns = [
    path('public/',public_view,name='public_view'),
    path('privet/',privet_view,name='privet_view')
>>>>>>> bb6dde2e5fb9d750dbe7c15e0c66699b5d9a21c2
]
