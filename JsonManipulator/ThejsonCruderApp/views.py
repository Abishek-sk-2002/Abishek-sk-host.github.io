from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .QueryManipulation import listUserData,insertUserDetails,updateUserDetails
from .serializers import DataSerializer

def helloWorldFunction(request):
    return HttpResponse("Hello world!")


def RetrieveUserData(request):
    if request.method == 'GET':
        resultData  = listUserData()
        json_data   = json.dumps(resultData, indent=2)
        return JsonResponse(json.loads(json_data), safe=False)


# @csrf_exempt
def CreateUserData(request):
    if request.method == 'POST':
        user_name = request.POST.get('user-name')
        email_id = request.POST.get('email-id')
        if insertUserDetails(user_name, email_id):
            return JsonResponse({'message': 'Data inserted successfully'})
        else:
            return JsonResponse({'message': 'Something went wrong while inserting data'})
    return JsonResponse({'message': 'Invalid request method'})

def UpdateUserData(request):
    if request.method == 'POST':
        user_id = int(request.POST.get('user-id'))
        user_name = request.POST.get('user-name')
        email_id = request.POST.get('email-id')
        print(user_id,user_name,email_id)
        if(updateUserDetails(user_id,user_name,email_id)):
            return JsonResponse ({'message': 'Data Updated successfully'})
        else:
            return JsonResponse({'message':'Somthing went wrong while updating data in the database'})
    return JsonResponse({'message': 'Invalid request method'})

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def ApiView(request):
    sampleJsonData = {
        'Language': 'Python',
        'Framework':'Django'
    }
    return Response({'data':sampleJsonData})

@api_view()
def RetrieveUserDataUsingSerializers(request):
    # if request.method == 'GET':
    result_data = listUserData()
    data_list = [{'user_id': item[0], 'user_name': item[1], 'email_id': item[2]} for item in result_data]
    serializer = DataSerializer(data_list )
    return Response(serializer.data)

