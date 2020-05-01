import tkinter as tk
from pydes import des


class Caesar:
    def __init__(self):
        self.cipher = ""
        self.text = ""
        self.alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 

    def Index_of(self,character):
        for i in range(0,26):
            if character == self.alphabet[i]:
                return i
        return None    
    
    def encrypt(self,message,displacement = 3):
        message = message.lower()
        message = message.replace(" ","")
        for i in range(0,len(message)):
            index = self.Index_of(message[i])
            if (index+displacement) >= 26:
                index = (index + displacement) - 26
            else:
                index = index + displacement
            self.cipher = self.cipher + str(self.alphabet[index])
        return self.cipher
    
    def decrypt(self,cipher,displacement = 3):
        for i in range(0,len(cipher)):
            index = self.Index_of(cipher[i])
            if (index - displacement) < 0:
                index = (index - displacement) + 26
            else:
                index = index - displacement
            self.text = self.text + str(self.alphabet[index])
        return self.text

class PlayFair:
    def __init__(self,keyword):
        self.keyword = keyword
        self.keyword = self.keyword.lower()
        self.keyword = self.keyword.replace(" ","")

        self.arr = self.mat_create(5,5)      #matrix creation

        self.a = 0                      #temporary variables
        self.flag = 0
        
        self.alphabet = list("abcdefghijklmnopqrstuvwxyz") #removnig
        self.alphabet.reverse()
        for i in self.keyword:
            if i in self.alphabet:
                self.alphabet.remove(i) 
        
        for i in range(0,5):            #insertion of the keyword into the matrix
            for j in range(0,5):
                self.arr[i][j] = self.keyword[self.a]
                self.a += 1
                if(j > 4):
                    break
                elif(self.a >= len(self.keyword)):
                    self.flag = 1
                    break   
            if self.flag == 1:
                self.flag = 0
                j += 1
                break
        
        if 'i' in self.alphabet and 'j' in self.alphabet:            #resolving i and j
            self.alphabet.remove('j')
        elif 'i' not in self.alphabet and 'j' in self.alphabet:
            self.alphabet.remove('j')
        elif 'j' not in self.alphabet and 'i' in self.alphabet:
            self.alphabet.remove('i')
            self.flag = 1
        elif 'i' in self.alphabet and 'j' in self.alphabet:
            print("Error! (Choose a key that does not have i and j together)")
                             
        for i in range(0,5):                   #character insertions
            for j in range(0,5):
                if self.arr[i][j] == 0:
                    self.arr[i][j] = self.alphabet.pop()

    def mat_create(self,rows,cols):
        return [[0 for i in range(cols)] for j in range(rows)]
    
    def print_matrix(self):
        for rows in self.arr:
            print(rows)

    def encrypt(self,word):      #return string
        word = word.replace(" ","")
        word = word.lower()
        word = list(word)
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0
        temp = 0
        letter = "0"
        cipher = list()

        self.a = 0 
        for i in range(len(word)-1):       #counter
            if word[i] == word[i+1]:
                self.a += 1
        
        for i in range(len(word) + self.a - 1):
            if word[i] == word[i+1]:
                word.insert(i+1,"x")

        if len(word)%2 == 1:               #counter for odd even numbers
            word.append("x")

        word.reverse()

        for num in range(int(len(word)/2)):
            letter = word.pop()

            for i in range(5):
                for j in range(5):
                    if self.arr[i][j] == letter:
                        self.i = i
                        self.j = j
                        break
            
            letter = word.pop()

            for k in range(5):
                for l in range(5):
                    if self.arr[k][l] == letter:
                        self.k = k
                        self.l = l
                        break

            if self.j == self.l and self.i != self.k:                   #same column
                self.i += 1
                self.k += 1
                if self.i == 5:
                    self.i -= 5
                elif self.k == 5:
                    self.k -= 5
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

            elif self.i == self.k and self.j != self.l:                  #same row
                self.j += 1
                self.l += 1
                if self.j == 5:
                    self.j -= 5
                elif self.l == 5:
                    self.l -= 5
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

            else:
                temp = self.j
                self.j = self.l
                self.l = temp
                cipher.append(self.arr[self.i][self.j])
                cipher.append(self.arr[self.k][self.l])

        return("".join(cipher))          
    
    def decrypt(self,cipher):                            #not operational
        cipher = cipher.replace(" ","")
        cipher = cipher.lower()
        cipher = list(cipher)
        cipher.reverse()
        self.i = 0
        self.j = 0
        self.k = 0
        self.l = 0
        temp = 0
        letter = "0"
        message = list()

        for num in range(int(len(cipher)/2)):
            letter = cipher.pop()

            for i in range(5):       #first alphabet
                for j in range(5):
                    if self.arr[i][j] == letter:
                        self.i = i
                        self.j = j
                        break
            
            letter = cipher.pop()

            for k in range(5):          #second alphabet
                for l in range(5):
                    if self.arr[k][l] == letter:
                        self.k = k
                        self.l = l
                        break

            if self.j == self.l and self.i != self.k:                   #same column
                self.i -= 1
                self.k -= 1
                if self.i == -1:
                    self.i += 5
                elif self.k == -1:
                    self.k += 5
                message.append(self.arr[self.i][self.j])
                message.append(self.arr[self.k][self.l])

            elif self.i == self.k and self.j != self.l:                  #same row
                self.j -= 1
                self.l -= 1
                if self.j == -1:
                    self.j += 5
                elif self.l == -1:
                    self.l += 5
                message.append(self.arr[self.i][self.j])
                message.append(self.arr[self.k][self.l])

            else:
                temp = self.j
                self.j = self.l
                self.l = temp
                message.append(self.arr[self.i][self.j])
                message.append(self.arr[self.k][self.l])

        return("".join(message))  

def CaesarED(num,mess,key):
    instance = Caesar()
    if num == 1:
        cipher = instance.encrypt(mess,key)
        cipher = 'The Calculated Cipher is : ' + cipher
        Result = tk.Label(E_Result,text=cipher)
        Result.pack(side='top')
    if num == 2:
        message = instance.decrypt(mess,key)
        message = 'The Calculated Message is : '+ message
        dResult = tk.Label(D_Result,text=message)
        dResult.pack(side='top')

def Choice_Caesar():
    
    for widget in Selected.winfo_children():
        widget.destroy()

    for widget in E_Name_Fr.winfo_children():
        widget.destroy()

    for widget in D_Name_Fr.winfo_children():
        widget.destroy()

    for widget in E_K_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_K_Inp.winfo_children():
        widget.destroy()

    for widget in D_K_Disp.winfo_children():
        widget.destroy()

    for widget in D_K_Inp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Inp.winfo_children():
        widget.destroy()

    for widget in D_M_Disp.winfo_children():
        widget.destroy()
        
    for widget in D_M_Inp.winfo_children():
        widget.destroy()

    for widget in E_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in D_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in E_Result.winfo_children():
        widget.destroy()
    
    for widget in D_Result.winfo_children():
        widget.destroy()

    status = tk.Label(Selected, text='The Selected Algorithm is : Caesar Cipher')
    status.pack(side='top')
    
    Encryption_Head = tk.Label(E_Name_Fr,text='Encrypt Message (Caesar Cipher)')
    Encryption_Head.pack(side='top')

    Decription_Head = tk.Label(D_Name_Fr,text='Decrypt Message (Caesar Cipher)')
    Decription_Head.pack(side='top')

    E_Key = tk.Label(E_K_Disp, text='Enter the key/displacement')
    E_Mess = tk.Label(E_M_Disp, text='Enter the Message')
    Inp_Key = tk.Entry(E_K_Inp)
    Inp_Message = tk.Entry(E_M_Inp)

    E_Key.pack(side='right')
    E_Mess.pack(side='right')
    Inp_Key.pack(side='left')
    Inp_Message.pack(side='left')

    D_Key = tk.Label(D_K_Disp, text='Enter the key/displacement')
    D_Mess = tk.Label(D_M_Disp, text='Enter the Cipher')
    D_InpKey = tk.Entry(D_K_Inp)
    D_InpMessage = tk.Entry(D_M_Inp)

    D_Key.pack(side='right')
    D_Mess.pack(side='right')
    D_InpKey.pack(side='left')
    D_InpMessage.pack(side='left')

    E_Submit = tk.Button(E_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: CaesarED(1,Inp_Message.get(),int(Inp_Key.get())))
    E_Submit.pack(side='top')
    D_Submit = tk.Button(D_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: CaesarED(2,D_InpMessage.get(),int(D_InpKey.get())))
    D_Submit.pack(side='top')

def PlayFairED(num,mess,key):
    pf = PlayFair(key)
    if num == 1:
        cipher = pf.encrypt(mess)
        cipher = 'The Calculated Cipher is : ' + cipher
        Result = tk.Label(E_Result,text=cipher)
        Result.pack(side='top')
    if num == 2:
        message = pf.decrypt(mess)
        message = 'The Calculated Message is : '+ message
        dResult = tk.Label(D_Result,text=message)
        dResult.pack(side='top')

def Choice_PlayFair():

    for widget in Selected.winfo_children():
        widget.destroy()

    for widget in E_Name_Fr.winfo_children():
        widget.destroy()

    for widget in D_Name_Fr.winfo_children():
        widget.destroy()

    for widget in E_K_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_K_Inp.winfo_children():
        widget.destroy()

    for widget in D_K_Disp.winfo_children():
        widget.destroy()

    for widget in D_K_Inp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Inp.winfo_children():
        widget.destroy()

    for widget in D_M_Disp.winfo_children():
        widget.destroy()
        
    for widget in D_M_Inp.winfo_children():
        widget.destroy()

    for widget in E_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in D_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in E_Result.winfo_children():
        widget.destroy()
    
    for widget in D_Result.winfo_children():
        widget.destroy()

    status = tk.Label(Selected, text='The Selected Algorithm is : PlayFair Cipher')
    status.pack(side='top')
    
    Encryption_Head = tk.Label(E_Name_Fr,text='Encrypt Message (PlayFair Cipher)')
    Encryption_Head.pack(side='left')

    Decription_Head = tk.Label(D_Name_Fr,text='Decrypts Message (Playfair Cipher)')
    Decription_Head.pack(side='left')

    E_Key = tk.Label(E_K_Disp, text='Enter the key')
    E_Mess = tk.Label(E_M_Disp, text='Enter the Message')
    Inp_Key = tk.Entry(E_K_Inp)
    Inp_Message = tk.Entry(E_M_Inp)

    E_Key.pack(side='right')
    E_Mess.pack(side='right')
    Inp_Key.pack(side='left')
    Inp_Message.pack(side='left')

    D_Key = tk.Label(D_K_Disp, text='Enter the key')
    D_Mess = tk.Label(D_M_Disp, text='Enter the Cipher')
    D_InpKey = tk.Entry(D_K_Inp)
    D_InpMessage = tk.Entry(D_M_Inp)

    D_Key.pack(side='right')
    D_Mess.pack(side='right')
    D_InpKey.pack(side='left')
    D_InpMessage.pack(side='left')

    E_Submit = tk.Button(E_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: PlayFairED(1,Inp_Message.get(),Inp_Key.get()))
    E_Submit.pack(side='top')
    D_Submit = tk.Button(D_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: PlayFairED(2,D_InpMessage.get(),D_InpKey.get()))
    D_Submit.pack(side='top')

def DES_ED(num,key,mess):
    d = des()
    if num == 1:
        cipher = d.encrypt(key,mess,padding=True)
        cipher = 'The Calculated Cipher is : ' + cipher
        Result = tk.Label(E_Result,text=cipher)
        Result.pack(side='top')
    if num == 2:
        message = d.decrypt(key,mess,padding=True)
        message = 'The Calculated Message is : '+ message
        dResult = tk.Label(D_Result,text=message)
        dResult.pack(side='top')

def Choice_DES():

    for widget in Selected.winfo_children():
        widget.destroy()

    for widget in E_Name_Fr.winfo_children():
        widget.destroy()

    for widget in D_Name_Fr.winfo_children():
        widget.destroy()

    for widget in E_K_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_K_Inp.winfo_children():
        widget.destroy()

    for widget in D_K_Disp.winfo_children():
        widget.destroy()

    for widget in D_K_Inp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Disp.winfo_children():
        widget.destroy()
    
    for widget in E_M_Inp.winfo_children():
        widget.destroy()

    for widget in D_M_Disp.winfo_children():
        widget.destroy()
        
    for widget in D_M_Inp.winfo_children():
        widget.destroy()

    for widget in E_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in D_Submit_Fr.winfo_children():
        widget.destroy()
    
    for widget in E_Result.winfo_children():
        widget.destroy()
    
    for widget in D_Result.winfo_children():
        widget.destroy()

    status = tk.Label(Selected, text='The Selected Algorithm is : Data Encryption Standard')
    status.pack(side='top')
    
    Encryption_Head = tk.Label(E_Name_Fr,text='Encrypt Message (Data Encryption Standard)')
    Encryption_Head.pack(side='left')

    Decription_Head = tk.Label(D_Name_Fr,text='Decrypts Message (Data Encryption Standard)')
    Decription_Head.pack(side='left')

    E_Key = tk.Label(E_K_Disp, text='Enter the key(8 letter keys)')
    E_Mess = tk.Label(E_M_Disp, text='Enter the Message')
    Inp_Key = tk.Entry(E_K_Inp)
    Inp_Message = tk.Entry(E_M_Inp)

    E_Key.pack(side='right')
    E_Mess.pack(side='right')
    Inp_Key.pack(side='left')
    Inp_Message.pack(side='left')

    D_Key = tk.Label(D_K_Disp, text='Enter the key(8 letter keys)')
    D_Mess = tk.Label(D_M_Disp, text='Enter the Cipher')
    D_InpKey = tk.Entry(D_K_Inp)
    D_InpMessage = tk.Entry(D_M_Inp)

    D_Key.pack(side='right')
    D_Mess.pack(side='right')
    D_InpKey.pack(side='left')
    D_InpMessage.pack(side='left')

    E_Submit = tk.Button(E_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: DES_ED(1,Inp_Key.get(),Inp_Message.get()))
    E_Submit.pack(side='top')
    D_Submit = tk.Button(D_Submit_Fr,text='Submit',padx=150,pady=15,command= lambda: DES_ED(2,D_InpKey.get(),D_InpMessage.get()))
    D_Submit.pack(side='top')

gui = tk.Tk()
gui.iconbitmap(r'favicon.ico')
gui.title("Information Security Software")
gui.geometry("1400x660")

#creating all frames

Center = tk.Frame(gui, bg="white")
Center.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)

Selected = tk.Frame(Center, bg="pink")
Selected.place(relx=0.352,rely=0.14,relwidth=0.3,relheight=0.08)

E_Name_Fr = tk.Frame(Center, bg="pink")     
E_Name_Fr.place(relx=0.1,rely=0.3,relwidth=0.35,relheight=0.08)

D_Name_Fr = tk.Frame(Center, bg="pink")
D_Name_Fr.place(relx=0.57,rely=0.3,relwidth=0.35,relheight=0.08)

E_K_Disp = tk.Frame(Center, bg='red')
E_K_Disp.place(relx=0.1,rely=0.4,relwidth=0.172,relheight=0.08)

E_M_Disp = tk.Frame(Center, bg='red')
E_M_Disp.place(relx=0.1,rely=0.5,relwidth=0.172,relheight=0.08)

E_K_Inp = tk.Frame(Center, bg='red')
E_K_Inp.place(relx=0.275,rely=0.4,relwidth=0.172,relheight=0.08)

E_M_Inp = tk.Frame(Center, bg='red')
E_M_Inp.place(relx=0.275,rely=0.5,relwidth=0.172,relheight=0.08)

D_K_Disp = tk.Frame(Center, bg='red')
D_K_Disp.place(relx=0.57,rely=0.4,relwidth=0.172,relheight=0.08)

D_M_Disp = tk.Frame(Center, bg='red')
D_M_Disp.place(relx=0.57,rely=0.5,relwidth=0.172,relheight=0.08)

D_K_Inp = tk.Frame(Center, bg='red')
D_K_Inp.place(relx=0.745,rely=0.4,relwidth=0.172,relheight=0.08)

D_M_Inp = tk.Frame(Center, bg='red')
D_M_Inp.place(relx=0.745,rely=0.5,relwidth=0.172,relheight=0.08)

E_Submit_Fr = tk.Frame(Center, bg= 'red')
E_Submit_Fr.place(relx=0.1,rely=0.6,relwidth=0.35,relheight=0.08)
D_Submit_Fr = tk.Frame(Center, bg = 'red')
D_Submit_Fr.place(relx=0.57,rely=0.6,relwidth=0.35,relheight=0.08)

E_Result = tk.Frame(Center, bg='pink')
E_Result.place(relx=0.1, rely=0.7, relwidth=0.35, relheight=0.2)

D_Result = tk.Frame(Center, bg='pink')
D_Result.place(relx=0.57, rely=0.7, relwidth=0.35, relheight=0.2)

#creation of the algorithm selection buttons
Caesarb = tk.Button(Center,text="Caesar Cipher", activebackground='#ff687e', bg='#943b6d', relief ='ridge',bd=5, padx=120, pady=10, command=Choice_Caesar)
Caesarb.place(relx=0.01, rely=0.01)

PFair = tk.Button(Center,text="Playfair Cipher", bg='#CC6686', bd=5, padx=120, pady=10, command=Choice_PlayFair)
PFair.place(relx=0.37, rely=0.01)

DES = tk.Button(Center,text="Data Encription Standard", bg='#CC6686', bd=5, padx=90, pady=10, command=Choice_DES)
DES.place(relx=0.725, rely=0.01)

gui.mainloop()
