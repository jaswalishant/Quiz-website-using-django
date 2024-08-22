from django import template

register=template.Library()

@register.filter
def index(mylist, i):
    return mylist[i]