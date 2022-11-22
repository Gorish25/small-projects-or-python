from pytube import YouTube


# link to be given
link="https://youtu.be/Py5b0f_WFvI"

# giving link to function
youtube1=YouTube(link)


# print title of youtube video
# print(youtube1.title) 


# printing thumbnail url of youtube video
# print(youtube1.thumbnail_url)


# knowing the streaming (pixels) of video and storing it in a string
videos=youtube1.streams.all()
vid=list(enumerate(videos))


# if we want only audio of youtube video
# audio=youtube1.streams.filter(only_audio=True)


# printing the type of pixels
for i in vid:
    print(i)


# asking user to input the stream of video to download
strm=int(input("Enter the quality index to download: "))
videos[strm].download()

print("Successfully downloaded video")