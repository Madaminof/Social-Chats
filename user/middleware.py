from django.utils import timezone
from datetime import timedelta


class UpdateOnlineStatusMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = timezone.now()
            if now - request.user.last_login < timedelta(minutes=5):
                request.user.is_online = True
            else:
                request.user.is_online = False
            request.user.save()

        response = self.get_response(request)
        return response