from pytube import YouTube


while True:
    link = input("Enter youtube link: ")
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Views: ", yt.views)
    print("Length: ", yt.length)
    print("Rating: ", yt.rating)
    print("File_size: ", yt.streams.get_highest_resolution().filesize)
    


    while True:
    
        confirm_dl = input("\nDownload video? ")
        if confirm_dl.lower() == "y":
            print("Downloading...")
            ys = yt.streams.get_highest_resolution()
            ys.download('D:/Python/Py_Youtube')     #('Desktop/Youtube')
            print("Download complete")
            break

        elif confirm_dl.lower() == "n":
            break

        else:
            print(confirm_dl)
