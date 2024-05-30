from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializer import ItemSerializer

@api_view(['GET'])
def Getdata(request):
    items = Item.objects.all()  # Retrieve all items from the database
    serializer = ItemSerializer(items, many=True)  # Serialize multiple items, so use many=True
    return Response(serializer.data)  # Pass serialized data to Response