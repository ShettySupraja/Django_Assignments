from django.shortcuts import render
from django.http import JsonResponse

from flightApp.models import Passenger
from rest_framework.decorators import api_view
from flightApp.serializers import PassengerSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# def passenger(request):
#     # Below is the static data without any model defined
#     # data_static = {
#     #     "passenger": "John Doe",
#     #     "flight": "Singapore Airlines",
#     #     "date": "2021-12-01",
#     #     "time": "12:00"
#     # }
    
#     # Below is the dynamic data with model defined
#     data = Passenger.objects.all()
#     response = {'passengers': list(data.values('first_name','last_name','dob','travelPoints'))}
    
#     return JsonResponse(response)



# create a new view to display the passenger details using function based view
@api_view(['GET', 'POST'])
def passenger_list(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def passenger_details(request, pk):
    try:
        passenger = Passenger.objects.get(pk=pk)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =PassengerSerializer(passenger)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer= PassengerSerializer(passenger, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)