from django.db.models import F
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from .models import AccessLevel, Profession
from .serializers import AccessLevelSerializer, ProfessionSerializer


class AccessLevelViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Return a list of all possible access levels."""

    queryset = AccessLevel.objects.all().order_by(
        F("order").asc(nulls_last=True), "name"
    )
    serializer_class = AccessLevelSerializer
    permission_classes = (AllowAny,)
    pagination_class = None


class ProfessionViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """Return a list of all possible professions."""

    queryset = Profession.objects.all().order_by(
        F("order").asc(nulls_last=True), "name"
    )
    serializer_class = ProfessionSerializer
    permission_classes = (AllowAny,)
