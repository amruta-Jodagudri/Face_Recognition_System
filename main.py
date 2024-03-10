from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recgnition System")

        # first Image
        img1=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\image1.jpg")
        img1 = img1.resize((450, 130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=450,height=130)


        # second Image
        img2=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\image2top.jpeg")
        img2 = img2.resize((500, 130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=450,y=0,width=500,height=130)


        # third Image
        img3=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\img3.jpeg")
        img3 = img3.resize((450, 130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=950,y=0,width=450,height=130)


        # bg Image
        img4=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\bg3.webp")
        img4 = img4.resize((1380,660))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1380,height=660)

        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1380,height=45)


        # Student Details
        img5=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\student.jpg")
        img5 = img5.resize((180,180))
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=140,y=80,width=180,height=180)

        b1_1=Button(bg_img,text="STUDENT DETAILS",cursor="hand2",font=("times new roman",13,"bold"),bg="skyblue",fg="red")
        b1_1.place(x=140,y=260,width=180,height=40)


        # Face Recognise
        img6=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\face.jpeg")
        img6 = img6.resize((180,180))
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b2.place(x=440,y=80,width=180,height=180)

        b2_1=Button(bg_img,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",13,"bold"),bg="skyblue",fg="red")
        b2_1.place(x=440,y=260,width=180,height=40)

        # attedance face button
        img7=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\Attedance.jpeg")
        img7 = img7.resize((180,180))
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=740,y=80,width=180,height=180)

        b3_1=Button(bg_img,text="ATTENDANCE",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b3_1.place(x=740,y=260,width=180,height=40)

        # help face button
        img8=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\help.jpeg")
        img8 = img8.resize((180,180))
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1040,y=80,width=180,height=180)

        b4_1=Button(bg_img,text="HELP",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b4_1.place(x=1040,y=260,width=180,height=40)

        # Train face button
        img9=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\train.jpeg")
        img9 = img9.resize((180,180))
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b5.place(x=140,y=330,width=180,height=180)

        b5_1=Button(bg_img,text="TRAIN DATA",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b5_1.place(x=140,y=510,width=180,height=40)

        # Photos face button
        img10=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\phots.jpeg")
        img10 = img10.resize((180,180))
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b6.place(x=440,y=330,width=180,height=180)

        b6_1=Button(bg_img,text="PHOTOS",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b6_1.place(x=440,y=510,width=180,height=40)


        # Developer face button
        img11=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\develop.jpeg")
        img11 = img11.resize((180,180))
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=740,y=330,width=180,height=180)

        b7_1=Button(bg_img,text="DEVELOPER",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b7_1.place(x=740,y=510,width=180,height=40)

        # Exit face button
        img12=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\exit.jpeg")
        img12 = img12.resize((180,180))
        self.photoimg12=ImageTk.PhotoImage(img12)

        b8=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b8.place(x=1040,y=330,width=180,height=180)

        b8_1=Button(bg_img,text="EXIT",cursor="hand2",font=("times new roman",15,"bold"),bg="skyblue",fg="red")
        b8_1.place(x=1040,y=510,width=180,height=40)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()









