from django.shortcuts import render
from core.models import Post
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def post_list(request):
    posts = Post.objects.all()
    post_data = [{"title": p.title, "body": p.body} for p in posts]
    return Response(post_data)
