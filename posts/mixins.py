from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime

class TargetDateValidationMixin:
    def clean_target_date(self):
        target_date = self.cleaned_data.get('target_date')

        # Convert target_date to a datetime.date object if it's a datetime.datetime object
        if isinstance(target_date, datetime):
            target_date = target_date.date()

        if target_date < timezone.now().date():
            raise ValidationError('Target date cannot be in the past.')
        return target_date
