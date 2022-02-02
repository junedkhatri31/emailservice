from django.http import JsonResponse
from rest_framework.views import APIView
from emailservice.messages.utils import send_email_in_background
from rest_framework.parsers import FormParser, MultiPartParser

class MessageView(APIView):
    """
    MessageView

    This view uses the POST method to deliver the email. Supports only POST method to send email.

    Supported POST paramters `from`, `to`, `subject`, `message`

    """

    parser_classes = [FormParser, MultiPartParser]
    authentication_classes = []

    def post(self, request):
        """
        Post method accepts from, to, subject and message from request body in form enoding
        It will start background task to send an email with provided configurations.

        celery task id will be returned.
        """
        required_fields = ['from', 'to', 'subject', 'message']
        request_keys = request.POST.keys()
        for required_field in required_fields:
            if required_field not in request_keys:
                return JsonResponse({
                    "message": f"'{required_field}' is required in POST parameters"
                }, status=400)
        result = send_email_in_background.delay(request.POST['from'], request.POST['to'], request.POST['subject'], request.POST['message'])
        return JsonResponse({
            "task_id": result.id
        })

    def options(self, request, *args, **kwargs):
        print(self.parser_classes)
        return super().options(request, *args, **kwargs)
