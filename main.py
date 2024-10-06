from tkinter import *
from tkinter import font,messagebox,filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress
from PIL import Image, ImageTk


 




def main():

    def obtener_img(ruta):
        imagen = Image.open(ruta)
        imagen = imagen.resize((100,100))
        imagen_tk = ImageTk.PhotoImage(image=imagen)
        return imagen_tk
    
    def dowload(url,ruta):
        try:
            yt = YouTube(url)
            yt_filter = yt.streams.get_audio_only()
            nombre_archivo = f'{yt.title}_audio.{yt_filter.mime_type.split('/')[-1]}'
            yt_filter.download(ruta,nombre_archivo,mp3=True)
            lbl4.config(text='¡Descarga exitosa!',fg='green')
            

        except Exception:
            lbl4.config(text='Error',fg='red')

    def verificacion():

        if ety1.get():
                
            url = ety1.get()
            ruta_guardar = filedialog.askdirectory()
            dowload(url,ruta_guardar)
            ety2.insert(0,ruta_guardar)
        
        



    root = Tk()
    root.title('Descargar MP3')
    fuente = font.Font(root,family='roboto',size=13)
    ancho_pantalla = root.winfo_screenwidth() // 2
    alto_pantalla = root.winfo_screenheight() // 2
    root.geometry(f'600x400+{str(ancho_pantalla-400)}+{str(alto_pantalla-400)}')
    root.config(bd=15)
    root.resizable(False,False)
    imagen = obtener_img('imagenes/dowload.png')


    lbl1 = Label(root,image=imagen)
    lbl1.place(relx=0.01,rely=0.01)

    frame1 = LabelFrame(root,text='Descarga Música, ¡GRATIS!',bg='white',font=fuente)
    frame1.place(relx=0.2,width=450,height=200)

    lbl2 = Label(frame1,text='URL:',font=fuente,fg='black',bg='white')
    lbl2.place(x=1,rely=.1)

    ety1 = Entry(frame1,font=fuente,width=40,bg='beige')
    ety1.place(relx=.1,rely=.1,height=25)

    lbl3 = Label(frame1,text='OUTPUT:',font=fuente,fg='black',bg='white')
    lbl3.place(relx=.5,rely=.4,anchor=CENTER)

    ety2 = Entry(frame1,font=fuente,width=40,bg='beige')
    ety2.place(relx=.1,rely=.5,height=25)

    btn1 = Button(frame1,text='DOWLOAD',bg='red',command=verificacion,width=30,border=5,font=fuente)
    btn1.place(relx=.5,rely=.9,anchor=CENTER)


    lbl4 = Label(root,text='Hola',font=('roboto',20,'bold'))
    lbl4.pack(side=BOTTOM)



    
    
    
    
    
    
    
    
    
    
    root.mainloop()


if __name__ == '__main__':
    main()