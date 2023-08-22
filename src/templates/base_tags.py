from django import template

register = template.Library()

@register.simple_tag
def custom_tag():
    return "base"
