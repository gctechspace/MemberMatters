from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from membermatters.helpers import log_user_event
from .models import MemberBucks
from profile.models import Profile, User
from constance import config
import pytz

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

utc = pytz.UTC

class Inductionquiz(APIView):
    """
    get: returns the member's current memberbucks balance.
    """

    def get(self, request):
        return Response({"balance": "profile.memberbucks_balance"})

