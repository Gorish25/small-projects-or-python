from pytube import Playlist


# playlist data url
py=Playlist("https://www.youtube.com/playlist?list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l")


# printing playlist title name
print(py.title)