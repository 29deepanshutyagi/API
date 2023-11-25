from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
import requests
# In your views.py or views module
from rest_framework.permissions import IsAuthenticated, AllowAny


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def data(request):
    if request.method == "GET":
        api_url = "https://data.sec.gov/api/xbrl/companyfacts/CIK0001544522.json"
        response = requests.get(api_url)
        print(response)
        
        if response.status_code == 200:
            if response.content:
                data = response.json()
                print(data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response("Empty response", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(f"Failed to fetch data. Status code: {response.status_code}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

