from django.shortcuts import render, get_object_or_404, redirect
from .models import Publication, Category, User, Edition
from django.utils import timezone
from django.core.paginator import Paginator
from django.views import View
from publications.forms import UserEditForm, PublicationForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.
PAGE_NUM = 10


def index_editions(editions):
    editions = editions.order_by('-pub_date')
    editions = editions.order_by(
        "-pub_date"
    )
    return editions


def index(request):
    dt_now = timezone.now()
    editions = Edition.objects.filter(
        pub_date__lte=dt_now,
        is_published=True,
        category__is_published=True
    )
    editions = index_editions(editions)
    paginator = Paginator(editions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'publications/index.html', {'page_obj': page_obj})


def edition_detail(request, category_slug, edition_slug):
    dt_now = timezone.now()
    category = get_object_or_404(
        Category,
        pub_date__lte=dt_now,
        slug=category_slug,
    )
    edition = get_object_or_404(
        Edition,
        pub_date__lte=dt_now,
        slug=edition_slug,
        category=category,
    )
    publications = Publication.objects.filter(
        pub_date__lte=dt_now,
        edition=edition,
    )
    paginator = Paginator(publications, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'category': category,
        'edition': edition,
    }
    return render(request, 'publications/edition.html', context)


def category_list(request):
    dt_now = timezone.now()
    category = Category.objects.filter(
        pub_date__lte=dt_now,
    )
    paginator = Paginator(category, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'publications/categories_list.html', context)


def category_detail(request, category_slug):
    dt_now = timezone.now()
    category = get_object_or_404(
        Category,
        pub_date__lte=dt_now,
        slug=category_slug,
    )
    edition = Edition.objects.filter(
        pub_date__lte=dt_now,
        category=category,
    )
    paginator = Paginator(edition, PAGE_NUM)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'category': category,
    }
    return render(request, 'publications/category_detail.html', context)


def publication_detail(request, category_slug, edition_slug, post_id):
    dt_now = timezone.now()
    category = get_object_or_404(
        Category,
        pub_date__lte=dt_now,
        slug=category_slug,
    )
    edition = get_object_or_404(
        Edition,
        pub_date__lte=dt_now,
        slug=edition_slug,
        category=category,
    )
    publication = get_object_or_404(
        Publication,
        pub_date__lte=dt_now,
        edition=edition,
        pk=post_id,
    )
    context = {
        'publication': publication,
        'category': category,
        'edition': edition,
    }
    return render(request, 'publications/detail.html', context)


@login_required
def article_application(request):
    pass


class Profile(View):
    template = 'publications/profile.html'

    def get(self, request, **kwargs):
        username = kwargs['username']
        profile = get_object_or_404(User, username=username)
        author = Profile.objects.get(user=profile)
        publications = Publication.objects.filter(author=profile)
        publications = publications.order_by('-pub_date')
        paginator = Paginator(publications, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        contex = {
            "profile": profile,
            'author': author,
            'page_obj': page_obj
        }
        return render(request, self.template, contex)


class AdminPanel(View):
    template = 'publications/AdminPanel.html'

    def get(self, request, **kwargs):
        pass

    def post(self, request):
        pass

    def patch(self, request):
        pass
