from django.urls import path
from .views import DrummerList, DrummerDetail



urlpatterns = [
    path('', DrummerList.as_view(), name='drummer_list'),
    path('<int:pk>', DrummerDetail.as_view(), name='drummer_detail'),
]
    # 'about' is the url
    # HomePageView() is the class in views.py





