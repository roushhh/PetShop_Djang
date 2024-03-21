from django import template
from datetime import datetime


register=template.Library()


def printdate():
    return datetime.now().strftime("%d-%m-%y")



register.filter("printdate",printdate)

@register.filter(name="multiply")
def multiply(v1,v2):
    return v1*v2