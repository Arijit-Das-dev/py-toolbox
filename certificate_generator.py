from tkinter import *
import cv2
from PIL import Image, ImageTk

class VideoBackgroundApp:
    
    def __init__(self, root, video_path):
        self.root = root
        self.root.title("Certify")
        self.root.geometry("800x600")

        self.cap = cv2.VideoCapture(video_path)

        # Background label for video
        self.bg_label = Label(root)
        self.bg_label.pack(fill="both", expand=True)

        self.play_video()

    def play_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (800, 600))
            frame = cv2.GaussianBlur(frame, (25, 25), 0)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.bg_label.config(image=img)
            self.bg_label.image = img

            self.root.after(30, self.play_video)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            self.play_video()

if __name__ == "__main__":
    root1 = Tk()

    #First load the video background
    app = VideoBackgroundApp(root1, r"C:\Users\abijit\Downloads\19800595-hd_1920_1080_25fps.mp4")

    #Then add your text on top

    text1 = Label(root1,
                 text="Welcome to Certify",
                 fg="white",
                 bg="#3D75B5",
                 relief=RAISED,
                 font=("calibri", 25, "bold"))
    text1.place(relx=0.5, rely=0.1, anchor='center')

    text2 = Label(root1,
                  text='Generate your certificate !',
                  fg='white',
                  bg="#578BC7",
                  font=('calibri',13,'bold') 
                  )
    text2.place(x=300, y=90)

    #textBox1
    textBox1 = Entry(root1,
                    font=('arial',9, 'bold'),
                    fg='Black',
                    background="#83B8F4"
                    )
    textBox1.insert(0,' Enter your name')
    textBox1.place(x=320, y=250)

    #textBox2
    textBox2 = Entry(root1,
                    font=('arial',9, 'bold'),
                    fg='Black',
                    background="#83B8F4"
                    )
    textBox2.insert(0,' Enter course start date')
    textBox2.place(x=320, y=290)

    #textBox3
    textBox3 = Entry(root1,
                    font=('arial',9, 'bold'),
                    fg='Black',
                    background="#83B8F4"
                    )
    textBox3.insert(0,' Enter course End date')
    textBox3.place(x=320, y=330)

    #textBox4
    textBox4 = Entry(root1,
                    font=('arial',9, 'bold'),
                    fg='Black',
                    background="#83B8F4"
                    )
    textBox4.insert(0,' Enter course title')
    textBox4.place(x=320, y=370)

    def delete_all():

        textBox1.delete(0, END)
        textBox2.delete(0, END)
        textBox3.delete(0, END)
        textBox4.delete(0, END)
    
    button_refresh = Button(root1,
                     text='REFRESH',
                     font=('arial',8,'bold'),
                     fg='black',
                     command=delete_all,
                     background='#A8C9ED',
                     activebackground="#0C6FE1",
                    )
    button_refresh.place(x=395, y=400)

    def submit_all():

        box1 = textBox1.get()
        box2 = textBox2.get()
        box3 = textBox3.get()
        box4 = textBox4.get()

        image = cv2.imread("C:\\Users\\abijit\\Documents\\Certificate_Image.jpg")

        if image is not None:

            
            cv2.putText(image, box1, (125,450), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 0),1)
            cv2.putText(image, box2, (125,295), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),1)
            cv2.putText(image, box3, (125,320), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 0),1)
            cv2.putText(image, box4, (125,530), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 0),2)
            cv2.putText(image, 'Course', (125,510), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 0),2)

            cv2.imshow("Certificate",image)
            cv2.waitKey()
            cv2.destroyAllWindows()
        
        else:
            print("Error")

    button_submit = Button(root1,
                    text='SUBMIT',
                     font=('arial',8,'bold'),
                     fg='black',
                     command=submit_all,
                     background="#A8C9ED",
                     activebackground="#0C6FE1",
                    )
    
    button_submit.place(x=340, y=400)
    
    disclaimer_label = Label(root1,
                            text='@ 2025 C e r t i f y App | Designed by - Arijit Das',
                            fg="black",
                            bg="#AFC0D3",
                            border=2,
                            relief=RAISED,
                            font=("calibri", 10, "bold"),
                            anchor="center"
                            )
    disclaimer_label.place(x=20, y=560)

    disclaimer_label = Label(root1,
                            text='Need Help ? Contact No : 6289449233 || email : @arijitdas.das99@gmail.com',
                            fg="black",
                            bg="#AFC0D3",
                            border=2,
                            relief=RAISED,
                            font=("calibri", 10, "bold"),
                            anchor="center"
                            )
    disclaimer_label.place(x=20, y=530)

    root1.mainloop()