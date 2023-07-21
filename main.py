import customtkinter
import os
from PIL import Image
import webbrowser
import sqlite3
import tkinter as tk
from tkinter import ttk

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestión")
        self.geometry("700x450")
        customtkinter.set_default_color_theme("theme/fravega.json")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner.png")), size=(480, 150))
        self.banner_image_compra = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner_compra.png")), size=(500, 50))
        self.banner_image_venta = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner_venta.png")), size=(500, 50))
        self.banner_image_empleados = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner_empleados.png")), size=(500, 50))
        self.banner_image_deposito = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner_deposito.png")), size=(500, 50))
        self.banner_image_entregas = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner_entregas.png")), size=(500, 50))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "inicio.png")), size=(20, 20))
        self.admin_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "admin.png")), size=(20, 20))
        self.rrhh_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "rrhh.png")), size=(20, 20))
        self.deposito_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "deposito.png")), size=(20, 20))
        self.entregas_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "entregas.png")), size=(20, 20))
        self.mensajes_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mensajes.png")), size=(20, 20))

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

            self.home_frame_2_button_1 = customtkinter.CTkButton(self.frame_2, text="Mensajes", image=self.mensajes_image,command=self.email_event)
            self.home_frame_2_button_1.grid(row=2, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_2_banner_image_compra_label = customtkinter.CTkLabel(self.frame_2, text="", image=self.banner_image_compra)
            self.home_frame_2_banner_image_compra_label.grid(row=3, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")    

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
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

            self.home_frame_3_button_1 = customtkinter.CTkButton(self.frame_3, text="Mensajes", image=self.mensajes_image)
            self.home_frame_3_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_3_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_3, text="", image=self.banner_image_empleados)
            self.home_frame_3_banner_image_empleados_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#E3E3E3", foreground="gray1", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])   

            self.treeview_empleados = ttk.Treeview(self.frame_3, style="Treeview", height=4)           
            self.treeview_empleados["columns"] = ("Nombre y Apellido", "Area", "Salario", "Asistencia")
            self.treeview_empleados.column("#0", width=40, minwidth=40, stretch=tk.NO)
            self.treeview_empleados.column("Nombre y Apellido", width=182, minwidth=182, stretch=tk.NO)
            self.treeview_empleados.column("Area", width=82, minwidth=82, stretch=tk.NO)
            self.treeview_empleados.column("Salario", width=82, minwidth=82, stretch=tk.NO)
            self.treeview_empleados.column("Asistencia", width=82, minwidth=82, stretch=tk.NO)
            self.treeview_empleados.heading("#0", text="DNI")
            self.treeview_empleados.heading("Nombre y Apellido", text="Nombre y Apellido")
            self.treeview_empleados.heading("Area", text="Area")
            self.treeview_empleados.heading("Salario", text="Salario")
            self.treeview_empleados.heading("Asistencia", text="Asistencia")
            self.treeview_empleados.grid(row=3,column=0,padx=5,pady=0)

            self.treeview_empleados_scrollbar = customtkinter.CTkScrollbar(self.frame_3, height=124, command=self.treeview_empleados.yview)
            self.treeview_empleados_scrollbar.grid(row=3, column=0,padx=(460,0))

            self.home_frame_3_label_dni = customtkinter.CTkLabel(self.frame_3, text="DNI", fg_color="transparent")
            self.home_frame_3_label_dni.place(x=65,y=247)
            self.home_frame_3_label_nombreyapellido = customtkinter.CTkLabel(self.frame_3, text="Nombre y Apellido", fg_color="transparent")
            self.home_frame_3_label_nombreyapellido.place(x=312,y=247)
            self.home_frame_3_label_area = customtkinter.CTkLabel(self.frame_3, text="Area", fg_color="transparent")
            self.home_frame_3_label_area.place(x=65,y=319)
            self.home_frame_3_label_salario = customtkinter.CTkLabel(self.frame_3, text="Salario", fg_color="transparent")
            self.home_frame_3_label_salario.place(x=312,y=319)
            
            self.home_frame_3_entry_dni = customtkinter.CTkEntry(self.frame_3, placeholder_text="Solo números")
            self.home_frame_3_entry_dni.grid(row=5,column=0,padx=(0,250),pady=40)
            self.home_frame_3_entry_nombreyapellido = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_nombreyapellido.grid(row=5,column=0,padx=(250,0),pady=40)
            self.home_frame_3_entry_area = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_area.grid(row=6,column=0,padx=(0,250),pady=5)
            self.home_frame_3_entry_salario = customtkinter.CTkEntry(self.frame_3)
            self.home_frame_3_entry_salario.grid(row=6,column=0,padx=(250,0),pady=5)

            self.home_frame_3_button_2 = customtkinter.CTkButton(self.frame_3, text="Modificar", width=20)
            self.home_frame_3_button_2.grid(row=7, column=0, padx=(120,0), pady=20)
            self.home_frame_3_button_3 = customtkinter.CTkButton(self.frame_3, text="Guardar", width=20)
            self.home_frame_3_button_3.grid(row=7, column=0, padx=(260,0), pady=20)
            self.home_frame_3_button_4 = customtkinter.CTkButton(self.frame_3, text="Eliminar", width=20)
            self.home_frame_3_button_4.grid(row=7, column=0, padx=(400,0), pady=20)
        else:
            self.frame_3.grid_forget()
        if name == "frame_4":
            self.frame_4.grid(row=0, column=1, sticky="nsew")

            self.home_frame_4_button_1 = customtkinter.CTkButton(self.frame_4, text="Mensajes", image=self.mensajes_image)
            self.home_frame_4_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_4_banner_image_deposito_label = customtkinter.CTkLabel(self.frame_4, text="", image=self.banner_image_deposito)
            self.home_frame_4_banner_image_deposito_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
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

            self.home_frame_5_button_1 = customtkinter.CTkButton(self.frame_5, text="Mensajes", image=self.mensajes_image)
            self.home_frame_5_button_1.grid(row=1, column=0, padx=5, pady=20,sticky="e")

            self.home_frame_5_banner_image_empleados_label = customtkinter.CTkLabel(self.frame_5, text="", image=self.banner_image_entregas)
            self.home_frame_5_banner_image_empleados_label.grid(row=2, column=0, padx=5, pady=0)

            style = ttk.Style()
            style.theme_use("default")

            if(self.appearance_mode_menu.get() == "Dark"):                
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#343638", bordercolor="#343638", borderwidth=0)
                style.map('Treeview', background=[('selected', '#b01685')])
            
                style.configure("Treeview.Heading", background="#2E2F31", foreground="white", relief="flat")
                style.map("Treeview.Heading", background=[('active', '#b01685')])
                                  
            elif(self.appearance_mode_menu.get() == "Light"):
                style.configure("Treeview", background="#b01685", foreground="#3B2682", rowheight=25, fieldbackground="#F9F9FA", bordercolor="#343638", borderwidth=0)
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
            elif (column0 == "Entregas"):
                self.frame_5_button.configure(state="enabled")
        else:
            self.home_frame_label_5 = customtkinter.CTkLabel(self.home_frame, text="Usuario no encontrado.", text_color="red")
            self.home_frame_label_5.place(x=195, y=380)

            def after_user_error():
                self.home_frame_label_5.destroy()

            self.home_frame.after(3500,after_user_error)

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")

    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def email_event(self):
        app_email = customtkinter.CTk()
        app_email.geometry("650x400")
        app_email.title("Email Fravega")

        app_email.mainloop()

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
    app.iconbitmap("test_images/fravega.ico")
    app.resizable(0,0)
    app.mainloop()