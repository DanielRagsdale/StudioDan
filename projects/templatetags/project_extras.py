from django import template

register = template.Library()

@register.simple_tag
def md_render(value):

    return "test"
