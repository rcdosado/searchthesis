from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q, Count
from taggit.models import Tag

from searchthesis.settings import PAGINATION_PER_PAGE
from .models import Thesis, Comment, PublishedManager
from .forms import CommentForm


def thesis_list(request, tag_slug=None):
    object_list = Thesis.published.all()
    if request.method == 'POST':
        query = request.POST.get("q")
        if query:
            object_list=Thesis.published.filter(
                Q(title__icontains=query) |
                Q(abstract__icontains=query) |
                Q(authors__icontains=query) 
                ).order_by('-publish')
            # import pdb; pdb.set_trace()

    tag = None 
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    # import pdb; pdb.set_trace()
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
    # list of active comments for this thesis
    comments = thesis.comments.filter(active=True)

    new_comment = None 
    current_user = None

    if request.user.is_authenticated:
        current_user = request.user
        
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = thesis 
            if current_user:
                new_comment.user = current_user
            new_comment.save()
            return redirect(thesis)
    else:
        comment_form = CommentForm()
    thesis_tags_ids = thesis.tags.values_list('id', flat=True)
    similar_thesis = Thesis.published.filter(tags__in=thesis_tags_ids)\
                                     .exclude(id=thesis.id) 
    similar_thesis = similar_thesis.annotate(same_tags=Count('tags'))\
                                   .order_by('-same_tags', '-publish')[:4]
    # import pdb; pdb.set_trace()
    return render(request,
                    'search/post/detail.html',
                    {'thesis':thesis,
                     'comments':comments,
                     'current_user':current_user,
                     'new_comment':new_comment,
                     'comment_form':comment_form,
                     'similar_thesis': similar_thesis})
