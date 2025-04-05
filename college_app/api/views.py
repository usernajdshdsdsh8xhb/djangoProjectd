
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from college_app.api.models import Post
from college_app.api.serializers import CustomPostSerializer, PostSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status


@api_view()
def posts_list(request):
    posts = Post.objects.filter(acceptorName="")
    serializer = PostSerializer(posts, many=True)
    return Response({"list":serializer.data})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def my_posts_list(request):
    posts_first = Post.objects.filter(posterName=request.user.first_name, )
    posts_second = Post.objects.filter(acceptorName=request.user.first_name, )
    posts = posts_first.union(posts_second)

    serializer = CustomPostSerializer(posts, many=True)
    print(type(serializer.data))
    return Response({"list":serializer.data})
    
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_post(request):
    try:
        name = request.user.first_name
        if (name==""):
            request.data["posterName"] = "NULL"
        else:
            request.data["posterName"] = name
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    except:
        return Response({"message":"An Error Happened"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def accept_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.acceptorName = request.user.first_name
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except:
        return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_post(request, pk):
    try:
        post = Post.objects.filter(pk=pk, posterName = request.user.first_name)
        post.delete()
        return Response({"message":"Deleted Successfully"})
    except:
        return Response({"message":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        