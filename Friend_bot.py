# single bot helper chat
import tkinter
from tkinter import*
from tkinter import ttk

root=Tk()
root.title("Friendly Bot")
root.configure(bg="darkgrey")
lab0=Label(root,text="PROTON BOT",font=("arial",16,'bold'),background="blue",foreground="white").grid(row=0,column=1,pady=10)
ent_box=Entry(root,background="lightblue",borderwidth=8,font=("arial",20,'bold'),justify="right")
ent_box.grid(row=1,column=1,ipadx=130,ipady=20,padx=20,pady=20)
blank="""                                                                                               
                                                                                          
                                                                                          
                                                                                             
                                                                                         """
#blank space for new element proper view
lab2=tkinter.Label(root,text=blank,font=40,background="yellow").grid(row=2,column=1,pady=10,ipadx=30,ipady=40)
lab2=tkinter.Label(root,text="""Hi ! I am PROTON your AI friend
                    Please enter a message to start the chat""",font=40,background="yellow").grid(row=2,column=1,pady=10,ipadx=30,ipady=40)

def send():
    lab2=tkinter.Label(root,text=blank,font=40,background="yellow").grid(row=2,column=1,pady=10,ipadx=30,ipady=40)
    x=ent_box.get()
    if "cefibrubreyfr" in x:
        bot="""  ----- yet to be written"""
    
    
    elif "name"and"kunal" in x:
        bot="""  Welcome boss !! I am ready to take orders. 
              KK BOSS. The developer of this Bot. 🫡🙇
                      Salute BOSS """
    elif "what is your name" in x:
        bot="""  My name is proton. the virtual bot. 
                Developed By Kunal 
                founder of KKsoftexh pvt.ltd  """
    elif ("kv"or"KV") in x:
        bot="""   Shit !! One of the most Scam school in India
                  dont ask about it again to me 😡😡"""
    elif "is ai" in x:
        bot=""" AI is latest advanced technology developed by humans
            You can say it one of the most dangerous tech which has 
            the potential to replace its own creator THE HUMAN.
            AI is portrayed as danger by many tech experts considering
            recent rise of the use of deepfakes, etc...  """
    elif "hello" in x:
        bot="""Hello Human! 🥰🥰 I am proton. I can help you.
              You can talk to me if you feel lonely. 😜🤗🫠 
                I can make you feel happy 😃😄"""
    elif "name"and"iman" in x:
        bot="""Hello iman kalyan deuri.. i am you AI slave made
               by your developer friend Kunal dangawala 🧑‍💻"""
    elif "biology" in x:
        bot="""Biology is a branch of science that deals with
              human body and nature things. A very vast subject
              and also very interesting one. 🧑‍🔬"""
    elif "computer science" in x:
        bot=""" Computers are as you know very advanced 
                machines capable of doing various tasks. 
                Even me "PROTON BOT"
                was developed using a computer 💻"""



    elif x=="":
        bot=""" Please enter some message !!!"""
    else:
        bot=""" Sorry ! I couldn't understand your words.😔😅 
                I am still in development stage 🧑‍💻🧑‍💻
                Text me again  🥰 """
    
    
    print("User:-",x)
    print(" Proton bot:- ",bot)
    lab2=tkinter.Label(root,text=bot,font=("arial",14),background="yellow").grid(row=2,column=1,pady=10,ipadx=30,ipady=40)

send=Button(root,text="SEND",bg="red",font=("arial",15,'bold'),borderwidth=8,command=send).grid(row=1,column=2,padx=20)
#lab1=Label(root,text="Hi! I am PROTON. Your AI friend!",font=("arial",16,'bold'),background="blue").grid(row=2,column=1,pady=10)
lab4=Label(root,text=""" ©© KKsoftechz.pvt.ltd   
                        DEVELOPER:- Kunal Kashyap """,font=("arial",12,'bold'),background="blue").grid(row=3,column=1,pady=10)

root.resizable(False,False)
root.geometry("770x468")
root.mainloop()

#  lab2=tkinter.Label(root,text="""    """,font=40).grid(row=3,column=1,pady=10,ipadx=50,ipady=40)

