"""recipes URL Configuration

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

from django.urls import path
from calculator.views import home_view_1, omlet_view, pasta_view #, ingr_list, ingr_details
from django.contrib import admin


urlpatterns = [
    path('', home_view_1, name='home1'),
    path('omlet/', omlet_view, name='omlet'),
    path('pasta/', pasta_view, name='pasta'),
  #  path('ingridients/', ingr_list, name='listing'),
  #  path('/<str:ingr_id>/', ingr_details, name='details'),
    path('admin/', admin.site.urls),
]
