from django.urls import path
from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'categories/<slug:category_slug>/editions/<slug:edition_slug>/publications/<int:post_id>/',
        views.publication_detail,
        name='publication_detail'
    ),
    path(
        'categories/<slug:category_slug>/editions/<slug:edition_slug>/',
        views.edition_detail,
        name='edition_detail'
    ),
    path(
        'categories/<slug:category_slug>/',
        views.category_detail,
        name='category_detail'
    ),
    path(
        'categories/',
        views.category_list,
        name='categories_list'
    ),
    path(
        'profile/<slug:username>/',
        views.Profile.as_view(),
        name='profile'
    ),
    path(
        'application/',
        views.article_application,
        name='application'
    ),
    path(
        'edit_publication/<int:publication_id>/',
        views.AdminPanel.as_view(),
        name='edit_publication'
    ),
    path(
        'edit_publication/<int:publication_id>/',
        views.AdminPanel.as_view(),
        name='delete_publication'
    )
]
