import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataView(APIView):
    def get(self, request):
        id = request.query_params.get('id')
        if not id:
            return Response({"error": "ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.get(
                f'https://sitr.cnd.com.pa/m/pub/data/gen.json?{id}')
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
