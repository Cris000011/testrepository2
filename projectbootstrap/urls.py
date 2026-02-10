"""
URL configuration for projectbootstrap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),        # DODANE
    path('pricing/', views.pricing, name='pricing'),  # DODANE
    path('faq/', views.faq, name='faq'),               # DODANE
    path('contact/', views.contact, name='contact'),  # DODANE
    path('blog/', views.blog_home, name='blog_home'), # PODSTRONY BLOGA
    path('blog/post/', views.blog_post, name='blog_post'), # PODSTRONY BLOGA
    path('portfolio/', views.portfolio_overview, name='portfolio_overview'), # PORTFOLIO
    path('portfolio/item/', views.portfolio_item, name='portfolio_item'),  # PORTFOLIO


]
