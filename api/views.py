from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.api.serializers import CategorySerializer
from products.models import Category


@api_view(['GET'])
def overview(request):

    api_urls = {
        'products' : {
            'category':{
                'list': 'category/',
            },
        }
    }

    return Response(api_urls)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)

    return Response(serializer.data)