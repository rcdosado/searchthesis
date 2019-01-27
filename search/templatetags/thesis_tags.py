from django import template
from ..models import Thesis


register = template.Library()


@register.simple_tag
def total_posts():
	return Thesis.published.count()

@register.inclusion_tag('search/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Thesis.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}
