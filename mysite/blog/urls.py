from django.conf.urls import url
from blog.views import (AboutView,
                        PostListView,
                        PostDetailView,
                        PostCreateView,
                        PostUpdateView,
                        PostDeleteView,
                        DraftListView,
                        add_comments_to_post,
                        comment_approve,
                        comment_remove,
                        post_publish)


urlpatterns = [
    url(r'^$', PostListView.as_view(),name='post_list'),
    url(r'^about/$', AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$', PostCreateView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', PostUpdateView.as_view(),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$', DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', add_comments_to_post,name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/delete/$', comment_remove,name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', post_publish,name='post_publish'),
]