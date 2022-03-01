from pytube import YouTube

link = input("Enter the URL of your video : ")
name = input("Enter the name of your file : ")
name = name + ".mp4"
yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, file_extension = "mp4").first().download(output_path = "C:\\Users\\adity\\OneDrive\\Desktop\\stuff\\PYTHON\\YouTube",
filename = name)
except:
    print("Some Error!")
print('Task Completed!')
