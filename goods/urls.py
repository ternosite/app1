"""   
1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from goods import views

app_name = 'catalog'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product'),
]