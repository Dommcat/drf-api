from rest_framework import serializers
from .models import Drummer

class DrummerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'band', 'name', 'drum_brand', 'genre' , 'active', 'created_at', 'updated_at')
        model = Drummer

# id is auto created then add fields in the model 

    # name = models.CharField(max_length=100)
    # band = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # drum_brand = models.CharField(max_length=100)
    # genre = models.CharField(max_length=100)
    # active = models.BooleanField(default=False)   
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)