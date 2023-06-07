from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view 
from . import views
from .forms import LoginForm
urlpatterns=[
     path('base/',views.base_view),
     path('',views.home_view,name='home'),
     path('about/',views.about_view,name='about'),
     path('contact/',views.contact_view,name='contact'),
     path('registration/',views.CustomerRegistrationView.as_view(),name='registration'),
     path('account/login/',auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
     path('profile/', views.ProfileView.as_view(), name='profile'),
     path('address/', views.address,name='address'),
     path('update/<pk>', views.UpdateAddressView.as_view(), name='update'),
     path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
     path('proddetail/<int:pk>', views.ProductDetail.as_view(), name='proddetail'),
     path('category-title/<val>', views.CategoryTitle.as_view(), name='category-title'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


