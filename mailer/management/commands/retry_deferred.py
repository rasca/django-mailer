import logging

from django.core.management.base import NoArgsCommand
from django.conf import settings

from mailer.models import Message

# The maximum amount of emails we are goind to retry sending
RETRY_LIMIT = getattr(settings, "MAILER_RETRY_LIMIT", None)


class Command(NoArgsCommand):
    help = "Attempt to resend any deferred mail."
    
    def handle_noargs(self, **options):
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
        count = Message.objects.retry_deferred(limit=RETRY_LIMIT) # @@@ new_priority not yet supported
        logging.info("%s message(s) retried" % count)
