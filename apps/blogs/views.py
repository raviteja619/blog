"""Api File for presentation."""

from django.views.generic import TemplateView
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import Blog
from .forms import BlogForm, BlogEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
import logging

logger = logging.getLogger('main')


class BlogView(TemplateView):
    """List all presentation, or create a new user."""

    template_name = 'all_presentations.html'

    def render_to_response(self, context, **response_kwargs):
        """Render method for the view."""
        context['entries'] = Blog.objects.all()
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


class NewBlogView(LoginRequiredMixin, TemplateView):
    """List all presentation, or create a new user."""

    template_name = 'add_new_blog.html'

    def render_to_response(self, context, **response_kwargs):
        """Render method for the view."""
        context['form'] = BlogForm(self.request)
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **response_kwargs
        )


def get_blog_summary(request, slug):
    """Get the summary of ppt over the modal."""
    # slug = request.GET.get('slug', None)
    p = Blog.objects.filter(slug=slug)
    ctx = {
        'blog': p,
        'user': request.user
    }
    return render_to_response('blog_detail.html', ctx, context_instance=RequestContext(request))


def edit_blog(request, slug):
    """Get the summary of ppt over the modal."""
    # slug = request.GET.get('slug', None)
    try:
        p = Blog.objects.get(slug=slug)
    except:
        logger.error('Blog Not found')
        p = None
    ctx = {'blog': p, 'form': BlogEditForm(request, instance=p), 'user': request.user}
    return render_to_response('edit_blog.html', ctx, context_instance=RequestContext(request))
