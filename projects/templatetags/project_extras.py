from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def md_render(value):
    
    html = markdown.markdown(value)
    return mark_safe(html)
