from django import template

register = template.Library()

from ..models import Mytext

@register.simple_tag(name='my_tag')
def total_post():
    return  Mytext.name.count()

@register.inclusion_tag('artical.html')
def show_latest_post(count = 10):
    latest_posts = Mytext.updated.order_by('updated')[:count]
    return {'latest-posts':latest_posts}