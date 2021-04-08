from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

from transformers.models import Transformer, Customer
from django.contrib.auth.models import User
from transformers.serializers import TransformerSerializer, CustomerSerializer

@api_view(['GET','POST'])
def transformer_list(request):
	"""
	List all transformers, or create a new transformer
	"""
	if request.method == 'GET':
		transformer = Transformer.objects.all()
		serializer = TransformerSerializer(transformer, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = TransformerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
							status=status.HTTP_201_CREATED)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def transformer_detail(request, pk):
	try:
		transformer = Transformer.objects.get(pk=pk)
	except Transformer.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TransformerSerializer(transformer)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = TransformerSerializer(transformer, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'PATCH':
		serializer = TransformerSerializer(transformer,
										data=request.data,
										partial=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		transformer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def usersData(request, obj):
	"""
	List all customers' transformers, or create a new transformer for customer
	"""
	if request.method == 'GET':
		transformerdata = []

		customer = Customer.objects.get(id=obj)
		transformers = customer.transformer_set.all()

		for i in transformers:
			transformerdata.append({'customer_name' : i.customer.name,
									'customer_id' : i.customer.id, 
									'transformer_name' : i.name,
									'description' : i.description,
									'alternate_mode' : i.alternate_mode,
									'alive' : i.alive,
									'transformer_id' : i.id })
		return JsonResponse(transformerdata, safe=False)

	elif request.method == 'POST':
		serializer = TransformerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,
							status=status.HTTP_201_CREATED)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def usersDataDetail(request, obj, pk):
	"""
	control users data details'
	"""
	try:
		transformer = Transformer.objects.get(pk=pk)
		customer = Customer.objects.get(id=obj)
	except Transformer.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TransformerSerializer(transformer)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = TransformerSerializer(transformer, data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'PATCH':
		serializer = TransformerSerializer(transformer,
										data=request.data,
										partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors,
						status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		transformer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
