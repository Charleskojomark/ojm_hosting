# myapp/management/commands/send_bulk_emails.py

from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from userauth.models import User

class Command(BaseCommand):
    help = 'Send bulk customized emails to users'

    def handle(self, *args, **options):
        users = User.objects.all()
        
        for user in users:
            subject = 'Custom Email Subject'
            message = render_to_string('email_template.html', {
                'first_name': user.first_name,
                'last_name': user.last_name,
                # Add other context variables here
            })
            email = EmailMessage(
                subject,
                message,
                'Ojm Electrical',
                [user.email],
            )
            email.content_subtype = 'html'  # If sending HTML email
            email.send()

        self.stdout.write(self.style.SUCCESS('Successfully sent bulk emails.'))
