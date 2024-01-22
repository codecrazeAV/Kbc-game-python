import tkinter as tk
from pygame import mixer

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)
money = 0

def select(event):
    b = event.widget
    value = b['text']

    for i in range(14):
        if value == rightoptions[i]:
            questionArea.delete(1.0, tk.END)
            questionArea.insert(tk.END, qno[i + 1][0])
            optionButton1.config(text=qno[i + 1][1])
            optionButton2.config(text=qno[i + 1][2])
            optionButton3.config(text=qno[i + 1][3])
            optionButton4.config(text=qno[i + 1][4])
            amountLabel.config(image=amountImages[i])
            
        if value == rightoptions[4] or value == rightoptions[9]:
            if value == rightoptions[4]:
                money = 10000
            elif value == rightoptions[9]:
                money = 3202000
            
            root3 = tk.Toplevel()
            root3.grab_set()
            root3.overrideredirect(True)
            root3.config(bg='black')
            root3.geometry('800x200+110+390')
            mixer.music.stop()
            mixer.music.load('won.mp3')
            mixer.music.play()
            winLabel = tk.Label(root3, text=f"Congratulations! You have Won! {money} rupees", bg='black', fg='green',
                             font=('arial', 25, 'bold'))
            winLabel.pack()

            continueButton = tk.Button(root3, text="Continue!", font=('arial', 15, 'bold'), bg='black', fg='blue',
                                    activebackground='black', activeforeground='green', cursor='hand2', bd=0,
                                    command=lambda: [root3.grab_release(),root3.destroy(),mixer.music.load('kbc.mp3'),mixer.music.play()])
            continueButton.pack()

            quitButton = tk.Button(root3, text="Quit the Game!", font=('arial', 15, 'bold'), bg='black', fg='red',
                                activebackground='black', activeforeground='green', cursor='hand2', bd=0,
                                command=lambda: [root3.grab_release(),mixer.music.stop(),root3.destroy(), root.destroy()])
            quitButton.pack()
            if value == rightoptions[4] or value == rightoptions[9]:
                if value == rightoptions[4]:
                    questionArea.delete(1.0, tk.END)
                    questionArea.insert(tk.END, qno[5][0])
                    optionButton1.config(text=qno[5][1])
                    optionButton2.config(text=qno[5][2])
                    optionButton3.config(text=qno[5][3])
                    optionButton4.config(text=qno[5][4])
                    amountLabel.config(image=amountImages[4])
                if value == rightoptions[9]:
                    questionArea.delete(1.0, tk.END)
                    questionArea.insert(tk.END, qno[10][0])
                    optionButton1.config(text=qno[10][1])
                    optionButton2.config(text=qno[10][2])
                    optionButton3.config(text=qno[10][3])
                    optionButton4.config(text=qno[10][4])
                    amountLabel.config(image=amountImages[9])
            root3.wait_window()
            break

        if value not in rightoptions:
            def close():
                root1.grab_release()
                mixer.music.stop()
                root1.destroy()
                root.destroy()

            def tryagain():
                root1.grab_release()
                root1.destroy()
                questionArea.delete(1.0,tk.END)
                questionArea.insert(tk.END,qno[0][0])

                optionButton1.config(text=qno[0][1])
                optionButton2.config(text=qno[0][2])
                optionButton3.config(text=qno[0][3])
                optionButton4.config(text=qno[0][4])

                amountLabel.config(image=amountImage)
                
            root1=tk.Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            imgLabel=tk.Label(root1,image=centerImage,bd=0,height=200,width=303)
            imgLabel.pack(pady=30)

            looseLabel=tk.Label(root1,text="You Lose!",bg='black',fg='brown',font=('arial',25,'bold'))
            looseLabel.pack()

            tryagainButton=tk.Button(root1,text="Try again!",font=('arial',15,'bold'),bg='black',fg='blue',
                                  activebackground='black',activeforeground='green',cursor='hand2',bd=0,command=tryagain)
            tryagainButton.pack()
            closeButton=tk.Button(root1,text="Quit",font=('arial',15,'bold'),bg='black',fg='red',
                                  activebackground='black',activeforeground='green',cursor='hand2',bd=0,command=close)
            closeButton.pack()
            root1.mainloop()
            root1.wait_window()
            break
        if value==rightoptions[14]:
            mixer.music.stop()
            mixer.music.load('won.mp3')
            mixer.music.play()
            money="1 Crore"
            def close():
                root2.grab_release()
                mixer.music.stop()
                root2.destroy()
                root.destroy()

            def tryagain():
                root2.grab_release()
                root2.destroy()
                questionArea.delete(1.0,tk.END)
                questionArea.insert(tk.END,qno[0][0])

                optionButton1.config(text=qno[0][1])
                optionButton2.config(text=qno[0][2])
                optionButton3.config(text=qno[0][3])
                optionButton4.config(text=qno[0][4])
                mixer.music.stop()
                mixer.music.load('kbc.mp3')
                mixer.music.play()

                amountLabel.config(image=amountImage)

            root2=tk.Toplevel()
            root2.grab_set()
            root2.overrideredirect(True)
            root2.config(bg='black')
            root2.geometry('800x400+140+30')
            imgLabel=tk.Label(root2,image=centerImage,bd=0,height=200,width=303)
            imgLabel.pack(pady=30)

            winLabel=tk.Label(root2,text=f" Congratulations! You have Won! {money} rupees!!",bg='black',fg='green',font=('arial',25,'bold'))
            winLabel.pack()

            tryagainButton=tk.Button(root2,text="Try again!",font=('arial',15,'bold'),bg='black',fg='blue',
                                  activebackground='black',activeforeground='green',cursor='hand2',bd=0,command=tryagain)
            tryagainButton.pack()
            closeButton=tk.Button(root2,text="Quit",font=('arial',15,'bold'),bg='black',fg='red',
                                  activebackground='black',activeforeground='green',cursor='hand2',bd=0,command=close)
            closeButton.pack()
            amountLabel.config(image=amountImages[14])
            root2.wait_window()
            break


qno=[["What is the time complexity of quicksort algorithm?", "O(n)", "O(n log n)", "O(n^2)", "O(log n)"],
     ["Which of the following is a Lewis acid?", "HCl", "H2O", "AlCl3", "NH3" ],
     ["Which type of brake is used in automobiles for emergency stopping?", "Disc Brake", "Drum Brake", "Hydraulic Brake", "Air Brake"],
     ["What is the frequency range of Wi-Fi in the 5 GHz band?", "2.4 GHz-2.5 GHz", "5.1 GHz-5.8 GHz", "5.9 GHz-6.4 GHz", "4.9 GHz-5.3 GHz"],
     ["Which unit is used to measure the rate of mass transfer in a distillation column?", "kmol/m²·s", "kg/m²·s", "kmol/s", "kg/s"],
     ["What is the purpose of a yaw damper in an aircraft?", "Control pitch", "Control roll", "Control yaw", "Control thrust"],
     ["Which enzyme is used to amplify DNA in polymerase chain reaction (PCR)?", "DNA ligase", "DNA polymerase", "RNA polymerase", "RNA ligase"],
     ["Which instrument is used to measure pressure in a closed container?", "Manometer", "Barometer", "Hydrometer", "Piezometer"],
     ["What is the primary greenhouse gas responsible for global warming?", "Methane", "Carbon Dioxide", "Nitrous Oxide", "Ozone"],
     ["What is the eigenvalue of the identity matrix?", "1", "0", "-1", "It is not defined"],
     ["In the photoelectric effect, what happens to the kinetic energy of ejected electrons when the frequency of incident light increases?", "Increases", "Decreases", "Remains constant", "Depends on intensity"],
     ["What is the main alloying element in stainless steel?", "Nickel", "Chromium", "Manganese", "Vanadium"],
     ["Which rock type is formed by the solidification of molten magma?", "Sedimentary", "Metamorphic", "Igneous", "Conglomerate"],
     ['What is the primary purpose of a control rod in a nuclear reactor?', 'Generate electricity', 'Absorb neutrons', 'Cool the reactor', 'Regulate pressure'],
     ["Which method is commonly used for underground coal mining?" ,"Surface mining" ,"Room and pillar" ,"Quarrying" ,"Placer mining"]]

rightoptions=["O(n log n)", "AlCl3", "Air Brake", "5.1 GHz-5.8 GHz", "kmol/m²·s", "Control yaw", "DNA polymerase", "Manometer", "Carbon Dioxide", "1", "Increases", "Chromium", "Igneous", "Absorb neutrons",
              "Room and pillar"]

root=tk.Tk()
root.geometry('1490x780+0+0')
root.title('KBC game')
root.config(background='black')
leftframe=tk.Frame(root,bg='black',padx=150)
leftframe.grid(row=0,column=0)

topframe=tk.Frame(leftframe,bg='black',pady=20)
topframe.grid(row=0,column=0)

centerframe=tk.Frame(leftframe,bg='black',pady=20)
centerframe.grid(row=1,column=0)

bottomframe=tk.Frame(leftframe)
bottomframe.grid(row=2,column=0)


rightframe=tk.Frame(root,background='black',bg='black')
rightframe.grid(row=0, column=1, columnspan=2) 

image50=tk.PhotoImage(file='50-50.png')
lifeline50Button=tk.Button(topframe,image=image50,bg='black',bd=0,width=180,height=80,activebackground='black')
lifeline50Button.grid(row=0,column=0)

audiencePole=tk.PhotoImage(file='audiencePole.png')
audiencePoleButton=tk.Button(topframe,image=audiencePole,bg='black',bd=0,width=180,height=80,activebackground='black')
audiencePoleButton.grid(row=0,column=1)

phoneImage=tk.PhotoImage(file='phoneAFriend.png')
phoneImageButton=tk.Button(topframe,image=phoneImage,bg='black',bd=0,width=180,height=80,activebackground='black')
phoneImageButton.grid(row=0,column=2)

centerImage=tk.PhotoImage(file='ce.png')
logoLabel=tk.Label(centerframe,image=centerImage,bg='black')
logoLabel.grid(row=0,column=0)

amountImage=tk.PhotoImage(file='amt.png')
amountImage1=tk.PhotoImage(file='amt1.png')
amountImage3=tk.PhotoImage(file='amt3.png')
amountImage2=tk.PhotoImage(file='amt2.png')
amountImage4=tk.PhotoImage(file='amt4.png')
amountImage5=tk.PhotoImage(file='amt5.png')
amountImage6=tk.PhotoImage(file='amt6.png')
amountImage7=tk.PhotoImage(file='amt7.png')
amountImage8=tk.PhotoImage(file='amt8.png')
amountImage9=tk.PhotoImage(file='amt9.png')
amountImage10=tk.PhotoImage(file='amt10.png')
amountImage11=tk.PhotoImage(file='amt11.png')
amountImage12=tk.PhotoImage(file='amt12.png')
amountImage13=tk.PhotoImage(file='amt13.png')
amountImage14=tk.PhotoImage(file='amt14.png')
amountImage15=tk.PhotoImage(file='amt15.png')

amountImages=[amountImage1,amountImage2,amountImage3,amountImage4,amountImage5,
              amountImage6,amountImage7,amountImage8,amountImage9,amountImage10,amountImage11,
              amountImage12,amountImage13,amountImage14,amountImage15]

amountLabel=tk.Label(rightframe,image=amountImage,bg='black')
amountLabel.grid(row=0, column=1, sticky="e",padx=120)  # Place in column 1, stick to right

layoutimage=tk.PhotoImage(file='lay.png')
layoutLabel=tk.Label(bottomframe,image=layoutimage,bg='black')
layoutLabel.grid(row=0,column=0)

questionArea=tk.Text(bottomframe,font=('arial',15,'bold'),width=38,height=2,wrap='word',fg='white',bg='black',bd=0)
questionArea.place(x=75,y=14)
questionArea.insert(tk.END,qno[0][0])

labelA=tk.Label(bottomframe,text='A:',bg='black',fg='white',font=('arial',13,'bold'))
labelA.place(x=60,y=110)

labelB=tk.Label(bottomframe,text='B:',bg='black',fg='white',font=('arial',13,'bold'))
labelB.place(x=340,y=110)

labelC=tk.Label(bottomframe,text='C:',bg='black',fg='white',font=('arial',13,'bold'))
labelC.place(x=60,y=190)

labelD=tk.Label(bottomframe,text='D:',bg='black',fg='white',font=('arial',13,'bold'))
labelD.place(x=330,y=190)

optionButton1=tk.Button(bottomframe,text=qno[0][1],bg='black',bd=0,font=('arial',15,'bold'),
                     fg='white',activebackground='black',activeforeground='orange',cursor='hand2')
optionButton1.place(x=90,y=103)

optionButton2=tk.Button(bottomframe,text=qno[0][2],bg='black',bd=0,font=('arial',15,'bold'),
                     fg='white',activebackground='black',activeforeground='orange',cursor='hand2')
optionButton2.place(x=370,y=103)

optionButton3=tk.Button(bottomframe,text=qno[0][3],bg='black',bd=0,font=('arial',15,'bold'),
                     fg='white',activebackground='black',activeforeground='orange',cursor='hand2')
optionButton3.place(x=90,y=182)

optionButton4=tk.Button(bottomframe,text=qno[0][4],bg='black',bd=0,font=('arial',15,'bold'),
                     fg='white',activebackground='black',activeforeground='orange',cursor='hand2')
optionButton4.place(x=370,y=182)

optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)
root.mainloop(-1)

