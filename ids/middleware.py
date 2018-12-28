from ids.models import Report
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser


class IdsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        n1 = 15
        h = 10
        n2 = 10
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        report = Report()
        report.remote_address = request.META.get('REMOTE_ADDR')
        report.user_agent = request.META.get('HTTP_USER_AGENT')
        req = Report.objects.filter(remote_address=request.META.get('REMOTE_ADDR')).order_by('-date_time')[0]
        if request.user.is_anonymous:
            try:
                report.nn=req.nn+1
                if report.nn > n2:
                    return HttpResponse('GFYS2')
            except:
                pass
        try:
            if datetime.now().second - req.date_time.second < h:
                report.n = req.n + 1
            if report.n > n1:
                return HttpResponse('GFYS1')
        except:
            pass
        report.save()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
