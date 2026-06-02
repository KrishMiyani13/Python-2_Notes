from django.shortcuts import render
from .models import Music
# Create your views here.
def music(request):
    music_records = Music.objects.all()
    if request.method == 'POST':
        song = request.POST.get('song')
        artist = request.POST.get('artist')
        year = request.POST.get('year')
        album = request.POST.get('album')

        if song:
            music_records = music_records. filter(song_icontains=song)
        if artist:
            music_records = music_records.filter(artist_icontains=artist)
        if year:
            music_records = music_records. filter(year_icontains=year)
        if album:
            music_records = music_records.filter(album_icontains=album)

    return render (request,"findmusic/music.html",{'music_records':music_records})
 