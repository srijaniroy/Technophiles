from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras

# Create your views here.
def blogHome(request): 
    allPosts = Post.objects.all().order_by('-views')
    context = {'allPosts' : allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    post.views= post.views +1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None).order_by('-timestamp')
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by('timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, "blog/blogPost.html", context)



from django.core.exceptions import ObjectDoesNotExist

def postComment(request):
    if request.method == "POST":
        comment_text = request.POST.get('comment')
        user = request.user
        post_sno = request.POST.get('postSno')
        post = Post.objects.get(sno=post_sno)
        parent_sno = request.POST.get('parentSno')

        # Debugging output
        print(f"Parent Sno: {parent_sno}")  # For debugging

        if parent_sno is not None and parent_sno.strip() != "":
            # Try to convert parent_sno to an integer
            try:
                parent_sno = int(parent_sno)
            except ValueError:
                messages.error(request, "Invalid parent comment reference.")
                return redirect(f"/blog/{post.slug}")

        if parent_sno is None:
            # Post a new comment
            comment = BlogComment(comment=comment_text, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            try:
                # Try to get the parent comment
                parent_comment = BlogComment.objects.get(sno=parent_sno)
                # Post a reply to an existing comment
                reply = BlogComment(comment=comment_text, user=user, post=post, parent=parent_comment)
                reply.save()
                messages.success(request, "Your reply has been posted successfully")
            except ObjectDoesNotExist:
                messages.error(request, f"The parent comment with Sno {parent_sno} does not exist.")

    return redirect(f"/blog/{post.slug}")
