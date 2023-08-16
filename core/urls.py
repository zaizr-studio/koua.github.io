from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='home'),
    path('post/', views.post, name='post'),
    path('signup/', views.register, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('profile/<int:userID>', views.profile, name='profile'),
    path('product/<int:postID>', views.product, name='product'),
    path('edit/<int:postID>', views.edit, name='edit'),
    path('delete/<int:postID>', views.delete, name='delete'),
    path('search', views.search, name='search'),
    path('store', views.store, name='store'),
    path('verify_email/<uidb64>/<token>', views.activate_user, name='activate'),
]