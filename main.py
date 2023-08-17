import customtkinter
import os
import subprocess
from PIL import Image
import webbrowser
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.simpledialog as simpledialog
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from datetime import datetime

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión")
        self.geometry("700x450")
        customtkinter.set_default_color_theme("theme/fravega.json")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "logo.png")), size=(26, 26))
        self.banner_image = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner.png")), size=(480, 150))
        self.banner_image_compra = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_compra.png")), size=(500, 50))
        self.banner_image_venta = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_venta.png")), size=(500, 50))
        self.banner_image_empleados = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_empleados.png")), size=(500, 50))
        self.banner_image_deposito = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_deposito.png")), size=(500, 50))
        self.banner_image_entregas = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_entregas.png")), size=(500, 50))
        self.banner_image_caja = customtkinter.CTkImage(Image.open(os.path.join(self.image_path, "banner_caja.png")), size=(500, 50))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "inicio.png")), size=(20, 20))
        self.admin_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "admin.png")), size=(20, 20))
        self.rrhh_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "rrhh.png")), size=(20, 20))
        self.deposito_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "deposito.png")), size=(20, 20))
        self.entregas_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "entregas.png")), size=(20, 20))
        self.caja_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "caja.png")), size=(20, 20))
        self.mensajes_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "mensajes.png")), size=(20, 20))
        self.editar = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "editar.png")), size=(20, 20))
        self.eliminar = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "eliminar.png")), size=(20, 20))
        self.factura = customtkinter.CTkImage(light_image=Image.open(os.path.join(self.image_path, "fravega_factura.png")), size=(20, 20))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="FRÁVEGA", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont("Calibri",size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=25, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Administración",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.admin_image, state="disabled", anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="RR.HH",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.rrhh_image, anchor="w", state="disabled", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Depósito",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.deposito_image, anchor="w", state="disabled", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=4, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Entregas",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.entregas_image, anchor="w", state="disabled", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Caja",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.caja_image, anchor="w", state="disabled", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_banner_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.banner_image)
        self.home_frame_banner_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_label_1 = customtkinter.CTkLabel(self.home_frame, text="Usuario", fg_color="transparent")
        self.home_frame_label_1.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_label_2 = customtkinter.CTkLabel(self.home_frame, text="Clave", fg_color="transparent")
        self.home_frame_label_2.grid(row=4, column=0, padx=20, pady=10)
        self.home_frame_label_3 = customtkinter.CTkLabel(self.home_frame, text="https://www.fravega.com/", fg_color="transparent",
                                                            compound="right")
        self.home_frame_label_3.grid(row=7, column=0, padx=20, pady=20)

        def label_click(self):
            url = "https://www.fravega.com/"
            webbrowser.open(url)
        self.home_frame_label_3.bind("<Button-1>", label_click)

        self.home_frame_entry_1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Introduzca usuario")
        self.home_frame_entry_1.grid(row=3, column=0, padx=20, pady=0)
        self.home_frame_entry_2 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Introduzca clave", show="*")
        self.home_frame_entry_2.grid(row=5, column=0, padx=20, pady=0)

        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Iniciar Sesión", compound="right", command=self.login_event)
        self.home_frame_button_1.grid(row=6, column=0, padx=20, pady=20)

        self.frame_2 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_3 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_4 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_5 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_6 = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.select_frame_by_name("home")

        self.carrito = []

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.frame_2.grid(row=0, column=1,sticky="nsew")

            self.home_frame_2_button_1 = customtkinter.CTkButton(self.frame_2, text="Mensaje", width=2, image=self.mensajes_image)
            self.home_frame_2_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_2_banner_image_compra_label = customtkinter.CTkLabel(self.frame_2, text="", image=self.banner_image_compra)
            self.home_frame_2_banner_image_compra_label.grid(row=3, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")    

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#343638", foreground="white", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#F9F9FA", foreground="black", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_compra = ttk.Treeview(self.frame_2, style="Treeview", height=4)           
            self.treeview_compra["columns"] = ("area", "fecha", "documento")
            self.treeview_compra.column("#0", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_compra.column("area", width=85, minwidth=100, stretch=tk.NO)
            self.treeview_compra.column("fecha", width=100, minwidth=100, stretch=tk.NO)
            self.treeview_compra.column("documento", width=250, minwidth=100, stretch=tk.NO)
            self.treeview_compra.heading("#0", text="Id")
            self.treeview_compra.heading("area", text="Area")
            self.treeview_compra.heading("fecha", text="Fecha")
            self.treeview_compra.heading("documento", text="Mensaje")
            self.treeview_compra.grid(row=4,column=0,padx=5,pady=0)

            self.treeview_compra_scrollbar = customtkinter.CTkScrollbar(self.frame_2, height=124, command=self.treeview_compra.yview)
            self.treeview_compra_scrollbar.grid(row=4, column=0,padx=(460,0))

            self.home_frame_2_banner_image_venta_label = customtkinter.CTkLabel(self.frame_2, text="", image=self.banner_image_venta)
            self.home_frame_2_banner_image_venta_label.grid(row=5, column=0, padx=5, pady=0)

            self.treeview_venta = ttk.Treeview(self.frame_2, style="Treeview", height=4)           
            self.treeview_venta["columns"] = ("area", "fecha", "documento")
            self.treeview_venta.column("#0", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_venta.column("area", width=85, minwidth=100, stretch=tk.NO)
            self.treeview_venta.column("fecha", width=100, minwidth=100, stretch=tk.NO)
            self.treeview_venta.column("documento", width=250, minwidth=100, stretch=tk.NO)
            self.treeview_venta.heading("#0", text="Id")
            self.treeview_venta.heading("area", text="Area")
            self.treeview_venta.heading("fecha", text="Fecha")
            self.treeview_venta.heading("documento", text="Mensaje")
            self.treeview_venta.grid(row=6,column=0,padx=5,pady=0)

            treeview_venta_scrollbar = customtkinter.CTkScrollbar(self.frame_2, height=124, command=self.treeview_compra.yview)
            treeview_venta_scrollbar.grid(row=6, column=0,padx=(460,0))
        else:
            self.frame_2.grid_forget()
        if name == "frame_3":

            self.frame_3.grid(row=0, column=1, sticky="nsew")

            self.home_frame_3_button_1 = customtkinter.CTkButton(self.frame_3, text="Mensaje", width=2, image=self.mensajes_image)
            self.home_frame_3_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_3_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_3, text="", image=self.banner_image_empleados)
            self.home_frame_3_banner_image_empleados_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):
                style.configure("Treeview", background="#343638", foreground="white", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#F9F9FA", foreground="black", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_empleados = ttk.Treeview(self.frame_3, style="Treeview", height=4)           
            self.treeview_empleados["columns"] = ("DNI","Nombre y Apellido", "Area", "Salario", "Documentación")
            self.treeview_empleados.column("#0", width=0, minwidth=0)
            self.treeview_empleados.column("DNI", width=50, minwidth=50, stretch=tk.NO)
            self.treeview_empleados.column("Nombre y Apellido", width=152, minwidth=152, stretch=tk.NO)
            self.treeview_empleados.column("Area", width=55, minwidth=55, stretch=tk.NO)
            self.treeview_empleados.column("Salario", width=72, minwidth=72, stretch=tk.NO)
            self.treeview_empleados.column("Documentación", width=115, minwidth=115, stretch=tk.NO)
            self.treeview_empleados.heading("#0", text="")
            self.treeview_empleados.heading("DNI", text="DNI")
            self.treeview_empleados.heading("Nombre y Apellido", text="Nombre y Apellido")
            self.treeview_empleados.heading("Area", text="Area")
            self.treeview_empleados.heading("Salario", text="Salario")
            self.treeview_empleados.heading("Documentación", text="Documentación")
            self.treeview_empleados.grid(row=3,column=0,padx=5,pady=0)

            self.treeview_empleados_show(self.treeview_empleados)
            self.treeview_empleados.bind("<<TreeviewSelect>>", lambda event: self.treeview_empleados_show_entry(event, self.treeview_empleados))
            self.treeview_empleados.bind("<Escape>", lambda event: self.clear_entries_and_selection())

            self.treeview_empleados_scrollbar = customtkinter.CTkScrollbar(self.frame_3, height=124, command=self.treeview_empleados.yview)
            self.treeview_empleados_scrollbar.grid(row=3, column=0,padx=(460,0))

            self.home_frame_3_label_dni = customtkinter.CTkLabel(self.frame_3, text="DNI", fg_color="transparent")
            self.home_frame_3_label_dni.place(x=65,y=247)
            self.home_frame_3_label_nombreyapellido = customtkinter.CTkLabel(self.frame_3, text="Nombre y Apellido", fg_color="transparent")
            self.home_frame_3_label_nombreyapellido.place(x=312,y=247)
            self.home_frame_3_label_area = customtkinter.CTkLabel(self.frame_3, text="Area", fg_color="transparent")
            self.home_frame_3_label_area.place(x=65,y=312)
            self.home_frame_3_label_salario = customtkinter.CTkLabel(self.frame_3, text="Salario", fg_color="transparent")
            self.home_frame_3_label_salario.place(x=312,y=312)
            self.home_frame_3_label_documentación = customtkinter.CTkLabel(self.frame_3, text="Documentación", fg_color="transparent")
            self.home_frame_3_label_documentación.place(x=65,y=378)
            
            self.home_frame_3_entry_dni = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_dni.grid(row=5,column=0,padx=(0,250),pady=31)
            self.home_frame_3_entry_nombreyapellido = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_nombreyapellido.grid(row=5,column=0,padx=(250,0),pady=31)
            self.home_frame_3_entry_area = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_area.grid(row=6,column=0,padx=(0,250),pady=5)
            self.home_frame_3_entry_salario = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_salario.grid(row=6,column=0,padx=(250,0),pady=5)
            self.home_frame_3_entry_documentación = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_documentación.grid(row=7,column=0,padx=(0,250),pady=37)
            self.home_frame_3_entry_imagen = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_imagen.grid(row=23,column=0,padx=(0,0),pady=37)
            
            self.home_frame_3_entry_dni.configure(validate="key", validatecommand=(self.register(self.validate_dni), "%P"))
            self.home_frame_3_entry_nombreyapellido.configure(validate="key", validatecommand=(self.register(self.validate_nombre), "%P"))
            self.home_frame_3_entry_area.configure(validate="key", validatecommand=(self.register(self.validate_area), "%P"))
            self.home_frame_3_entry_salario.configure(validate="key", validatecommand=(self.register(self.validate_salario), "%P"))

            self.home_frame_3_button_2 = customtkinter.CTkButton(self.frame_3, text="Modificar", width=20, command=self.treeview_empleados_modify)
            self.home_frame_3_button_2.grid(row=7, column=0, padx=(130,0), pady=20)
            self.home_frame_3_button_3 = customtkinter.CTkButton(self.frame_3, text="Guardar", width=20, command=self.treeview_empleados_add)
            self.home_frame_3_button_3.grid(row=7, column=0, padx=(270,0), pady=20)
            self.home_frame_3_button_4 = customtkinter.CTkButton(self.frame_3, text="Eliminar", width=20, command=self.treeview_empleados_delete)
            self.home_frame_3_button_4.grid(row=7, column=0, padx=(400,0), pady=20)
        else:
            self.frame_3.grid_forget()
        if name == "frame_4":
            self.frame_4.grid(row=0, column=1, sticky="nsew")

            self.home_frame_4_button_1 = customtkinter.CTkButton(self.frame_4, text="Mensaje", width=2, image=self.mensajes_image)
            self.home_frame_4_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_4_banner_image_deposito_label = customtkinter.CTkLabel(self.frame_4, text="", image=self.banner_image_deposito)
            self.home_frame_4_banner_image_deposito_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#343638", foreground="white", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#F9F9FA", foreground="black", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_deposito = ttk.Treeview(self.frame_4, style="Treeview", height=4)           
            self.treeview_deposito["columns"] = ("Producto", "Fecha Entrada", "Fecha Salida")
            self.treeview_deposito.column("#0", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_deposito.column("Producto", width=182, minwidth=182, stretch=tk.NO)
            self.treeview_deposito.column("Fecha Entrada", width=110, minwidth=110, stretch=tk.NO)
            self.treeview_deposito.column("Fecha Salida", width=110, minwidth=110, stretch=tk.NO)
            self.treeview_deposito.heading("#0", text="Id")
            self.treeview_deposito.heading("Producto", text="Producto")
            self.treeview_deposito.heading("Fecha Entrada", text="Fecha Entrada")
            self.treeview_deposito.heading("Fecha Salida", text="Fecha Salida")
            self.treeview_deposito.grid(row=3,column=0,padx=5,pady=0)

            self.treeview_deposito_scrollbar = customtkinter.CTkScrollbar(self.frame_4, height=124, command=self.treeview_deposito.yview)
            self.treeview_deposito_scrollbar.grid(row=3, column=0,padx=(460,0))

            self.home_frame_4_label_producto = customtkinter.CTkLabel(self.frame_4, text="Producto", fg_color="transparent")
            self.home_frame_4_label_producto.place(x=50,y=248)
            self.home_frame_4_label_fecha_entrada = customtkinter.CTkLabel(self.frame_4, text="Fecha Entrada", fg_color="transparent")
            self.home_frame_4_label_fecha_entrada.place(x=198,y=248)
            self.home_frame_4_label_fecha_salida = customtkinter.CTkLabel(self.frame_4, text="Fecha Salida", fg_color="transparent")
            self.home_frame_4_label_fecha_salida.place(x=351,y=248)
            
            self.home_frame_4_entry_producto= customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_producto.grid(row=5,column=0,padx=(0,300),pady=40)
            self.home_frame_4_entry_fecha_entrada = customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_fecha_entrada.grid(row=5,column=0,padx=(0,0),pady=40)
            self.home_frame_4_entry_fecha_salida = customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_fecha_salida.grid(row=5,column=0,padx=(300,0),pady=5)

            self.home_frame_4_button_2 = customtkinter.CTkButton(self.frame_4, text="Guardar", width=20)
            self.home_frame_4_button_2.grid(row=7, column=0, padx=(260,0), pady=58)
            self.home_frame_4_button_3 = customtkinter.CTkButton(self.frame_4, text="Eliminar", width=20)
            self.home_frame_4_button_3.grid(row=7, column=0, padx=(400,0), pady=58)
        else:
            self.frame_4.grid_forget()
        if name == "frame_5":
            self.frame_5.grid(row=0, column=1, sticky="nsew")

            self.home_frame_5_button_1 = customtkinter.CTkButton(self.frame_5, text="Mensaje", width=2, image=self.mensajes_image)
            self.home_frame_5_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_5_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_5, text="", image=self.banner_image_entregas)
            self.home_frame_5_banner_image_empleados_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#343638", foreground="white", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#F9F9FA", foreground="black", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_entregas = ttk.Treeview(self.frame_5, style="Treeview", height=4)           
            self.treeview_entregas["columns"] = ("Producto", "Cantidad", "Cliente")
            self.treeview_entregas.column("#0", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_entregas.column("Producto", width=182, minwidth=182, stretch=tk.NO)
            self.treeview_entregas.column("Cantidad", width=52, minwidth=52, stretch=tk.NO)
            self.treeview_entregas.column("Cliente", width=172, minwidth=172, stretch=tk.NO)
            self.treeview_entregas.heading("#0", text="Id")
            self.treeview_entregas.heading("Producto", text="Producto")
            self.treeview_entregas.heading("Cantidad", text="Cantidad")
            self.treeview_entregas.heading("Cliente", text="Cliente")
            self.treeview_entregas.grid(row=3,column=0,padx=5,pady=0)

            self.treeview_entregas_scrollbar = customtkinter.CTkScrollbar(self.frame_5, height=124, command=self.treeview_entregas.yview)
            self.treeview_entregas_scrollbar.grid(row=3, column=0,padx=(460,0))

            self.home_frame_5_label_producto = customtkinter.CTkLabel(self.frame_5, text="Producto", fg_color="transparent")
            self.home_frame_5_label_producto.place(x=50,y=248)
            self.home_frame_5_label_fecha_entrada = customtkinter.CTkLabel(self.frame_5, text="Cantidad", fg_color="transparent")
            self.home_frame_5_label_fecha_entrada.place(x=198,y=248)
            self.home_frame_5_label_fecha_salida = customtkinter.CTkLabel(self.frame_5, text="Cliente", fg_color="transparent")
            self.home_frame_5_label_fecha_salida.place(x=351,y=248)
            
            self.home_frame_5_entry_producto= customtkinter.CTkEntry(self.frame_5, width=120)
            self.home_frame_5_entry_producto.grid(row=5,column=0,padx=(0,300),pady=40)
            self.home_frame_5_entry_fecha_entrada = customtkinter.CTkEntry(self.frame_5, width=120)
            self.home_frame_5_entry_fecha_entrada.grid(row=5,column=0,padx=(0,0),pady=40)
            self.home_frame_5_entry_fecha_salida = customtkinter.CTkEntry(self.frame_5, width=120)
            self.home_frame_5_entry_fecha_salida.grid(row=5,column=0,padx=(300,0),pady=5)

            self.home_frame_5_button_2 = customtkinter.CTkButton(self.frame_5, text="Guardar", width=20)
            self.home_frame_5_button_2.grid(row=7, column=0, padx=(260,0), pady=58)
            self.home_frame_5_button_3 = customtkinter.CTkButton(self.frame_5, text="Eliminar", width=20)
            self.home_frame_5_button_3.grid(row=7, column=0, padx=(400,0), pady=58)
        else:
            self.frame_5.grid_forget()
        if name == "frame_6":
            self.frame_6.grid(row=0, column=1, sticky="nsew")

            self.home_frame_6_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_6, text="", image=self.banner_image_caja)
            self.home_frame_6_banner_image_empleados_label.grid(row=0, column=0, padx=5, pady=0)

            self.home_frame_6_label_producto = customtkinter.CTkLabel(self.frame_6, text="1. Seleccione el o los productos:", fg_color="transparent")
            self.home_frame_6_label_producto.grid(row=1, column=0, padx=(0,250), pady=0)
            
            self.values_menu_productos()

            self.home_frame_6_label_cantidad = customtkinter.CTkLabel(self.frame_6, text="2. Escriba la cantidad:", fg_color="transparent")
            self.home_frame_6_label_cantidad.grid(row=2, column=0, padx=(0,310), pady=0)
            self.home_frame_6_entry_cantidad = customtkinter.CTkEntry(self.frame_6, width=40)
            self.home_frame_6_entry_cantidad.grid(row=2,column=0,padx=(0,140),pady=0)
            self.home_frame_6_button_2 = customtkinter.CTkButton(self.frame_6, text="Agregar al carrito", width=20, command=self.agregar_al_carrito)
            self.home_frame_6_button_2.grid(row=2, column=0, padx=(325, 0), pady=0)
            self.home_frame_6_button_3 = customtkinter.CTkButton(self.frame_6, text="", image=self.editar, width=20, command=self.editar_item_seleccionado)
            self.home_frame_6_button_3.grid(row=2, column=0, padx=(160,0), pady=0)
            self.home_frame_6_button_4 = customtkinter.CTkButton(self.frame_6, text="", image=self.eliminar, width=20, command=self.limpiar_carrito)
            self.home_frame_6_button_4.grid(row=2, column=0, padx=(70, 0), pady=0)
            
            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):
                style.configure("Treeview", background="#343638", foreground="white", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#F9F9FA", foreground="black", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_carrito = ttk.Treeview(self.frame_6, style="Treeview", height=3)           
            self.treeview_carrito["columns"] = ("Id","Producto", "Cantidad", "Precio")
            self.treeview_carrito.column("#0", width=0, minwidth=0, stretch=tk.NO)
            self.treeview_carrito.column("Id", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_carrito.column("Producto", width=250, minwidth=250, stretch=tk.NO)
            self.treeview_carrito.column("Cantidad", width=60, minwidth=60, stretch=tk.NO)
            self.treeview_carrito.column("Precio", width=70, minwidth=70, stretch=tk.NO)
            self.treeview_carrito.heading("#0", text="Id")
            self.treeview_carrito.heading("Id", text="Id")
            self.treeview_carrito.heading("Producto", text="Producto")
            self.treeview_carrito.heading("Cantidad", text="Cantidad")
            self.treeview_carrito.heading("Precio", text="Precio")
            self.treeview_carrito.grid(row=3,column=0,padx=5,pady=20)

            self.treeview_carrito.bind("<ButtonRelease-1>", self.seleccionar_producto)

            self.treeview_carrito_scrollbar = customtkinter.CTkScrollbar(self.frame_6, height=104, command=self.treeview_carrito.yview)
            self.treeview_carrito_scrollbar.grid(row=3, column=0,padx=(420,0))

            self.home_frame_6_label_dni = customtkinter.CTkLabel(self.frame_6, text="3. DNI Cliente:", fg_color="transparent")
            self.home_frame_6_label_dni.grid(row=4, column=0, padx=(0,350), pady=0)
            self.home_frame_6_entry_dni = customtkinter.CTkEntry(self.frame_6, width=120)
            self.home_frame_6_entry_dni.grid(row=4,column=0,padx=(0,140),pady=0)

            self.home_frame_6_label_total = customtkinter.CTkLabel(self.frame_6, text="4. Precio total:", fg_color="transparent")
            self.home_frame_6_label_total.grid(row=5, column=0, padx=(0,350), pady=20)
            self.home_frame_6_entry_total = customtkinter.CTkEntry(self.frame_6, width=120)
            self.home_frame_6_entry_total.insert(0, "0")
            self.home_frame_6_entry_total.grid(row=5,column=0,padx=(0,140),pady=20)

            self.home_frame_6_button_5 = customtkinter.CTkButton(self.frame_6, text="Vender", width=20, command=self.realizar_venta)
            self.home_frame_6_button_5.grid(row=6, column=0, padx=(0, 400), pady=30)

        else:
            self.frame_6.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def leave_event(self):

            self.home_frame_label_1 = customtkinter.CTkLabel(self.home_frame, text="Usuario", fg_color="transparent")
            self.home_frame_label_1.grid(row=2, column=0, padx=20, pady=10)
            self.home_frame_label_2 = customtkinter.CTkLabel(self.home_frame, text="Clave", fg_color="transparent")
            self.home_frame_label_2.grid(row=4, column=0, padx=20, pady=10)
                
            self.home_frame_entry_1 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Introduzca usuario")
            self.home_frame_entry_1.grid(row=3, column=0, padx=20, pady=0)
            self.home_frame_entry_2 = customtkinter.CTkEntry(self.home_frame, placeholder_text="Introduzca clave", show="*")
            self.home_frame_entry_2.grid(row=5, column=0, padx=20, pady=0)            

            self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="Iniciar Sesión", compound="right", command=self.login_event)
            self.home_frame_button_1.grid(row=6, column=0, padx=20, pady=20)

            self.frame_2_button.configure(state="disabled")
            self.frame_3_button.configure(state="disabled")
            self.frame_4_button.configure(state="disabled")
            self.frame_5_button.configure(state="disabled")

            self.home_frame_label_4.destroy()

    def login_event(self):
        conn = sqlite3.connect("fravega_data.db")
        cursor = conn.cursor()
        data = (self.home_frame_entry_1.get(), self.home_frame_entry_2.get())
        cursor.execute("SELECT * FROM user WHERE usuario = ? AND clave = ?", (data))
        fetchall = cursor.fetchall()

        if (fetchall):
            self.home_frame_label_1.destroy()
            self.home_frame_entry_1.destroy()
            self.home_frame_button_1.destroy()
            self.home_frame_label_2.destroy()
            self.home_frame_entry_2.destroy()

            for row in fetchall:
                column0 = row[0]

            self.home_frame_label_4 = customtkinter.CTkLabel(self.home_frame, text="Inició sesión como "+column0+".", fg_color="transparent")
            self.home_frame_label_4.grid(row=2, column=0, padx=20, pady=10)

            self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Cerrar Sesión", compound="right", command=self.leave_event)
            self.home_frame_button_2.grid(row=6, column=0, padx=20, pady=20)

            if (column0 == "Gerente"):
                self.frame_2_button.configure(state="enabled")
                self.frame_3_button.configure(state="enabled")
                self.frame_4_button.configure(state="enabled")
                self.frame_5_button.configure(state="enabled")
                self.frame_6_button.configure(state="enabled")
            elif (column0 == "Administración"):
                self.frame_2_button.configure(state="enabled")
            elif (column0 == "Rrhh"):
                self.frame_3_button.configure(state="enabled")
            elif (column0 == "Depósito"):
                self.frame_4_button.configure(state="enabled")
            elif (column0 == "Entregas"):
                self.frame_5_button.configure(state="enabled")
            elif (column0 == "Caja"):
                self.frame_6_button.configure(state="enabled")
        else:
            self.home_frame_label_5 = customtkinter.CTkLabel(self.home_frame, text="Usuario no encontrado.", text_color="red")
            self.home_frame_label_5.place(x=195, y=380)

            def after_user_error():
                self.home_frame_label_5.destroy()

            self.home_frame.after(3500,after_user_error)

    #Funciones frames

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")

    def email_event(self):
        app_email = customtkinter.CTk()
        app_email.geometry("650x400")
        app_email.title("Email Fravega")

        app_email.mainloop()
        
    #Frame 2 functions 

    def treeview_empleados_show(self, treeview_empleados):
        try:
            conn = sqlite3.connect("fravega_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT dni, nya, area, sal, doc, img FROM rh")
            fetchall = cursor.fetchall()
            conn.close()

            for fila in treeview_empleados.get_children():
                treeview_empleados.delete(fila)

            for dato in fetchall:
                treeview_empleados.insert("", "end", values=dato)

        except sqlite3.Error as error:
            mensaje_error = "Error al acceder a la base de datos: " + str(error)
            tk.messagebox.showerror("Error", mensaje_error)

    def treeview_empleados_show_entry(self, event, treeview_empleados):
        seleccion = treeview_empleados.selection()
        if seleccion:
            item = treeview_empleados.item(seleccion[0], "values")
            self.home_frame_3_entry_dni.delete(0, tk.END)
            self.home_frame_3_entry_dni.insert(0, item[0])
            self.home_frame_3_entry_nombreyapellido.delete(0, tk.END)
            self.home_frame_3_entry_nombreyapellido.insert(0, item[1])
            self.home_frame_3_entry_area.delete(0, tk.END)
            self.home_frame_3_entry_area.insert(0, item[2])
            self.home_frame_3_entry_salario.delete(0, tk.END)
            self.home_frame_3_entry_salario.insert(0, item[3])
            self.home_frame_3_entry_documentación.delete(0, tk.END)
            self.home_frame_3_entry_documentación.insert(0, item[4])
            imagen_ruta = item[5] 

            if imagen_ruta != "":

                if hasattr(self, "home_frame_3_label_imagen"):
                    self.home_frame_3_label_imagen.destroy()

                self.home_frame_3_label_imagen = tk.Label(self.frame_3)
                self.home_frame_3_label_imagen.place(x=215, y=280)

                img = Image.open(imagen_ruta)
                img_resized = img.resize((75, 75)) 
                self.empleado_image = ImageTk.PhotoImage(img_resized) 
                self.home_frame_3_label_imagen.configure(image=self.empleado_image)
            else:
                if hasattr(self, "home_frame_3_label_imagen"):
                    self.home_frame_3_label_imagen.destroy()

    def treeview_empleados_delete(self):
        question = messagebox.askquestion("Cuidado","¿Desea eliminar definitivamente el empleado?")

        if (question == "yes"):
            dni = self.home_frame_3_entry_dni.get()
            try:
                conexion = sqlite3.connect("fravega_data.db")
                cursor = conexion.cursor()

                cursor.execute("DELETE FROM rh WHERE dni = ?", (dni,))
                conexion.commit()
                conexion.close()

                self.clear_entries_and_selection()
                self.refresh_treeview()
            
                messagebox.showinfo("Exito","El empleado fue dado de baja.")

            except sqlite3.Error as error:
                mensaje_error = "Error al eliminar el empleado: " + str(error)
                messagebox.showerror("Error", mensaje_error)
        else:
            return
        
    def treeview_empleados_modify(self):
        question = messagebox.askquestion("Cuidado","Desea modificar el empleado?")

        if (question == "yes"):
            dni = self.home_frame_3_entry_dni.get()
            nya = self.home_frame_3_entry_nombreyapellido.get()
            area = self.home_frame_3_entry_area.get()
            salario = self.home_frame_3_entry_salario.get()
            doc = self.home_frame_3_entry_documentación.get()
            img = self.home_frame_3_entry_imagen.get()

            conexion = sqlite3.connect("fravega_data.db")
            cursor = conexion.cursor()

            question = messagebox.askquestion("Cuidado","¿Desea modificar la imagen?")
            if (question == "yes"):
                self.load_image()
                img = self.home_frame_3_entry_imagen.get()
                cursor.execute("UPDATE rh SET nya=?, area=?, sal=?,doc=?,img=? WHERE dni=?", (nya, area, salario, doc, img, dni))

            elif (question == "no"):
                cursor.execute("UPDATE rh SET nya=?, area=?, sal=?,doc=? WHERE dni=?", (nya, area, salario, doc, dni))
            conexion.commit()
            conexion.close()

            self.clear_entries_and_selection()
            self.refresh_treeview()

            messagebox.showinfo("Exito","El empleado fue modificado.")
        else:
            return

    def treeview_empleados_add(self):
        def dni_verification(dni):
            try:
                conexion = sqlite3.connect("fravega_data.db")
                cursor = conexion.cursor()

                cursor.execute("SELECT dni FROM rh WHERE dni = ?", (dni,))
                resultado = cursor.fetchone()

                conexion.close()

                if resultado:
                    return True
                else:
                    return False

            except sqlite3.Error as error:
                mensaje_error = "Error al verificar el DNI: " + str(error)
                messagebox.showerror("Error", mensaje_error)
                return True

        question = messagebox.askquestion("Cuidado", "¿Desea agregar este nuevo empleado?")

        if question == "yes":
            dni = self.home_frame_3_entry_dni.get()
            nya = self.home_frame_3_entry_nombreyapellido.get()
            area = self.home_frame_3_entry_area.get()
            salario = self.home_frame_3_entry_salario.get()
            doc = self.home_frame_3_entry_documentación.get()

            if not dni or not nya or not area or not salario or not doc:
                messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
                return

            if dni_verification(dni):
                messagebox.showwarning("Cuidado", "El DNI ya está registrado. No se puede agregar nuevamente.")
                return

            try:
                conexion = sqlite3.connect("fravega_data.db")
                cursor = conexion.cursor()

                cursor.execute("INSERT INTO rh (dni, nya, area, sal, doc) VALUES (?, ?, ?, ?, ?)",
                            (dni, nya, area, salario, doc, img))
                conexion.commit()
                conexion.close()

                self.clear_entries_and_selection()
                self.refresh_treeview()

                messagebox.showinfo("Éxito", "El empleado fue dado de alta.")

            except sqlite3.Error as error:
                mensaje_error = "Error al agregar el empleado: " + str(error)
                messagebox.showerror("Error", mensaje_error)
        else:
            return

    def validate_dni(self, new_value):
        return new_value.isdigit() and len(new_value) <= 8 or new_value == ""
     
    def validate_nombre(self, new_value):
        return all(c.isalpha() or c.isspace() for c in new_value)

    def validate_salario(self, new_value):
        try:
            float(new_value)
            return True
        except ValueError:
            return new_value == "" or (new_value.replace(".", "", 1).isdigit() and (not new_value.startswith("0") or new_value == "0"))

    def validate_area(self, new_value):
        return all(c.isalpha() or c.isspace() for c in new_value)

    def clear_entries_and_selection(self):
    
        self.home_frame_3_entry_dni.delete(0, tk.END)
        self.home_frame_3_entry_nombreyapellido.delete(0, tk.END)
        self.home_frame_3_entry_area.delete(0, tk.END)
        self.home_frame_3_entry_salario.delete(0, tk.END)
        self.home_frame_3_entry_imagen.delete(0, tk.END)
        self.home_frame_3_entry_documentación.delete(0, tk.END)
        self.home_frame_3_label_imagen.destroy()

        self.treeview_empleados.selection_remove(self.treeview_empleados.focus())
    
    def load_image(self):
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
        self.home_frame_3_entry_imagen.delete(0, tk.END)
        self.home_frame_3_entry_imagen.insert(0, ruta_imagen)
    
    def refresh_treeview(self):
        for record in self.treeview_empleados.get_children():
            self.treeview_empleados.delete(record)

        conexion = sqlite3.connect("fravega_data.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT dni, nya, area, sal, doc, img FROM rh")
        empleados = cursor.fetchall()
        for empleado in empleados:
            self.treeview_empleados.insert("", "end", values=empleado)

        conexion.close()

        for col in ["#0", "DNI", "Nombre y Apellido", "Area", "Salario", "Documentación"]:
            self.treeview_empleados.heading(col, anchor=tk.W)
            self.treeview_empleados.column(col, anchor=tk.CENTER)

    #Frame 6 functions 

    def values_menu_productos(self):
        self.conn = sqlite3.connect("fravega_data.db")
        self.cursor = self.conn.cursor()

        query = "SELECT prod FROM dep WHERE cant > 1"
        self.cursor.execute(query)
        product_names = [row[0] for row in self.cursor.fetchall()]

        self.home_frame_6_menu_producto = customtkinter.CTkComboBox(self.frame_6, values=product_names, width=250)
        self.home_frame_6_menu_producto.grid(row=1, column=0, padx=(190, 0), pady=20)

        self.home_frame_6_menu_producto.set("Seleccione producto")
        self.home_frame_6_menu_producto.configure(state="readonly")

    def agregar_al_carrito(self):
        producto_seleccionado = self.home_frame_6_menu_producto.get()

        if not producto_seleccionado or producto_seleccionado == "Seleccione producto":
            messagebox.showinfo("Producto no seleccionado", "Por favor, seleccione un producto antes de agregarlo al carrito.")
            return

        cantidad = self.home_frame_6_entry_cantidad.get()

        if not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showinfo("Cantidad inválida", "Por favor, ingrese una cantidad válida mayor a 0.")
            return

        cantidad = int(cantidad)
        producto_seleccionado = self.home_frame_6_menu_producto.get()
        cantidad = int(self.home_frame_6_entry_cantidad.get())

        # Realizar consulta para obtener información del producto seleccionado
        query = f"SELECT id, prod, precio, cant FROM dep WHERE prod = '{producto_seleccionado}'"
        self.cursor.execute(query)
        producto_info = self.cursor.fetchone()

        if producto_info:
            
            producto_id, producto_nombre, producto_precio, stock_disponible = producto_info

            if cantidad > stock_disponible:
                messagebox.showerror("Error de Stock", f"La cantidad ingresada es mayor al stock disponible. Stock disponible: {stock_disponible}")
            elif cantidad <= 0:
                messagebox.showerror("Error de Cantidad", "La cantidad ingresada debe ser mayor a 0.")
            else:
                # Verificar si el producto ya está en el carrito
                for item in self.carrito:
                    if item["producto"] == producto_seleccionado:
                        messagebox.showinfo("Producto Existente", "Este producto ya está en el carrito.")
                        return

                # Calcular el precio total del producto
                precio_total = producto_precio * cantidad

                # Agregar el producto al carrito
                self.carrito.append({
                    "id": producto_id,
                    "producto": producto_nombre,
                    "cantidad": cantidad,
                    "precio_unitario": producto_precio,
                    "precio_total": precio_total
                })
                
                self.home_frame_6_menu_producto.set("Seleccione producto")
                self.home_frame_6_entry_cantidad.delete(0, tk.END)

                # Actualizar la vista del Treeview
                self.actualizar_treeview_carrito()

            # Restaurar el valor del Entry de cantidad
            self.home_frame_6_entry_cantidad.delete(0, tk.END)
            self.home_frame_6_menu_producto.set("Seleccione producto")
        else:
            messagebox.showerror("Error", "El producto seleccionado no se encontró en la base de datos.")

    def editar_item_seleccionado(self):
        # Obtener el elemento seleccionado en el Treeview
        elemento_seleccionado = self.treeview_carrito.focus()

        if not elemento_seleccionado:
            messagebox.showinfo("Ningún elemento seleccionado", "Por favor, seleccione un elemento en el carrito para editar.")
            return

        # Obtener los valores de las columnas del elemento seleccionado
        valores_elemento = self.treeview_carrito.item(elemento_seleccionado, "values")
        producto_id, producto_nombre, _, _ = valores_elemento

        # Buscar el elemento en el carrito comparando con el nombre del producto
        for idx, item in enumerate(self.carrito):
            if item["producto"] == producto_nombre:
                nueva_cantidad = self.home_frame_6_entry_cantidad.get()

                if not nueva_cantidad.isdigit() or int(nueva_cantidad) <= 0:
                    messagebox.showinfo("Cantidad inválida", "Por favor, ingrese una cantidad válida mayor a 0.")
                    return

                nueva_cantidad = int(nueva_cantidad)

                # Realizar consulta para obtener información del producto seleccionado
                query = f"SELECT id, prod, precio, cant FROM dep WHERE prod = '{producto_nombre}'"
                self.cursor.execute(query)
                producto_info = self.cursor.fetchone()

                if producto_info:
                    _, _, _, stock_disponible = producto_info

                    if nueva_cantidad > stock_disponible:
                        messagebox.showinfo("Cantidad excede el stock", f"La cantidad ingresada supera el stock disponible ({stock_disponible}).")
                        return

                # Actualizar la cantidad del elemento
                self.carrito[idx]["cantidad"] = nueva_cantidad

                # Actualizar el Treeview
                self.actualizar_treeview_carrito()

                # Limpiar los entry
                self.home_frame_6_menu_producto.set("Seleccione producto")
                self.home_frame_6_entry_cantidad.delete(0, tk.END)
                return

    def limpiar_carrito(self):
        respuesta = messagebox.askyesno("Limpiar Carrito", "¿Desea limpiar el carrito?")
        if respuesta:
            self.carrito = []
            self.actualizar_treeview_carrito()  # Limpia el Treeview
            self.actualizar_precio_total()   # Actualiza el precio total

            # Limpiar los entry
            self.home_frame_6_menu_producto.set("Seleccione producto")
            self.home_frame_6_entry_cantidad.delete(0, tk.END)

    def actualizar_treeview_carrito(self):
        self.treeview_carrito.delete(*self.treeview_carrito.get_children())
        for item in self.carrito:
            self.treeview_carrito.insert("", "end", values=(
                item["id"],
                item["producto"],
                item["cantidad"],
                item["precio_unitario"]
            ))
        self.actualizar_precio_total()
                
    def actualizar_precio_total(self):
        self.total_venta = sum(item["precio_total"] for item in self.carrito)
        self.home_frame_6_entry_total.delete(0, "end")
        self.home_frame_6_entry_total.insert(0, self.total_venta)

    def seleccionar_producto(self, event):
        selected_item = self.treeview_carrito.selection()
        if selected_item:
            item_producto = self.treeview_carrito.item(selected_item, "values")[1]
            item_cantidad = self.treeview_carrito.item(selected_item, "values")[2]

            self.home_frame_6_menu_producto.set(item_producto)
            self.home_frame_6_entry_cantidad.delete(0, tk.END)
            self.home_frame_6_entry_cantidad.insert(0, item_cantidad)

    def realizar_venta(self):
        # Obtén la ruta absoluta del archivo actual
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Ruta de la imagen de fondo
        image_path = os.path.join(current_dir, "images", "fravega_factura.png")

        # Obtener fecha y hora actual para el nombre del ticket
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_filename = os.path.join(current_dir, "tickets", f"ticket_{fecha_hora_actual}.pdf")

        # Calcular subtotal, IVA y total
        subtotal = sum(item["precio_total"] for item in self.carrito)
        total_iva = subtotal * 0.21
        total_con_iva = subtotal + total_iva

        # Crear el documento PDF
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Crear el contenido del ticket
        story = []

        # Agregar imagen de fondo a cada página
        def add_background(canvas, doc):
            canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])

        doc.build(story, onFirstPage=add_background, onLaterPages=add_background)

        # Agregar espacio para centrar contenido
        story.append(Spacer(1, (letter[1] - 150) / 2))  # Ajusta el valor para centrar

        # Agregar detalles del carrito al PDF
        style_normal = getSampleStyleSheet()['Normal']

        for item in self.carrito:
            producto_nombre = item["producto"]
            cantidad = item["cantidad"]
            precio_unitario = item["precio_unitario"]
            precio_total = item["precio_total"]

            # Presentar los datos sin formato de tabla
            details = [
                f"Producto: {producto_nombre}",
                f"Cantidad: {cantidad}",
                f"Precio Unitario: ${precio_unitario:.2f}",
                f"Precio Total: ${precio_total:.2f}"
            ]
            story.extend([Paragraph(detail, style_normal) for detail in details])
            story.append(Spacer(1, 12))

        # Agregar espacio después de los detalles del carrito
        story.append(Spacer(1, 50))  # Espacio adicional entre detalles y totales
        story.append(Paragraph(f"Subtotal: ${subtotal:.2f}", style_normal))
        story.append(Paragraph(f"Total IVA (21%): ${total_iva:.2f}", style_normal))
        story.append(Paragraph(f"Total con IVA: ${total_con_iva:.2f}", style_normal))

        # Generar el PDF
        doc.build(story)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Venta realizada", f"Se realizó la venta correctamente. El ticket se ha guardado en {pdf_filename}.")


    #Appearance 

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.home_button_event()
        self.home_frame_3_label_dni = customtkinter.CTkLabel(self.home_frame, text="Tema cambiado exitosamente", fg_color="transparent", text_color="#0AC90A")
        self.home_frame_3_label_dni.grid(row=8,column=0)

        def after_theme_changed():
                self.home_frame_3_label_dni.destroy()

        self.home_frame.after(2500,after_theme_changed)

if __name__ == "__main__":
    app = App()
    app.iconbitmap("images/fravega.ico")
    app.resizable(0,0)
    app.mainloop()