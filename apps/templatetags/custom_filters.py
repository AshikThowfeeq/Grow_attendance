from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(dictionary, key, default_value="Absent"):
    return dictionary.get(key,  default_value)
