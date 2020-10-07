# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MovieModel
# from .serializers import MovieSerializer


# class MovieView(APIView):
#     def get(self, request, *args, **kwargs):
#         movie = MovieModel.objects.all()
#         data = MovieSerializer(movie, many=True).data
#         return Response(data, status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         serializer=MovieSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import MovieSerializer
from .models import MovieModel


class MovieView(ListCreateAPIView):
    serializer_class = MovieSerializer

    # queryset = MovieModel.objects.all()

    def get_queryset(self):
        req = self.request
        qs = MovieModel.objects.all()
        query = req.query_params.get('filter')
        if query:
            return qs.filter(title__icontains=query)
        return qs


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()
