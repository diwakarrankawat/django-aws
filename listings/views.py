from time import time
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView
from django.http.response import HttpResponse

from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.response import Response

# locals
from . import models, serializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 1000

# Create your views here.


class AllListings(ListCreateAPIView):
    queryset = models.Listing.objects.all()
    serializer_class = serializer.ListingSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        dt, _ = models.Day.objects.get_or_create()
        tm = time()
        try:
            data: list = request.data
            gdata: list = data.copy()
            if type(data) == list:
                for g in data:
                    if type(g) == dict:
                        if models.Listing.objects.filter(cid=g['cid']).exists():
                            gdata.remove(g)
            dt = serializer.ListingSerializer(data=gdata, many=True)
            if dt.is_valid():
                dt.save()
                return Response({"status": True, "message": f"created:{len(gdata)}, duplicates:{len(data)-len(gdata)}", "time-taken": f"{time()-tm}"}, 200)
            return Response({"errors": dt.errors, "time-taken": f"{time()-tm}"}, 400)
        finally:
            # return Response({"er":str(e)})
            pass


def something(request):
    return HttpResponse("<h1>This title will be updated</h1>")
