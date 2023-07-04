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

        class TreeViewStyle1():

            style = ttk.Style()
            style.theme_use("default")    
            style.configure("Treeview",
                            background="#2a2d2e",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="gray14",
                            bordercolor="#343638",
                            borderwidth=0)
            style.map('Treeview', background=[('selected', '#b01685')])
        
            style.configure("Treeview.Heading",
                            background="gray13",
                            foreground="white",
                            relief="flat")
            style.map("Treeview.Heading",
                    background=[('active', '#b01685')])
            
        class TreeViewStyle2():

            style = ttk.Style()
            style.theme_use("default")    
            style.configure("Treeview",
                            background="red",
                            foreground="black",
                            rowheight=25,
                            fieldbackground="gray14",
                            bordercolor="#343638",
                            borderwidth=0)
            style.map('Treeview', background=[('selected', '#b01685')])
        
            style.configure("Treeview.Heading",
                            background="red",
                            foreground="white",
                            relief="flat")
            style.map("Treeview.Heading",
                    background=[('active', '#b01685')])

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(26, 26))
        self.banner_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner.png")), size=(500, 150))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "inicio.png")), size=(20, 20))
        self.admin_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "admin.png")), size=(20, 20))
        self.rrhh_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "rrhh.png")), size=(20, 20))
        self.deposito_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "deposito.png")), size=(20, 20))
        self.entregas_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "entregas.png")), size=(20, 20))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(6, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  FRÁVEGA", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont("Calibri",size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

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
            self.frame_2.grid(row=0, column=1, sticky="nsew")

            treeview = ttk.Treeview(self.frame_2, style="Treeview")
            treeview["columns"] = ("ganancias", "perdidas")
            treeview.column("#0", width=100, minwidth=100, stretch=tk.NO)
            treeview.column("ganancias", width=100, minwidth=100, stretch=tk.NO)
            treeview.column("perdidas", width=100, minwidth=100, stretch=tk.NO)
            treeview.heading("#0", text="Ganancias")
            treeview.heading("ganancias", text="Perdidas")
            treeview.heading("perdidas", text="ASLDKASJ")
            treeview.grid(row=0,column=0)
        else:
            self.frame_2.grid_forget()
        if name == "frame_3":
            self.frame_3.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_3.grid_forget()
        if name == "frame_4":
            self.frame_4.grid(row=0, column=1, sticky="nsew")
        else:
            self.frame_4.grid_forget()
        if name == "frame_5":
            self.frame_5.grid(row=0, column=1, sticky="nsew")
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
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        data = (self.home_frame_entry_1.get(), self.home_frame_entry_2.get())
        cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND clave = ?", (data))
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

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.iconbitmap("test_images/fravega.ico")
    app.resizable(0,0)
    app.mainloop()