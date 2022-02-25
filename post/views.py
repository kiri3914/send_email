from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForms
from .service import send
from .tasks import send_span_email


class ContactView(CreateView):
    model = Contact
    form_class = ContactForms
    success_url = '/'
    template_name = 'post/index.html'

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_span_email.delay(form.instance.email)
        return super().form_valid(form)
