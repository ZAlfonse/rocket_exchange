from .models import Listing, User
from .serializers import ListingSerializer, UserSerializer

from rest_framework import viewsets
from django.http import HttpResponse


class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user

        return super(UserViewSet, self).get_object()

def debug(request):
    output = ""
    import pdb; pdb.set_trace()
    html = "<html><body>{}</body></html>".format(output)
    return HttpResponse(html)
