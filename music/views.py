#from django.http import HttpResponse
#from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Album, Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class IndexView(generic.ListView):
     template_name = 'music/index.htm'
     context_object_name = 'all_albums'

     def get_queryset(self):
          return Album.objects.all()


class DetailView(generic.DetailView):
     model = Album
     template_name = 'music/detail.htm'


class AlbumCreate(CreateView):
     model = Album
     template_name = 'music/album_form.htm'
     fields = ['artist', 'album_title', 'genre']


class UserFormView(View):
     form_class = UserForm
     template_name = 'music/registration_form.htm'

     def get(self, request):
          form = self.form_class(None)
          return render(request, self.template_name, {'form': form})


     def post(self, request):
          form = self.form_class(request.POST)

          if form.is_valid():
               user = form.save(commit=False)

               username = form.cleaned_data['username']
               password = form.cleaned_data['password']
               user.set_password(password)
               user.save()

               user = authenticate(username=username, password=password)

               if user is not None:
                    if user.is_active:
                         login(request, user)
                         return redirect('index')
          return render(request, self.template_name, {'form': form})



































# Create your views here.
#def index(request):
#     all_albums = Album.objects.all()
#     return render(request, 'music/index.htm', {'all_albums': all_albums})
#
#def detail(request, album_id):
#    album = get_object_or_404(Album, pk=album_id)
#    return render(request, 'music/detail.htm', {'album': album})

#def favorite (request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#          selected_song = album.song_set.get(pk=request.POST['song'])
#     except(KeyError, SongDoesNotExist):
#          return render(request, '/music/detail.htm', {
#               'album': album,
#               'error_message': "You did not select a valid message"
#          })
#     else:
#          selected_song.is_favorite = True
#          selected_song.save()
#          return render(request, 'music/detail.htm', {'album': album})


 #html = ''
    # for album in all_albums:
   #      url = '/music/' + str(album.id) + ''
  #       html += '<a href="' + url + '">' + album.album_title + '</a><br>'
  #try:
   #     album = Album.objects.get(pk=album_id)
 #   except Album.DoesNotExist:
  #      raise Http404("Album does not exist")