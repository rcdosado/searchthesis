from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from searchthesis.settings import PAGINATION_PER_PAGE
from .models import Thesis 


def thesis_list(request):
    object_list = Thesis.published.all()
    paginator = Paginator(object_list, PAGINATION_PER_PAGE)
    page = request.GET.get('page')
    try:
        theses = paginator.page(page)
    except PageNotAnInteger:
        theses = paginator.page(1)
    except EmptyPage:
        theses = paginator.page(paginator.num_pages)
    return render(request,
                'search/post/list.html',
                {'page':page,
                 'theses':theses})

def thesis_detail(request, year, month, day, thesis):
    thesis = get_object_or_404(Thesis, slug=thesis,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,
                    'search/post/detail.html',
                    {'thesis':thesis})