from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now
from datetime import timedelta
register = template.Library()

@register.filter(name='timesince')
def time_since(value):
    """Dado un datetime, devuelve cuánto tiempo ha pasado desde esa fecha"""  
    if (now().date() - value).days < 1:
        return "today"
    else:
        return f"{timesince(value, depth=1)} ago"
