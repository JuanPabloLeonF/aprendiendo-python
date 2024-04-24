from django import template

register = template.Library()
@register.filter(name="hello")

def hello(value):
    return f"<h4 style='color:red'>{value}</h4>"