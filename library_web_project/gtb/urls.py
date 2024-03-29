"""gtb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from books.views import home_veiw, books_veiw,book_veiw, book_main_view
from profiles.views import order_view

urlpatterns = [
    path('',home_veiw, name='welcomepage'),
    path('accounts/', include('allauth.urls')),
    path("profile/", order_view),
    path("book_main/", book_main_view, name="dashboard"),
    path('books/',books_veiw, name='books'),
    path('books_table/',books_veiw, name='books_table'),
    path('book/<int:book_id>/',book_veiw, name='book'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
