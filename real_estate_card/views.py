from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from real_estate_card import permissions
from real_estate_card.models import RealEstate
from real_estate_card.serializer import EstateSerializer


class EstateView(ModelViewSet):
    queryset = RealEstate.objects.all()
    serializer_class = EstateSerializer
    permission_classes = [permissions.IsAdmin, permissions.HasAccess]


def objectcard(request):
    return render(request, 'objectcard.html')


def object_update(request):
    return render(request, 'editingcard.html')


def reestr(request):
    return render(request, 'reestr.html')


def estate_card(request):
    return render(request, 'obj1.html')


def index(request):
    return render(request, 'index.html')


class DeleteEstateView(ModelViewSet):
    queryset = RealEstate.objects.all()
    serializer_class = EstateSerializer
    permission_classes = [permissions.IsAdmin]
