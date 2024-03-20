from rest_framework import serializers
from .models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id','first_name', 'last_name', 'dob', 'travelPoints'] 
        # or fields = __all__ will return all the fields in the model