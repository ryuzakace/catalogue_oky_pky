from rest_framework.decorators import api_view, throttle_classes, APIView

from .serializers import CategoriesSerializer, SubCategoriesSerializer, ProductsSerializer
from ..models import Categories, SubCategories, Products
from rest_framework.response import Response
import json

@api_view(['GET'])
def categories(request):
    data = Categories.objects.all()
    serializer = CategoriesSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sub_categories(request):
    try:
        pk = list(Categories.objects.values('category', 'id').filter(category=request.GET['category']))[0]['id']
        data_g = SubCategories.objects.filter(category = pk)
        print('1')
        serializer = SubCategoriesSerializer(data_g, many = True)
        print(2)
        print("3", serializer)
        return Response(serializer.data)
    except Exception as e:
        print(e.__str__())
        return Response(e.__str__())


class ProductList(APIView):

    def get(self, request):

        queryparam = dict(request.GET)

        product_list = []

        category = queryparam.get('category', None)
        sub_category = queryparam.get('sub_category', None)

        """If get request contains category field"""
        try:
            if category:
                category = category[0]
                cat_id = Categories.objects.values('id').get(category = category)['id']
                sub_category_ids = list(SubCategories.objects.values('id').filter(category = cat_id))
                for id in sub_category_ids:
                    i = id['id']
                    products_query = Products.objects.filter(sub_category = i)
                    serializer_product = ProductsSerializer(products_query, many=True)
                    product_list.extend(serializer_product.data)
        except Exception as e:
            print(e.__str__())
            return Response("Error in category")

        """If get request contains sub_category field"""
        try:
            if sub_category:
                sub_category = sub_category[0]
                sub_category_id = SubCategories.objects.values('id').get(sub_category = sub_category)['id']
                products_query = Products.objects.filter(sub_category=sub_category_id)
                serializer_product = ProductsSerializer(products_query, many=True)
                product_list.extend(serializer_product.data)
        except Exception as e:
            print(e.__str__())
            return Response("Error in subcategory")

        return Response(product_list)


    def post(self, request):
        payload = dict(json.dumps(request.POST))

        try:
            print(payload)
            product_name = payload['product']
            sub_category_name = payload['sub_category']
            category = payload['category']
            """adding new product under EXISTING category + sub_category"""
            try:
                product = Products()
                product.sub_category = list(SubCategories.objects.values('id').filter(sub_category = sub_category_name))[0]['id']
                product.product = product_name
                product.save()
                print("Successfully added")
                return Response("Successfully added")
            except Exception as e:
                print(e.__str__())
                return Response("Something wrong with post addition")
        except Exception as e:
            print(e.__str__())
            return Response("Invalid Request")



    print("suck - sess")
    pass



