from tkinter import*
from numpy import*
import numpy as np
from PIL import ImageTk, Image  

class Calc_det:
    
    def __init__(self,root) -> None:

        self.lblTitulo = Label(text="Calcular Determinantes", fg='deeppink4',bg="lightpink2")
        self.lblTitulo["font"] = ("Arial","18",'bold','italic')
        self.lblTitulo.place(x=35,y=10,width=300,height=50)
       
        #SELECIONAR TAMANHO DA MATRIZ
        self.selecionar = IntVar()

        self.selecionar.set(1)
        self.rdFuncao = Radiobutton(text="2x2", value=1, variable=self.selecionar)
        self.rdFuncao.pack()
        self.rdFuncao.place(x=10,y=70, height=30, width=80)
        self.rdFuncao["font"] = ("Arial","12",'bold')
        self.rdFuncao["bg"] = ("lightpink2")
        self.rdFuncao["fg"] = ("deeppink4")
        self.rdFuncao = Radiobutton(text="3x3", value=2, variable=self.selecionar)
        self.rdFuncao.pack()
        self.rdFuncao.place(x=10,y=100, height=30, width=80)
        self.rdFuncao["font"] = ("Arial","12",'bold')
        self.rdFuncao["bg"] = ("lightpink2")
        self.rdFuncao["fg"] = ("deeppink4")
        self.rdFuncao = Radiobutton(text="4x4", value=3, variable=self.selecionar)
        self.rdFuncao.pack()
        self.rdFuncao.place(x=10,y=130, height=30, width=80)
        self.rdFuncao["font"] = ("Arial","12",'bold')
        self.rdFuncao["bg"] = ("lightpink2")
        self.rdFuncao["fg"] = ("deeppink4")
        self.rdFuncao = Radiobutton(text="5x5", value=4, variable=self.selecionar)
        self.rdFuncao.pack()
        self.rdFuncao.place(x=10,y=160, height=30, width=80)
        self.rdFuncao["font"] = ("Arial","12",'bold')
        self.rdFuncao["bg"] = ("lightpink2")
        self.rdFuncao["fg"] = ("deeppink4")
      
        
        #CAMPOS DE ENTRADA Coluna ****1****
        self.e1x1 = Entry()
        self.e1x1.place(x=120, y=70, width=30, height=30)
        self.e1x1["font"] = ("Arial","12","bold")
        self.e1x1["bg"] = ("antiquewhite1")
        self.e1x1["fg"] = ("maroon")

        self.e1x2 = Entry()
        self.e1x2.place(x=120, y=100, width=30, height=30)
        self.e1x2["font"] = ("Arial","12","bold")
        self.e1x2["bg"] = ("antiquewhite1")
        self.e1x2["fg"] = ("maroon")

        self.e1x3 = Entry()
        self.e1x3.place(x=120, y=130, width=30, height=30)
        self.e1x3["font"] = ("Arial","12","bold")
        self.e1x3["bg"] = ("antiquewhite1")
        self.e1x3["fg"] = ("maroon")

        self.e1x4 = Entry()
        self.e1x4.place(x=120, y=160, width=30, height=30)
        self.e1x4["font"] = ("Arial","12","bold")
        self.e1x4["bg"] = ("antiquewhite1")
        self.e1x4["fg"] = ("maroon")

        self.e1x5 = Entry()
        self.e1x5.place(x=120, y=190, width=30, height=30)
        self.e1x5["font"] = ("Arial","12","bold")
        self.e1x5["bg"] = ("antiquewhite1")
        self.e1x5["fg"] = ("maroon")

        #CAMPOS DE ENTRADA coluna  ****2****
        self.e2x1 = Entry()
        self.e2x1.place(x=150, y=70, width=30, height=30)
        self.e2x1["font"] = ("Arial","12","bold")
        self.e2x1["bg"] = ("antiquewhite1")
        self.e2x1["fg"] = ("maroon")

        self.e2x2 = Entry()
        self.e2x2.place(x=150, y=100, width=30, height=30)
        self.e2x2["font"] = ("Arial","12","bold")
        self.e2x2["bg"] = ("antiquewhite1")
        self.e2x2["fg"] = ("maroon")

        self.e2x3 = Entry()
        self.e2x3.place(x=150, y=130, width=30, height=30)
        self.e2x3["font"] = ("Arial","12","bold")
        self.e2x3["bg"] = ("antiquewhite1")
        self.e2x3["fg"] = ("maroon")

        self.e2x4 = Entry()
        self.e2x4.place(x=150, y=160, width=30, height=30)
        self.e2x4["font"] = ("Arial","12","bold")
        self.e2x4["bg"] = ("antiquewhite1")
        self.e2x4["fg"] = ("maroon")

        self.e2x5 = Entry()
        self.e2x5.place(x=150, y=190, width=30, height=30)
        self.e2x5["font"] = ("Arial","12","bold")
        self.e2x5["bg"] = ("antiquewhite1")
        self.e2x5["fg"] = ("maroon")
         
         #CAMPOS DE ENTRADA coluna  ****3****
        self.e3x1 = Entry()
        self.e3x1.place(x=180, y=70, width=30, height=30)
        self.e3x1["font"] = ("Arial","12","bold")
        self.e3x1["bg"] = ("antiquewhite1")
        self.e3x1["fg"] = ("maroon")

        self.e3x2 = Entry()
        self.e3x2.place(x=180, y=100, width=30, height=30)
        self.e3x2["font"] = ("Arial","12","bold")
        self.e3x2["bg"] = ("antiquewhite1")
        self.e3x2["fg"] = ("maroon")

        self.e3x3 = Entry()
        self.e3x3.place(x=180, y=130, width=30, height=30)
        self.e3x3["font"] = ("Arial","12","bold")
        self.e3x3["bg"] = ("antiquewhite1")
        self.e3x3["fg"] = ("maroon")

        self.e3x4 = Entry()
        self.e3x4.place(x=180, y=160, width=30, height=30)
        self.e3x4["font"] = ("Arial","12","bold")
        self.e3x4["bg"] = ("antiquewhite1")
        self.e3x4["fg"] = ("maroon")

        self.e3x5 = Entry()
        self.e3x5.place(x=180, y=190, width=30, height=30)
        self.e3x5["font"] = ("Arial","12","bold")
        self.e3x5["bg"] = ("antiquewhite1")
        self.e3x5["fg"] = ("maroon")

         #CAMPOS DE ENTRADA coluna  ****4****
        self.e4x1 = Entry()
        self.e4x1.place(x=210, y=70, width=30, height=30)
        self.e4x1["font"] = ("Arial","12","bold")
        self.e4x1["bg"] = ("antiquewhite1")
        self.e4x1["fg"] = ("maroon")

        self.e4x2 = Entry()
        self.e4x2.place(x=210, y=100, width=30, height=30)
        self.e4x2["font"] = ("Arial","12","bold")
        self.e4x2["bg"] = ("antiquewhite1")
        self.e4x2["fg"] = ("maroon")

        self.e4x3 = Entry()
        self.e4x3.place(x=210, y=130, width=30, height=30)
        self.e4x3["font"] = ("Arial","12","bold")
        self.e4x3["bg"] = ("antiquewhite1")
        self.e4x3["fg"] = ("maroon")

        self.e4x4 = Entry()
        self.e4x4.place(x=210, y=160, width=30, height=30)
        self.e4x4["font"] = ("Arial","12","bold")
        self.e4x4["bg"] = ("antiquewhite1")
        self.e4x4["fg"] = ("maroon")

        self.e4x5 = Entry()
        self.e4x5.place(x=210, y=190, width=30, height=30)
        self.e4x5["font"] = ("Arial","12","bold")
        self.e4x5["bg"] = ("antiquewhite1")
        self.e4x5["fg"] = ("maroon")

         #CAMPOS DE ENTRADA coluna  ****5****
        self.e5x1 = Entry()
        self.e5x1.place(x=240, y=70, width=30, height=30)
        self.e5x1["font"] = ("Arial","12","bold")
        self.e5x1["bg"] = ("antiquewhite1")
        self.e5x1["fg"] = ("maroon")

        self.e5x2 = Entry()
        self.e5x2.place(x=240, y=100, width=30, height=30)
        self.e5x2["font"] = ("Arial","12","bold")
        self.e5x2["bg"] = ("antiquewhite1")
        self.e5x2["fg"] = ("maroon")

        self.e5x3 = Entry()
        self.e5x3.place(x=240, y=130, width=30, height=30)
        self.e5x3["font"] = ("Arial","12","bold")
        self.e5x3["bg"] = ("antiquewhite1")
        self.e5x3["fg"] = ("maroon")

        self.e5x4 = Entry()
        self.e5x4.place(x=240, y=160, width=30, height=30)
        self.e5x4["font"] = ("Arial","12","bold")
        self.e5x4["bg"] = ("antiquewhite1")
        self.e5x4["fg"] = ("maroon")

        self.e5x5 = Entry()
        self.e5x5.place(x=240, y=190, width=30, height=30)
        self.e5x5["font"] = ("Arial","12","bold")
        self.e5x5["bg"] = ("antiquewhite1")
        self.e5x5["fg"] = ("maroon")

        self.bttCalcular = Button(text='Calcular')
        self.bttCalcular.place(x=10, y=230, width=90, height=40)
        self.bttCalcular["font"] = ("Arial","12","bold")
        self.bttCalcular["bg"] = ("pink1")
        self.bttCalcular['command'] = self.calculo
        self.bttCalcular["fg"] = ("deeppink4")

        self.lblResposta= Label(bg='antiquewhite1',fg="maroon")
        self.lblResposta.place(x=110, y=230, width=200, height=40)
        self.lblResposta["font"] = ("Arial","15","bold")



    def calculo(self):
        M=0
        matriz = int(self.selecionar.get())
        if matriz==1:
            
            e11=int(self.e1x1.get())
            e12=int(self.e1x2.get())
            e21=int(self.e2x1.get())
            e22=int(self.e2x2.get())
            M=np.array([[e11,e21],[e12,e22]])
        
        elif matriz==2 :
            
            e11=int(self.e1x1.get())
            e12=int(self.e1x2.get())
            e13=int(self.e1x3.get())

            e21=int(self.e2x1.get())
            e22=int(self.e2x2.get())
            e23=int(self.e2x3.get())

            e31=int(self.e3x1.get())
            e32=int(self.e3x2.get())
            e33=int(self.e3x3.get())

            M=np.array([[e11,e21,e31],[e12,e22,e32],[e13,e23,e33]])
           
        elif matriz==3:
            
            e11=int(self.e1x1.get())
            e12=int(self.e1x2.get())
            e13=int(self.e1x3.get())
            e14=int(self.e1x4.get())

            e21=int(self.e2x1.get())
            e22=int(self.e2x2.get())
            e23=int(self.e2x3.get())
            e24=int(self.e2x4.get())

            e31=int(self.e3x1.get())
            e32=int(self.e3x2.get())
            e33=int(self.e3x3.get())
            e34=int(self.e3x4.get())

            e41=int(self.e4x1.get())
            e42=int(self.e4x2.get())
            e43=int(self.e4x3.get())
            e44=int(self.e4x4.get())

            M=np.array([[e11,e21,e31,e41],[e12,e22,e32,e42],[e13,e23,e33,e43],[e14,e24,e34,e44]])
            
        elif matriz==4:
            
            e11=int(self.e1x1.get())
            e12=int(self.e1x2.get())
            e13=int(self.e1x3.get())
            e14=int(self.e1x4.get())
            e15=int(self.e1x5.get())

            e21=int(self.e2x1.get())
            e22=int(self.e2x2.get())
            e23=int(self.e2x3.get())
            e24=int(self.e2x4.get())
            e25=int(self.e2x5.get())

            e31=int(self.e3x1.get())
            e32=int(self.e3x2.get())
            e33=int(self.e3x3.get())
            e34=int(self.e3x4.get())
            e35=int(self.e3x5.get())

            
            e41=int(self.e4x1.get())
            e42=int(self.e4x2.get())
            e43=int(self.e4x3.get())
            e44=int(self.e4x4.get())
            e45=int(self.e4x5.get())

            
            e51=int(self.e5x1.get())
            e52=int(self.e5x2.get())
            e53=int(self.e5x3.get())
            e54=int(self.e5x4.get())
            e55=int(self.e5x5.get())

            M=np.array([[e11,e21,e31,e41,e51],[e12,e22,e32,e42,e52],[e13,e23,e33,e43,e53],[e14,e24,e34,e44,e54],[e15,e25,e35,e45,e55]])
        
        det_M =round(np.linalg.det(M))
        self.lblResposta['text'] = det_M
        
        

root=Tk()
root.title("Cálculo de Determinantes")
root.geometry("375x325")
root.resizable(False,False)
root["bg"] = ("lightpink2")
app = Calc_det (root)
root.mainloop()