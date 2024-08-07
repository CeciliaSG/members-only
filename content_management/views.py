from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic, View

from .models import Post, SavedPost, LikedPost, Heading, Comment
from .forms import CommentForm, PostForm



class PostListView(generic.ListView):

    """
    Returns all published posts in :model:
    `content_management.Post`
    and displays them on the page in sections of
    as many post as their are for the filter.

    **Context**

    ``queryset``
        All published instances of :model:`Post`

    **Template:**

    :template:`content_management/index.html`
    """
    template_name = "content_management/index.html"
    posts = Post.objects.filter(status=1)
    context_object_name = 'posts'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(status=1)


def post_detail(request, slug):

    """
    From Blog walkthrough.

    Returns one published post in :model:
    `content_management.Post`
    and display on a details page.
    **Context**

    ``queryset``
        One published instance of :model:
        `content_management.Post`
        Filter for status and slug.

    **Template:**

    :template:`content_management/post_detail.html`

    """
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval')
        return redirect('post_detail', slug=slug)
    else:
        comment_form = CommentForm()

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form, },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment. From Blog walkthrough.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostListByHeadingView(generic.ListView):
    """
    Returns a heading id and parent-heading :model:
    `content_management.Heading`
    for filtering purposes
    **Context**

    ``queryset``
        Heading and parent heading :model:
        `content_management.Heading`
        For filtering and display purposes.

    **Template:**

    :template:`no specific template`

    """
    template_name = "content_management/index.html"
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        heading_id = self.kwargs.get('heading_id')
        parent_heading_name = self.kwargs.get('parent_heading_name')

        context['heading'] = Heading.objects.filter(id=heading_id)
        context['parent_heading'] = Heading.objects.filter(
            name=parent_heading_name)

        return context

    def get_queryset(self):
        heading_id = self.kwargs.get('heading_id')
        return Post.objects.filter(heading__id=heading_id, status=1)


def tag_filter(request, template_name, tags):

    """
    Returns one published post in :model:
    `content_management.Post`
    and display on a details page.
    **Context**

    ``queryset``
        Filters for multiple tags :model:
        `content_management.Post`
        Filter for status and slug.

    **Template:**

    :template:`multiple templates`

    """

    query = Q()

    for tag in tags:
        query |= Q(tag=tag, status=1)

    posts = Post.objects.filter(query)
    context = {
        'tags': tags,
        'posts': posts
    }

    return render(request, template_name, context)


def restaurants_bars_view(request, tags):
    tag_list = tags.split(',')
    template_name = 'content_management/restaurants_bars.html'
    return tag_filter(request, template_name, tag_list)


def things_to_do_view(request, tags):
    tag_list = tags.split(',')
    template_name = 'content_management/things_to_do.html'
    return tag_filter(request, template_name, tag_list)


def whats_on_view(request, tags):
    tag_list = tags.split(',')
    template_name = 'content_management/whats_on.html'
    return tag_filter(request, template_name, tag_list)


def perks_view(request, tags):
    tag_list = tags.split(',')
    template_name = 'content_management/perks.html'
    return tag_filter(request, template_name, tag_list)


def neighbourhoods_list_view(request):
    posts_with_neighbourhoods = Post.objects.exclude(
        neighbourhood__isnull=True).exclude(neighbourhood='')

    context = {
        'posts': posts_with_neighbourhoods
    }

    template_name = 'content_management/neighbourhoods.html'
    return render(request, template_name, context)


def post_tag_detail(request, tag):

    """
    Returns one published post in :model:
    `content_management.Post`
    and display on a details page.

    **Context**

    ``queryset``
       Tad and status :model:`content_management.Post`

    **Context**

    ``queryset``
        tag, status :model:`content_management.Post`
        For filtering and display purposes.

    **Template:**

    :template:`content_management/post_detail.html`


    """
    posts = Post.objects.filter(tag=tag, status=1)
    post = posts.first()

    return render(
        request,
        "content_management/post_detail.html",
        {"post": post, "tag": tag},
    )


@login_required
def save_post(request, post_id):

    """
    Returns one published post in database :model:
    `content_management.SavedPost`
    Checks if the post is already saved,
    un-save if saved, if not saved save to
    the database.

    **Context**

    ``queryset``
        One published instance of a post
        :model:`SavedPost`

    **Template:**

    :template:`multiple templates`

    """

    post = get_object_or_404(Post, id=post_id)

    try:
        saved_post = SavedPost.objects.get(user=request.user, post_id=post_id)
        saved_post.delete()
        return JsonResponse({
            'message': "You already saved this post. It is now unsaved!"})

    except SavedPost.DoesNotExist:

        post = Post.objects.get(id=post_id)
        saved_post = SavedPost(user=request.user, post=post)
        saved_post.save()

    return JsonResponse({'message': "Post saved successfully!"})


@login_required
def like_post(request, post_id):

    """
    Returns one published post in database :model:
    `content_management.LikedPost`
    Checks if the post is already liked,
    un-like if liked, if not saved the to the database.

    **Context**

    ``queryset``
        One published instance of a post (post_id) :model:`LikedPost`

    **Template:**

    :template:`multiple templates`

    """

    post = get_object_or_404(Post, id=post_id)

    try:
        liked_post = LikedPost.objects.get(user=request.user,
                                           post=post, post_id=post_id)
        liked_post.delete()
        message = "You unliked the post!"

    except LikedPost.DoesNotExist:

        liked_post = LikedPost(user=request.user, post=post)
        liked_post.save()
        message = "You liked the post!"

    return JsonResponse({'message': message, 'color': 'red'})


def about_page(request):

    """
    Returns/renders the static about.html.

    **Template:**

    :template:`about.html`

    """
    return render(request, 'content_management/footer/about.html')


def membership_page(request):

    """
    Returns/renders the static membership.html.

    **Template:**

    :template:`membership.html`

    """
    return render(request, 'content_management/footer/membership.html')


def partnerships_page(request):

    """
    Returns/renders the static partnership.html.

    **Template:**

    :template:`partnerships.html`

    """
    return render(request, 'content_management/footer/partnerships.html')


@login_required
def add_post(request):
    """
    View for adding a new Post object.

    On POST request:
    - Validates the form data submitted.
    - Saves the new post with the current authenticated user as
    the author.
    - Redirects to the detailed view of the newly created post upon
    successful save.
    - Displays an error message if a post with the same slug already
    exists.

    On GET request:
    - Initializes an empty form for creating a new post.

    Retrieves all existing posts and renders 'content_management/
    post_form.html' template with the form and posts context.

    Parameters:
    - request: HttpRequest object containing metadata about the request.

    Returns:
    - HttpResponse object rendering 'content_management/post_form.html'
    template with form and posts context.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            try:
                post.save()
                return redirect('post_detail', slug=post.slug)
            except IntegrityError:
                messages.error(request, "A post with this slug already exists."
                               " Please try a different title.")
    else:
        form = PostForm()
    posts = Post.objects.all()

    return render(request, 'content_management/post_form.html',
                  {'form': form, 'posts': posts})


class PostUpdateView(generic.UpdateView):
    """
    View for updating a Post object. Uses PostForm for data input and
    renders 'content_management/post_form.html' template. Handles form
    validation, slug generation, and displays success or error messages
    accordingly. Redirects to 'add_post' upon successful update.
    """
    model = Post
    form_class = PostForm
    template_name = 'content_management/post_form.html'
    success_url = reverse_lazy('add_post')

    def get_object(self):
        return get_object_or_404(Post, slug=self.kwargs['slug'])

    def form_valid(self, form):
        post = form.save(commit=False)
        if not post.slug or post.slug != slugify(post.title):
            post.slug = slugify(post.title)

        try:
            post.save()
            messages.success(self.request, "Post updated successfully.")
            return super().form_valid(form)

        except IntegrityError:
            messages.error(self.request,
                           "A post with this slug already exists."
                           "Please try a different title.")
            return self.form_invalid(form)


class PostDeleteView(View):
    """
    View to delete a Post.

    Allows authorized users (post author or staff) to delete
    a specific Post object. If the user is not authorized,
    an error message is displayed. Redirects to the 'add_post'
    page after deletion.

    Methods:
        get(self, request, slug, post_id):
            Handles GET requests to delete a Post.
            Retrieves the Post object based on slug and post_id.
            Deletes the Post if the requesting user is the author
            or staff. Displays success message upon successful deletion.
            Redirects to 'add_post' view after deletion.

    Usage:
        This view should be used to handle deletion of Post objects
        by authorized users.
    """
    def get(self, request, slug, post_id):
        post = get_object_or_404(Post, slug=slug, id=post_id)
        if post.author == request.user or request.user.is_staff:
            post.delete()
            messages.success(request, 'Post deleted successfully!')
        else:
            messages.error(request,
                           'You are not authorized to delete this post!')
        return HttpResponseRedirect(reverse('add_post'))
