from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.simple_tag
def md_render(value):
    
    html = markdown.markdown(value)
    return mark_safe(html)

@register.simple_tag
def md_render_short(value):
    shortVal = value.split('<!--shorten-->', 1)

    html = markdown.markdown(shortVal[0])
    return mark_safe(html)
