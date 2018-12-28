from ids.models import Report


class IdsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        report = Report()
        report.remote_address = request.META.get('REMOTE_ADDR')
        report.user_agent = request.META.get('HTTP_USER_AGENT')
        report.save()
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
