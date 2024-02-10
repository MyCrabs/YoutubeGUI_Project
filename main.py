import tkinter
import customtkinter
from pytube import YouTube
from PIL import Image, ImageTk

def startDownload():
    try:
        ytLink = link.get()
        yt = YouTube(ytLink, on_progress_callback= on_progress)
        ytVideo = yt.streams.get_highest_resolution() 
        ytVideo.download(r"C:\Users\ADMIN\Videos") 
        finish_label.configure(text = "Download Complete")
    except:
        finish_label.configure(text = "Invalid Link", text_color = "red")

def on_progress(stream, chunk, byte_remaining):
    total_size = stream.filesize
    byte_downloaded = total_size - byte_remaining
    per_of_completion = int(byte_downloaded / total_size * 100)
    pPercentage_label.configure(text = f"{per_of_completion} %")
    pPercentage_label.update()
    progressBar.set(float(per_of_completion) / 100)    
    
def Close():
    app.destroy()  



#System setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#Our app frame
app = customtkinter.CTk(fg_color="white")
app.geometry("720x480")
app.title("Youtube Downloader")
image_ = Image.open("Youtube.png")


label = customtkinter.CTkLabel(app, text = "Insert a youtube video link here", font = ("Arial", 16, "bold"))
label.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height= 40, textvariable = url_var )
link.pack()

finish_label = customtkinter.CTkLabel(app, text = "...")
finish_label.pack()

pPercentage_label  = customtkinter.CTkLabel(app, text = "0%")
pPercentage_label.pack()

progressBar = customtkinter.CTkProgressBar(app, width=450, height=10)
progressBar.pack(padx = 10, pady = 10)
progressBar.set(0)

btn_frame = customtkinter.CTkFrame(app, fg_color="white")
btn_frame.pack()

btn  = customtkinter.CTkButton(btn_frame, text= "Click here", command= startDownload)
btn.pack(padx = 10, pady = 10, side = "left")

btnExit = customtkinter.CTkButton(btn_frame, text="Exit", command=  Close, fg_color = "red")
btnExit.pack( side = "right")

#Run app
app.mainloop()

