from django import template
from django.db.models import Count
from ..models import Thesis


register = template.Library()


@register.simple_tag
def total_posts():
	return Thesis.published.count()

@register.inclusion_tag('search/post/latest_posts.html')
def show_latest_posts(count=5):
	latest_posts = Thesis.published.order_by('-publish')[:count]
	return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
	return Thesis.published.annotate(
				total_comments=Count('comments')
		).order_by('-total_comments')[:count]