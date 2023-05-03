from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Drummer
from .serializer import DrummerSerializer




# Create your views here.
class DrummerList(ListAPIView):
  queryset = Drummer.objects.all()
  serializer_class = DrummerSerializer


class DrummerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Drummer.objects.all()
    serializer_class = DrummerSerializer




# class DrummerDetail(ListAPIView):
#   queryset = Drummer.objects.all()
#   serializer_class = DrummerSerializer
