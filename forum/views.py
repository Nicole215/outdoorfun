from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import ForumPost, ForumComment
from .forms import ForumPostForm, ForumCommentForm


def forum_post_list(request):
    """
    Displays a list of all forum posts.
    """
    posts = ForumPost.objects.all()
    return render(request, 'forum/forum_post_list.html', {'posts': posts})


def forum_post_detail(request, slug):
    """
    Displays the details of a specific forum post.
    """
    post = get_object_or_404(ForumPost, slug=slug)
    return render(request, 'forum/forum_post_detail.html', {'post': post})


def add_post(request):
    """
    Handles the creation of a new forum post.

    If the request method is POST, validates the submitted form and saves the
    post with the current user as the author. Otherwise, displays an empty
    form for creating a post.
    """
    if request.method == "POST":
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('forum_post_detail', slug=post.slug)
    else:
        form = ForumPostForm()
    return render(request, 'forum/add_post.html', {'form': form})


def edit_post(request, slug):
    """
    Handles the editing of an existing forum post.

    Only the author of the post can edit it. Displays the edit form for GET
    requests and processes the updated post for POST requests.
    """
    post = get_object_or_404(ForumPost, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        raise Http404("You are not authorized to edit this post.")

    if request.method == "POST":
        form = ForumPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('forum_post_detail', slug=post.slug)
    else:
        form = ForumPostForm(instance=post)
    return render(
        request, 'forum/edit_post.html', {'form': form, 'post': post})


def delete_post(request, slug):
    """
    Handles the deletion of a forum post.

    Only the author of the post can delete it. Displays a confirmation page for
    GET requests and deletes the post for POST requests.
    """
    post = get_object_or_404(ForumPost, slug=slug)

    # Check if the current user is the author of the post
    if post.author != request.user:
        raise Http404("You are not authorized to edit this post.")

    if request.method == "POST":
        post.delete()
        return redirect('forum_post_list')
    return render(request, 'forum/delete_post.html', {'post': post})


# Add a comment
def add_comment(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)

    if request.method == "POST":
        form = ForumCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('forum_post_detail', slug=post.slug)
    else:
        form = ForumCommentForm()
    return render(
        request, 'forum/add_comment.html', {'form': form, 'post': post})


# Edit a comment
def edit_comment(request, comment_id):
    comment = get_object_or_404(ForumComment, id=comment_id)

    # Check if the current user is the author of the comment
    if comment.author != request.user:
        raise Http404("You are not authorized to edit this comment.")

    if request.method == "POST":
        form = ForumCommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('forum_post_detail', slug=comment.post.slug)
    else:
        form = ForumCommentForm(instance=comment)
    return render(
        request, 'forum/edit_comment.html', {'form': form, 'comment': comment})


# Delete a comment
def delete_comment(request, comment_id):
    comment = get_object_or_404(ForumComment, id=comment_id)

    # Check if the current user is the author of the comment
    if comment.author != request.user:
        raise Http404("You are not authorized to delete this comment.")

    if request.method == "POST":
        post_slug = comment.post.slug
        comment.delete()
        return redirect('forum_post_detail', slug=post_slug)
    return render(request, 'forum/delete_comment.html', {'comment': comment})
