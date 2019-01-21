from django import template
from ..models import Entry,Category,Notice

register = template.Library()

#加上装饰器的函数就是一个自定义的模板标签
@register.simple_tag
def get_recent_entries(num=3):
    return Entry.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def get_popular_entries(num=3):
    return Entry.objects.all().order_by('-visiting')[:num]

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_entry_count_of_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()

@register.simple_tag
def get_notice():
    return Notice.objects.all()

