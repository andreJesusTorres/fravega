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
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
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

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Caja",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.caja_image, anchor="w", state="disabled", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

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

        self.select_frame_by_name("home")

        self.carrito = []

    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")

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
            self.treeview_compra["columns"] = ("id","area", "fecha", "producto", "detalle")
            self.treeview_compra.column("#0", width=0, minwidth=0, stretch=tk.NO)
            self.treeview_compra.column("id", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_compra.column("area", width=75, minwidth=100, stretch=tk.NO)
            self.treeview_compra.column("fecha", width=65, minwidth=100, stretch=tk.NO)
            self.treeview_compra.column("producto", width=130, minwidth=100, stretch=tk.NO)
            self.treeview_compra.column("detalle", width=150, minwidth=100, stretch=tk.NO)
            self.treeview_compra.heading("#0", text="")
            self.treeview_compra.heading("id", text="Id")
            self.treeview_compra.heading("area", text="Area")
            self.treeview_compra.heading("fecha", text="Fecha")
            self.treeview_compra.heading("producto", text="Producto")
            self.treeview_compra.heading("detalle", text="Detalle")
            self.treeview_compra.grid(row=4,column=0,padx=5,pady=0)

            self.treeview_compra_show(self.treeview_compra)

            self.treeview_compra.bind("<Escape>", lambda event: self.clear_selection_compra())

            self.treeview_compra_scrollbar = customtkinter.CTkScrollbar(self.frame_2, height=124, command=self.treeview_compra.yview)
            self.treeview_compra_scrollbar.grid(row=4, column=0,padx=(460,0))

            self.home_frame_2_banner_image_venta_label = customtkinter.CTkLabel(self.frame_2, text="", image=self.banner_image_venta)
            self.home_frame_2_banner_image_venta_label.grid(row=5, column=0, padx=5, pady=0)

            self.treeview_venta = ttk.Treeview(self.frame_2, style="Treeview", height=4)           
            self.treeview_venta["columns"] = ("id","fecha", "producto", "cantidad","precio")
            self.treeview_venta.column("#0", width=0, minwidth=0, stretch=tk.NO)
            self.treeview_venta.column("id", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_venta.column("fecha", width=85, minwidth=100, stretch=tk.NO)
            self.treeview_venta.column("producto", width=210, minwidth=100, stretch=tk.NO)
            self.treeview_venta.column("cantidad", width=50, minwidth=100, stretch=tk.NO)
            self.treeview_venta.column("precio", width=70, minwidth=100, stretch=tk.NO)
            self.treeview_venta.heading("#0", text="")
            self.treeview_venta.heading("id", text="Id")
            self.treeview_venta.heading("fecha", text="Fecha")
            self.treeview_venta.heading("producto", text="Producto")
            self.treeview_venta.heading("cantidad", text="Cantidad")
            self.treeview_venta.heading("precio", text="Precio")
            self.treeview_venta.grid(row=6,column=0,padx=5,pady=0)

            self.treeview_venta_show(self.treeview_venta)
                        
            self.treeview_venta.bind("<Escape>", lambda event: self.clear_selection_venta())

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
            self.treeview_empleados.bind("<Escape>", lambda event: self.clear_entries_and_selection_empleados())

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

            self.home_frame_3_button_2 = customtkinter.CTkButton(self.frame_3, text="Modificar", width=20, command=lambda:self.treeview_empleados_modify(self.treeview_empleados))
            self.home_frame_3_button_2.grid(row=7, column=0, padx=(130,0), pady=20)
            self.home_frame_3_button_3 = customtkinter.CTkButton(self.frame_3, text="Guardar", width=20, command=self.treeview_empleados_add)
            self.home_frame_3_button_3.grid(row=7, column=0, padx=(270,0), pady=20)
            self.home_frame_3_button_4 = customtkinter.CTkButton(self.frame_3, text="Eliminar", width=20, command=lambda:self.treeview_empleados_delete(self.treeview_empleados))
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
            self.treeview_deposito["columns"] = ("Id","Producto", "Cantidad", "Precio")
            self.treeview_deposito.column("#0", width=0, minwidth=0)
            self.treeview_deposito.column("Id", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_deposito.column("Producto", width=292, minwidth=292, stretch=tk.NO)
            self.treeview_deposito.column("Cantidad", width=50, minwidth=50, stretch=tk.NO)
            self.treeview_deposito.column("Precio", width=60, minwidth=60, stretch=tk.NO)
            self.treeview_deposito.heading("#0", text="")
            self.treeview_deposito.heading("Id", text="Id")
            self.treeview_deposito.heading("Producto", text="Producto")
            self.treeview_deposito.heading("Cantidad", text="Cantidad")
            self.treeview_deposito.heading("Precio", text="Precio")
            self.treeview_deposito.grid(row=3,column=0,padx=5,pady=0)

            self.treeview_deposito_show(self.treeview_deposito)
            self.treeview_deposito.bind("<<TreeviewSelect>>", lambda event: self.treeview_deposito_show_entry(event, self.treeview_deposito))
            self.treeview_deposito.bind("<Escape>", lambda event: self.clear_entries_and_selection_deposito())

            self.treeview_deposito_scrollbar = customtkinter.CTkScrollbar(self.frame_4, height=124, command=self.treeview_deposito.yview)
            self.treeview_deposito_scrollbar.grid(row=3, column=0,padx=(460,0))

            self.home_frame_4_label_producto = customtkinter.CTkLabel(self.frame_4, text="Producto", fg_color="transparent")
            self.home_frame_4_label_producto.place(x=50,y=248)
            self.home_frame_4_label_cantidad = customtkinter.CTkLabel(self.frame_4, text="Cantidad", fg_color="transparent")
            self.home_frame_4_label_cantidad.place(x=198,y=248)
            self.home_frame_4_label_precio = customtkinter.CTkLabel(self.frame_4, text="Precio", fg_color="transparent")
            self.home_frame_4_label_precio.place(x=351,y=248)

            self.home_frame_4_entry_id= customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_id.grid(row=5,column=0,padx=(0,300),pady=40)            
            self.home_frame_4_entry_producto= customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_producto.grid(row=5,column=0,padx=(0,300),pady=40)
            self.home_frame_4_entry_cantidad= customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_cantidad.grid(row=5,column=0,padx=(0,0),pady=40)
            self.home_frame_4_entry_precio = customtkinter.CTkEntry(self.frame_4, width=120)
            self.home_frame_4_entry_precio.grid(row=5,column=0,padx=(300,0),pady=5)

            self.home_frame_4_button_2 = customtkinter.CTkButton(self.frame_4, text="Modificar", width=20, command=self.treeview_deposito_modify)
            self.home_frame_4_button_2.grid(row=7, column=0, padx=(130,0), pady=20)
            self.home_frame_4_button_3 = customtkinter.CTkButton(self.frame_4, text="Guardar", width=20, command=self.treeview_deposito_add)
            self.home_frame_4_button_3.grid(row=7, column=0, padx=(270,0), pady=20)
            self.home_frame_4_button_4 = customtkinter.CTkButton(self.frame_4, text="Eliminar", width=20, command=self.treeview_deposito_delete)
            self.home_frame_4_button_4.grid(row=7, column=0, padx=(400,0), pady=20)
        else:
            self.frame_4.grid_forget()
        
            self.frame_5.grid_forget()
        if name == "frame_5":
            self.frame_5.grid(row=0, column=1, sticky="nsew")

            self.home_frame_5_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_5, text="", image=self.banner_image_caja)
            self.home_frame_5_banner_image_empleados_label.grid(row=0, column=0, padx=5, pady=0)

            self.home_frame_5_label_producto = customtkinter.CTkLabel(self.frame_5, text="1. Seleccione el o los productos:", fg_color="transparent")
            self.home_frame_5_label_producto.grid(row=1, column=0, padx=(0,250), pady=0)
            
            self.values_menu_products()

            self.home_frame_5_label_cantidad = customtkinter.CTkLabel(self.frame_5, text="2. Escriba la cantidad:", fg_color="transparent")
            self.home_frame_5_label_cantidad.grid(row=2, column=0, padx=(0,310), pady=0)
            self.home_frame_5_entry_cantidad = customtkinter.CTkEntry(self.frame_5, width=40)
            self.home_frame_5_entry_cantidad.grid(row=2,column=0,padx=(0,140),pady=0)
            self.home_frame_5_button_2 = customtkinter.CTkButton(self.frame_5, text="Agregar al carrito", width=20, command=self.add_to_cart)
            self.home_frame_5_button_2.grid(row=2, column=0, padx=(325, 0), pady=0)
            self.home_frame_5_button_3 = customtkinter.CTkButton(self.frame_5, text="", image=self.editar, width=20, command=self.edit_selected_item)
            self.home_frame_5_button_3.grid(row=2, column=0, padx=(160,0), pady=0)
            self.home_frame_5_button_4 = customtkinter.CTkButton(self.frame_5, text="", image=self.eliminar, width=20, command=lambda:self.clear_cart(self.carrito))
            self.home_frame_5_button_4.grid(row=2, column=0, padx=(70, 0), pady=0)
            
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

            self.treeview_carrito = ttk.Treeview(self.frame_5, style="Treeview", height=3)           
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

            self.treeview_carrito.bind("<ButtonRelease-1>", self.select_product)

            self.treeview_carrito_scrollbar = customtkinter.CTkScrollbar(self.frame_5, height=104, command=self.treeview_carrito.yview)
            self.treeview_carrito_scrollbar.grid(row=3, column=0,padx=(420,0))

            self.home_frame_5_label_dni = customtkinter.CTkLabel(self.frame_5, text="3. DNI Cliente:", fg_color="transparent")
            self.home_frame_5_label_dni.grid(row=4, column=0, padx=(0,350), pady=0)
            self.home_frame_5_entry_dni = customtkinter.CTkEntry(self.frame_5, width=120)
            self.home_frame_5_entry_dni.grid(row=4,column=0,padx=(0,140),pady=0)

            self.home_frame_5_entry_dni.configure(validate="key", validatecommand=(self.register(self.validate_dni), "%P"))

            self.home_frame_5_label_total = customtkinter.CTkLabel(self.frame_5, text="4. Precio total:", fg_color="transparent")
            self.home_frame_5_label_total.grid(row=5, column=0, padx=(0,350), pady=20)
            self.home_frame_5_entry_total = customtkinter.CTkEntry(self.frame_5, width=120)
            self.home_frame_5_entry_total.grid(row=5,column=0,padx=(0,140),pady=20)

            self.home_frame_5_button_5 = customtkinter.CTkButton(self.frame_5, text="Vender", width=20, command=lambda:self.perform_sale(self.carrito))
            self.home_frame_5_button_5.grid(row=6, column=0, padx=(0, 400), pady=30)
        else:
            self.frame_5.grid_forget()

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
            elif (column0 == "Administración"):
                self.frame_2_button.configure(state="enabled")
            elif (column0 == "Rrhh"):
                self.frame_3_button.configure(state="enabled")
            elif (column0 == "Depósito"):
                self.frame_4_button.configure(state="enabled")
            elif (column0 == "Caja"):
                self.frame_5_button.configure(state="enabled")
        else:
            self.home_frame_label_5 = customtkinter.CTkLabel(self.home_frame, text="Usuario no encontrado.", text_color="red")
            self.home_frame_label_5.place(x=195, y=380)

            def after_user_error():
                self.home_frame_label_5.destroy()

            self.home_frame.after(3500,after_user_error)

    #Functions frames

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")
    
    #Frame 2 functions
    
    def treeview_compra_show(self, treeview_compra):

        try:
            conn = sqlite3.connect("fravega_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, area, fecha, prod, deta FROM adm_c")
            fetchall = cursor.fetchall()
            conn.close()

            for fila in treeview_compra.get_children():
                treeview_compra.delete(fila)

            for dato in fetchall:
                treeview_compra.insert("", "end", values=dato)

        except sqlite3.Error as error:
            mensaje_error = "Error al acceder a la base de datos: " + str(error)
            tk.messagebox.showerror("Error", mensaje_error)

    def treeview_venta_show(self, treeview_venta):

        try:
            conn = sqlite3.connect("fravega_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, fecha, prod, cant, precio FROM adm_v")
            fetchall = cursor.fetchall()
            conn.close()

            for fila in treeview_venta.get_children():
                treeview_venta.delete(fila)

            for dato in fetchall:
                treeview_venta.insert("", "end", values=dato)

        except sqlite3.Error as error:
            mensaje_error = "Error al acceder a la base de datos: " + str(error)
            tk.messagebox.showerror("Error", mensaje_error)

    def clear_selection_compra(self):    

        self.treeview_compra.selection_remove(self.treeview_compra.focus())

    def clear_selection_venta(self):

        self.treeview_venta.selection_remove(self.treeview_venta.focus())

    #Frame 3 functions 

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

    def treeview_empleados_delete(self,treeview_empleados):

        selected_item = self.treeview_empleados.selection()

        if not selected_item:
            messagebox.showinfo("Información", "Seleccione un empleado para eliminar.")
        else:
            # Continuar con el proceso de eliminación
            dni = self.home_frame_3_entry_dni.get()
            nya = self.home_frame_3_entry_nombreyapellido.get()
            area = self.home_frame_3_entry_area.get()
            salario = self.home_frame_3_entry_salario.get()
            doc = self.home_frame_3_entry_documentación.get()
            img = self.home_frame_3_entry_imagen.get()

            if not dni or not nya or not area or not salario or not doc:
                messagebox.showinfo("Información", "Complete todos los campos antes de eliminar.")
            else:
                question = messagebox.askquestion("Cuidado", "¿Desea eliminar definitivamente el empleado?")

                if question == "yes":
                    dni = self.home_frame_3_entry_dni.get()
                    try:
                        conexion = sqlite3.connect("fravega_data.db")
                        cursor = conexion.cursor()

                        cursor.execute("DELETE FROM rh WHERE dni = ?", (dni,))
                        conexion.commit()
                        conexion.close()

                        self.clear_entries_and_selection_empleados()
                        self.refresh_treeview_empleados()

                        messagebox.showinfo("Información", "El empleado fue dado de baja.")

                    except sqlite3.Error as error:
                        mensaje_error = "Error al acceder a la base de datos " + str(error)
                        messagebox.showerror("Error", mensaje_error)
                else:
                    return
        
    def treeview_empleados_modify(self,treeview_empleados):

        selected_item = self.treeview_empleados.selection()

        if not selected_item:
            messagebox.showinfo("Información", "Seleccione un empleado para modificar.")
        else:
            # Continuar con el proceso de modificación
            dni = self.home_frame_3_entry_dni.get()
            nya = self.home_frame_3_entry_nombreyapellido.get()
            area = self.home_frame_3_entry_area.get()
            salario = self.home_frame_3_entry_salario.get()
            doc = self.home_frame_3_entry_documentación.get()
            img = self.home_frame_3_entry_imagen.get()

            if not dni or not nya or not area or not salario or not doc:
                messagebox.showinfo("Información", "Complete todos los campos antes de modificar.")
            else:
                question = messagebox.askquestion("Cuidado", "¿Desea modificar el empleado?")

                if question == "yes":
                    conexion = sqlite3.connect("fravega_data.db")
                    cursor = conexion.cursor()

                    question = messagebox.askquestion("Cuidado", "¿Desea modificar la imagen?")
                    if question == "yes":
                        self.load_image()
                        img = self.home_frame_3_entry_imagen.get()
                        cursor.execute("UPDATE rh SET nya=?, area=?, sal=?,doc=?,img=? WHERE dni=?", (nya, area, salario, doc, img, dni))
                    elif question == "no":
                        cursor.execute("UPDATE rh SET nya=?, area=?, sal=?,doc=? WHERE dni=?", (nya, area, salario, doc, dni))
                    conexion.commit()
                    conexion.close()

                    self.clear_entries_and_selection_empleados()
                    self.refresh_treeview_empleados()

                    messagebox.showinfo("Información", "El empleado fue modificado.")
                else:
                    return

    def treeview_empleados_add(self):

        dni = self.home_frame_3_entry_dni.get()
        nya = self.home_frame_3_entry_nombreyapellido.get()
        area = self.home_frame_3_entry_area.get()
        salario = self.home_frame_3_entry_salario.get()
        doc = self.home_frame_3_entry_documentación.get()
        img = self.home_frame_3_entry_imagen.get()
    
        if not dni or not nya or not area or not salario or not doc:
            messagebox.showinfo("Información", "Complete todos los campos.")
        else:       

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
                    mensaje_error = "Error al acceder a la base de datos: " + str(error)
                    messagebox.showerror("Error", mensaje_error)
                    return True

            question = messagebox.askquestion("Cuidado", "¿Desea agregar este nuevo empleado?")

            if question == "yes":
                dni = self.home_frame_3_entry_dni.get()
                nya = self.home_frame_3_entry_nombreyapellido.get()
                area = self.home_frame_3_entry_area.get()
                salario = self.home_frame_3_entry_salario.get()
                doc = self.home_frame_3_entry_documentación.get()            
                img = self.home_frame_3_entry_imagen.get()

                if not dni or not nya or not area or not salario or not doc:
                    messagebox.showwarning("Cuidado", "Por favor, complete todos los campos.")
                    return

                if dni_verification(dni):
                    messagebox.showwarning("Cuidado", "El DNI ya está registrado. No se puede agregar nuevamente.")
                    return
                
                question = messagebox.askquestion("Cuidado","¿Desea agregar una imagen?")

                if (question == "yes"):

                    try:
                        self.load_image()
                        img = self.home_frame_3_entry_imagen.get()

                        conexion = sqlite3.connect("fravega_data.db")
                        cursor = conexion.cursor()
                        cursor.execute("INSERT INTO rh (dni, nya, area, sal, doc, img) VALUES (?, ?, ?, ?, ?, ?)",(dni, nya, area, salario, doc, img))
                        conexion.commit()
                        conexion.close()

                        self.clear_entries_and_selection_empleados()
                        self.refresh_treeview_empleados()

                        messagebox.showinfo("Información", "El empleado fue dado de alta.")

                    except sqlite3.Error as error:
                        mensaje_error = "Error al acceder a la base de datos " + str(error)
                        messagebox.showerror("Error", mensaje_error)

                elif (question == "no"):
                    messagebox.showwarning("Cuidado","Si o sí deberá cargar una imagen del empleado.")                  
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

    def clear_entries_and_selection_empleados(self):

        self.home_frame_3_entry_dni.delete(0, tk.END)
        self.home_frame_3_entry_nombreyapellido.delete(0, tk.END)
        self.home_frame_3_entry_area.delete(0, tk.END)
        self.home_frame_3_entry_salario.delete(0, tk.END)
        self.home_frame_3_entry_imagen.delete(0, tk.END)
        self.home_frame_3_entry_documentación.delete(0, tk.END)
        self.home_frame_3_entry_imagen.delete(0, tk.END)
        self.home_frame_3_label_imagen.destroy()
        
        self.treeview_empleados.selection_remove(self.treeview_empleados.focus())
               
    def load_image(self):
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen", filetypes=[("Imagen", "*.png;*.jpg;*.jpeg")])
        self.home_frame_3_entry_imagen.delete(0, tk.END)
        self.home_frame_3_entry_imagen.insert(0, ruta_imagen)
    
    def refresh_treeview_empleados(self):
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

    #Frame 4 functions

    def treeview_deposito_show(self, treeview_deposito):
        try:
            conn = sqlite3.connect("fravega_data.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id,prod,cant,precio FROM dep")
            fetchall = cursor.fetchall()
            conn.close()

            for fila in treeview_deposito.get_children():
                treeview_deposito.delete(fila)

            for dato in fetchall:
                treeview_deposito.insert("", "end", values=dato)

        except sqlite3.Error as error:
            mensaje_error = "Error al acceder a la base de datos: " + str(error)
            tk.messagebox.showerror("Error", mensaje_error)

    def treeview_deposito_show_entry(self, event, treeview_deposito):
        seleccion = treeview_deposito.selection()
        if seleccion:
            item = treeview_deposito.item(seleccion[0], "values")
            self.home_frame_4_entry_id.delete(0, tk.END)
            self.home_frame_4_entry_id.insert(0, item[0])
            self.home_frame_4_entry_producto.delete(0, tk.END)
            self.home_frame_4_entry_producto.insert(0, item[1])
            self.home_frame_4_entry_cantidad.delete(0, tk.END)
            self.home_frame_4_entry_cantidad.insert(0, item[2])
            self.home_frame_4_entry_precio.delete(0, tk.END)
            self.home_frame_4_entry_precio.insert(0, item[3])

    def treeview_deposito_delete(self):

        id = self.home_frame_4_entry_id.get()
        prod = self.home_frame_4_entry_producto.get()
        cant = self.home_frame_4_entry_cantidad.get()
        precio = self.home_frame_4_entry_precio.get()

        if not id or not prod or not cant or not precio:
            messagebox.showinfo("Información","No hay producto para eliminar.")
        else:              
            question = messagebox.askquestion("Cuidado","¿Desea eliminar definitivamente el producto?")

            if (question == "yes"):
                id = self.home_frame_4_entry_id.get()
                try:
                    conexion = sqlite3.connect("fravega_data.db")
                    cursor = conexion.cursor()

                    cursor.execute("DELETE FROM dep WHERE id=?", (id,))
                    conexion.commit()
                    conexion.close()

                    self.clear_entries_and_selection_deposito()
                    self.refresh_treeview_deposito()
                
                    messagebox.showinfo("Información","El producto fue dado de baja.")

                except sqlite3.Error as error:
                    mensaje_error = "Error al acceder a la base de datos: " + str(error)
                    tk.messagebox.showerror("Error", mensaje_error)
            else:
                return
        
    def treeview_deposito_modify(self):

        id = self.home_frame_4_entry_id.get()
        prod = self.home_frame_4_entry_producto.get()
        cant = self.home_frame_4_entry_cantidad.get()
        precio = self.home_frame_4_entry_precio.get()

        if not id or not prod or not cant or not precio:
            messagebox.showinfo("Información","No hay producto para modificar.")
        else:        
            question = messagebox.askquestion("Cuidado","Desea modificar el producto?")

            if (question == "yes"):            
                conexion = sqlite3.connect("fravega_data.db")
                cursor = conexion.cursor()
                cursor.execute("UPDATE dep SET prod=?,cant=?,precio=? WHERE id=?", (prod, cant, precio, id))
                conexion.commit()
                conexion.close()

                self.clear_entries_and_selection_deposito()
                self.refresh_treeview_deposito()

                messagebox.showinfo("Información","El producto fue modificado.")
            else:
                return

    def treeview_deposito_add(self):

        id = self.home_frame_4_entry_id.get()
        prod = self.home_frame_4_entry_producto.get()
        cant = self.home_frame_4_entry_cantidad.get()
        precio = self.home_frame_4_entry_precio.get()

        # Verifica que se completen todos los campos
        if not id or not prod or not cant or not precio:
            messagebox.showinfo("Información", "Complete todos los campos.")
        else:
            question = messagebox.askquestion("Cuidado", "¿Desea agregar este nuevo producto?")

            if question == "yes":
                if not prod or not cant or not precio:
                    messagebox.showwarning("Cuidado", "Por favor, complete todos los campos.")
                    return
                else:
                    try:
                        conexion = sqlite3.connect("fravega_data.db")
                        cursor = conexion.cursor()

                        cursor.execute("SELECT COUNT(*) FROM dep WHERE id = ?", (id,))
                        existe = cursor.fetchone()[0]

                        if existe > 0:
                            messagebox.showwarning("Cuidado", "El producto con el ID {} ya existe.".format(id))
                        else:
                            cursor.execute("INSERT INTO dep (id, prod, cant, precio) VALUES (?, ?, ?, ?)", (id, prod, cant, precio))
                            conexion.commit()
                            conexion.close()

                            self.clear_entries_and_selection_deposito()
                            self.refresh_treeview_deposito()

                            messagebox.showinfo("Información", "El producto fue dado de alta.")

                    except sqlite3.Error as error:
                        mensaje_error = "Error al acceder a la base de datos: " + str(error)
                        tk.messagebox.showerror("Error", mensaje_error)
            else:
                return
    
    def clear_entries_and_selection_deposito(self):
    
        self.home_frame_4_entry_id.delete(0, tk.END)
        self.home_frame_4_entry_producto.delete(0, tk.END)
        self.home_frame_4_entry_cantidad.delete(0, tk.END)
        self.home_frame_4_entry_precio.delete(0, tk.END)

        self.treeview_deposito.selection_remove(self.treeview_deposito.focus())
    
    def refresh_treeview_deposito(self):
        for record in self.treeview_deposito.get_children():
            self.treeview_deposito.delete(record)

        conexion = sqlite3.connect("fravega_data.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id,prod,cant,precio FROM dep")
        productos = cursor.fetchall()
        for producto in productos:
            self.treeview_deposito.insert("", "end", values=producto)

        conexion.close()

        for col in ["Id", "Producto", "Cantidad", "Precio"]:
            self.treeview_deposito.heading(col, anchor=tk.W)
            self.treeview_deposito.column(col, anchor=tk.W)

    #Frame 5 functions 

    def values_menu_products(self):
        self.conn = sqlite3.connect("fravega_data.db")
        self.cursor = self.conn.cursor()

        query = "SELECT prod FROM dep WHERE cant > 1"
        self.cursor.execute(query)
        product_names = [row[0] for row in self.cursor.fetchall()]

        self.home_frame_5_menu_producto = customtkinter.CTkComboBox(self.frame_5, values=product_names, width=250)
        self.home_frame_5_menu_producto.grid(row=1, column=0, padx=(190, 0), pady=20)

        self.home_frame_5_menu_producto.set("Seleccione producto")
        self.home_frame_5_menu_producto.configure(state="readonly")

    def add_to_cart(self):
        producto_seleccionado = self.home_frame_5_menu_producto.get()

        if not producto_seleccionado or producto_seleccionado == "Seleccione producto":
            messagebox.showinfo("Información", "Por favor, seleccione un producto antes de agregarlo al carrito.")
            return

        cantidad = self.home_frame_5_entry_cantidad.get()

        if not cantidad.isdigit() or int(cantidad) <= 0:
            messagebox.showinfo("Información", "Por favor, ingrese una cantidad válida mayor a 0.")
            return

        cantidad = int(cantidad)
        producto_seleccionado = self.home_frame_5_menu_producto.get()
        cantidad = int(self.home_frame_5_entry_cantidad.get())

        query = f"SELECT id, prod, precio, cant FROM dep WHERE prod = '{producto_seleccionado}'"
        self.cursor.execute(query)
        producto_info = self.cursor.fetchone()

        if producto_info:
            
            producto_id, producto_nombre, producto_precio, stock_disponible = producto_info

            if cantidad > stock_disponible:
                messagebox.showerror("Error", f"La cantidad ingresada es mayor al stock disponible. Stock disponible: {stock_disponible}")
            elif cantidad <= 0:
                messagebox.showerror("Error", "La cantidad ingresada debe ser mayor a 0.")
            else:
                # Verificar si el producto ya está en el carrito
                for item in self.carrito:
                    if item["producto"] == producto_seleccionado:
                        messagebox.showinfo("Información", "Este producto ya está en el carrito.")
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
                
                self.home_frame_5_menu_producto.set("Seleccione producto")
                self.home_frame_5_entry_cantidad.delete(0, tk.END)

                # Actualizar la vista del Treeview
                self.update_treeview_cart()

            # Restaurar el valor del Entry de cantidad
            self.home_frame_5_entry_cantidad.delete(0, tk.END)
            self.home_frame_5_menu_producto.set("Seleccione producto")
        else:
            messagebox.showerror("Error", "El producto seleccionado no se encontró en la base de datos.")

    def edit_selected_item(self):
        
        elemento_seleccionado = self.treeview_carrito.focus()

        if not elemento_seleccionado:
            messagebox.showinfo("Información", "Por favor, seleccione un elemento en el carrito para editar.")
            return

        valores_elemento = self.treeview_carrito.item(elemento_seleccionado, "values")
        producto_id, producto_nombre, _, _ = valores_elemento

        for idx, item in enumerate(self.carrito):
            if item["producto"] == producto_nombre:
                nueva_cantidad = self.home_frame_5_entry_cantidad.get()

                if not nueva_cantidad.isdigit() or int(nueva_cantidad) <= 0:
                    messagebox.showinfo("Información", "Por favor, ingrese una cantidad válida mayor a 0.")
                    return

                nueva_cantidad = int(nueva_cantidad)

                query = f"SELECT id, prod, precio, cant FROM dep WHERE prod = '{producto_nombre}'"
                self.cursor.execute(query)
                producto_info = self.cursor.fetchone()

                if producto_info:
                    _, _, _, stock_disponible = producto_info

                    if nueva_cantidad > stock_disponible:
                        messagebox.showinfo("Información", f"La cantidad ingresada supera el stock disponible ({stock_disponible}).")
                        return

                self.carrito[idx]["cantidad"] = nueva_cantidad

                self.update_treeview_cart()

                self.home_frame_5_menu_producto.set("Seleccione producto")
                self.home_frame_5_entry_cantidad.delete(0, tk.END)
                return

    def clear_cart(self, carrito):

        if not carrito:
            messagebox.showinfo("Información","No hay productos a eliminar.")
        else:
            respuesta = messagebox.askyesno("Limpiar Carrito", "¿Desea limpiar el carrito?")
            if respuesta:
                self.carrito = []
                self.update_treeview_cart()  
                self.update_total_price()   

                self.home_frame_5_menu_producto.set("Seleccione producto")
                self.home_frame_5_entry_cantidad.delete(0, tk.END)
                self.home_frame_5_entry_total.configure(state="normal")
                self.home_frame_5_entry_total.delete(0, "end")

    def update_treeview_cart(self):
        self.treeview_carrito.delete(*self.treeview_carrito.get_children())
        for item in self.carrito:
            self.treeview_carrito.insert("", "end", values=(
                item["id"],
                item["producto"],
                item["cantidad"],
                item["precio_unitario"]
            ))
        self.update_total_price()
                
    def update_total_price(self):
        self.home_frame_5_entry_total.configure(state="normal")
        self.total_venta = sum(item["precio_total"] for item in self.carrito)
        self.home_frame_5_entry_total.delete(0, "end")
        self.home_frame_5_entry_total.insert(0, self.total_venta)
        self.home_frame_5_entry_total.configure(state="readonly")

    def select_product(self, event):
        selected_item = self.treeview_carrito.selection()
        if selected_item:
            item_producto = self.treeview_carrito.item(selected_item, "values")[1]
            item_cantidad = self.treeview_carrito.item(selected_item, "values")[2]

            self.home_frame_5_menu_producto.set(item_producto)
            self.home_frame_5_entry_cantidad.delete(0, tk.END)
            self.home_frame_5_entry_cantidad.insert(0, item_cantidad)

    def perform_sale(self, carrito):

        dni_frame_5 = self.home_frame_5_entry_dni.get()

        if not dni_frame_5:
            messagebox.showinfo("Información","Debe colocar el DNI.")
        elif not carrito:
            messagebox.showinfo("Cuidado","Debe agregar un producto para vender.")
        else:

            current_dir = os.path.dirname(os.path.abspath(__file__))

            image_path = os.path.join(current_dir, "images", "fravega_factura.png")

            fecha_hora_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            fecha_actual = datetime.now().strftime("%Y-%m-%d")
            pdf_filename = os.path.join(current_dir, "tickets", f"ticket_{fecha_hora_actual}.pdf")

            subtotal = sum(item["precio_total"] for item in self.carrito)
            total_iva = subtotal * 0.21
            total_con_iva = subtotal + total_iva

            doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

            story = []

            def add_background(canvas, doc):
                canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])

            doc.build(story, onFirstPage=add_background, onLaterPages=add_background)

            story.append(Spacer(1, (letter[1] - 300) / 2)) 

            style_normal = getSampleStyleSheet()['Normal']

            #Table list for dni and dat
            dni_fecha_data = [
                ["", dni_frame_5, "", fecha_actual]
            ]

            dni_table = Table(dni_fecha_data, colWidths=[100, 200, 100, 100])
            dni_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
            ]))

            story.insert(0, dni_table)

            story.append(Spacer(1, 0))

            #Table list for products
            carrito_data = []
            for item in self.carrito:
                producto_nombre = item["producto"]
                cantidad = item["cantidad"]
                precio_unitario = f"${item['precio_unitario']:.2f}"
                precio_total = f"${item['precio_total']:.2f}"

                carrito_data.append([producto_nombre, cantidad, precio_unitario, precio_total])

            table = Table(carrito_data, colWidths=[310, 50, 60, 65])

            table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ]))

            story.append(table)

            #Table list for totals
            totals_data = [
                [f"", Paragraph(f"${subtotal:.2f}", style_normal)],
                [f"", Paragraph(f"${total_iva:.2f}", style_normal)],
                [f"", Paragraph(f"${total_con_iva:.2f}", style_normal)],
            ]

            totals_table = Table(totals_data, colWidths=[420, 100])
            totals_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'RIGHT'), 
            ]))

            story.append(Spacer(1, 183))
            story.append(totals_table)

            doc.build(story)

            messagebox.showinfo("Información", "Se realizó la venta correctamente.")


            self.carrito = []
            self.home_frame_5_menu_producto.set("Seleccione producto")
            self.home_frame_5_entry_dni.delete(0, tk.END)
            self.home_frame_5_entry_cantidad.delete(0, tk.END)
            self.home_frame_5_entry_total.configure(state="normal")
            self.home_frame_5_entry_total.delete(0, "end")
            self.treeview_carrito.delete(*self.treeview_carrito.get_children())

            subprocess.Popen([pdf_filename], shell=True)
            
    #Appearance 

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.home_button_event()
        self.home_frame_3_label_dni = customtkinter.CTkLabel(self.home_frame, text="Tema cambiado exitosamente", fg_color="transparent", text_color="#0AC90A")
        self.home_frame_3_label_dni.grid(row=8,column=0)

        def after_theme_changed():
                self.carrito = []
                self.home_frame_5_menu_producto.set("Seleccione producto")
                self.home_frame_5_entry_dni.delete(0, tk.END)
                self.home_frame_5_entry_cantidad.delete(0, tk.END)
                self.home_frame_5_entry_total.configure(state="normal")
                self.home_frame_5_entry_total.delete(0, "end")
                self.treeview_carrito.delete(*self.treeview_carrito.get_children())

        self.home_frame.after(2500,after_theme_changed)

if __name__ == "__main__":
    app = App()
    app.iconbitmap("images/fravega.ico")
    app.resizable(0,0)
    app.mainloop()