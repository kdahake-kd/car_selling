from django.shortcuts import render
from car.models import carList
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import carSerializer
from rest_framework import status
# def car_list_view(request):
#     cars=carList.objects.all()
#     context={
#         'cars':list(cars.values())
#     }
#     return JsonResponse(context)


# def car_detail_view(request,pk):
#     car=carList.objects.get(pk=pk)
#     context={
#         'name':car.name,
#         'description':car.description,
#         'active':car.active
#     }
#     return JsonResponse(context)


@api_view(['GET','POST'])
def car_list_view(request):
    if request.method=='GET':
        cars=carList.objects.all()
        serializers=carSerializer(cars,many=True)
        return Response(serializers.data)
    if request.method=='POST':
        serializers=carSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)



@api_view(['GET','PUT','DELETE'])
def car_detail_view(request,pk):
    if request.method=='GET':
        car=carList.objects.get(pk=pk)
        serializers=carSerializer(car)
        return Response(serializers.data)
    if request.method=='PUT':
        car=carList.objects.get(pk=pk)
        serializers=carSerializer(car,data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    if request.method=='DELETE':
        car=carList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

