import logging
import customtkinter
import twain
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.sm = twain.SourceManager(self)
        self.default_res = "600 dpi"
        self.scanner_model = "Canon LiDE 25"

        # Set font
        customtkinter.FontManager.load_font("Noto_Sans.ttf")

        # configure window
        self.title(" Scan utility")
        self.geometry(f"{360}x{250}")
        self.resizable(False, True)
        self.configure(highlightbackground="#122F7B")
        self.iconbitmap('icons/scanner.ico')
        # self.overrideredirect(True)

        # configure grid layout (1x1)
        # a non-zero weight causes a row or column to grow if there's extra space
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=0)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=300, fg_color="white")
        self.tabview.grid(row=0, column=0, sticky="nsew")
        self.tabview.pack(fill="both", expand=True, padx=5, pady=5)
        self.tabview.add("Actions")
        self.tabview.add("Settings")
        self.tabview.add("Install")

        # you can configure grid of individual tabs
        self.tabview.tab("Actions").grid_columnconfigure(0, weight=0)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=0)

        # Main tab
        self.scanner_model_label = customtkinter.CTkLabel(self.tabview.tab("Actions"),
                                                          text="Scanner:")
        self.scanner_model_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.scanner_model_saved_label = customtkinter.CTkLabel(self.tabview.tab("Actions"),
                                                                justify="left",
                                                                text=self.scanner_model,
                                                                )
        self.scanner_model_saved_label.grid(row=0, column=1,
                                            columnspan=2,
                                            padx=20, pady=(20, 10),
                                            sticky="w")  # to justify left

        self.scan_button_image = customtkinter.CTkImage(light_image=Image.open("icons/scanner.64x64.png"),
                                                        dark_image=Image.open("icons/scanner.64x64.png"),
                                                        size=(60, 60))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Actions"),
                                                           text="",
                                                           command=self.open_input_dialog_event,
                                                           border_color="#FFBF63",
                                                           border_width=3,
                                                           fg_color="white",
                                                           text_color="black",
                                                           image=self.scan_button_image,
                                                           width=80, height=80)
        self.string_input_button.grid(row=2, column=0, padx=15, pady=(10, 10))
        self.scanner_button_label = customtkinter.CTkLabel(self.tabview.tab("Actions"),
                                                           font=("Nota Sans", 14),
                                                           text="Scan"
                                                           )
        self.scanner_button_label.grid(row=3, column=0, padx=15)  # , pady=(10, 10))

        self.scan_pdf_button_image = customtkinter.CTkImage(light_image=Image.open("icons/pdf.64x64.png"),
                                                            dark_image=Image.open("icons/scanner.64x64.png"),
                                                            size=(60, 60))
        self.scan_pdf_button = customtkinter.CTkButton(self.tabview.tab("Actions"),
                                                       image=self.scan_pdf_button_image,
                                                       text="",
                                                       font=("Nota Sans", 20),
                                                       border_color="#FFBF63",
                                                       border_width=3,
                                                       fg_color="white",
                                                       text_color="black",
                                                       command=print("Hello"),
                                                       width=80,
                                                       height=80)
        self.scan_pdf_button.grid(row=2, column=1, padx=15, pady=(10, 10))
        self.scan_pdf_button_label = customtkinter.CTkLabel(self.tabview.tab("Actions"),
                                                           font=("Nota Sans", 14),
                                                           text="Scan to PDF"
                                                           )
        self.scan_pdf_button_label.grid(row=3, column=1, padx=15)  # , pady=(10, 10))

        # Scan B&W
        self.scan_bw_button_image = customtkinter.CTkImage(light_image=Image.open("icons/black-and-white.64x64.png"),
                                                            dark_image=Image.open("icons/black-and-white.64x64.png"),
                                                            size=(60, 60))
        self.scan_button_bw = customtkinter.CTkButton(self.tabview.tab("Actions"),
                                                      text="",
                                                      image=self.scan_bw_button_image,
                                                      font=("Nota Sans", 20),
                                                      border_color="#FFBF63",
                                                      border_width=3,
                                                      fg_color="white",
                                                      text_color="black",
                                                      command=print("Hello B&W"),
                                                      width=80,
                                                      height=80)
        self.scan_button_bw.grid(row=2, column=2, padx=15, pady=(10, 10))
        self.scan_bw_button_label = customtkinter.CTkLabel(self.tabview.tab("Actions"),
                                                            font=("Nota Sans", 14),
                                                            text="Scan B&W"
                                                            )
        self.scan_bw_button_label.grid(row=3, column=2, padx=15)  # , pady=(10, 10))

        # Tab Settings
        self.label_tab_2 = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Source...",
                                                   command=self.select_src)
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("Settings"),
                                                    values=["My Scanner", "Value 2"])
        self.combobox_1.grid(row=0, column=1, padx=20, pady=(10, 10))

        self.res_label = customtkinter.CTkLabel(self.tabview.tab("Settings"),
                                                text="Resolution:")
        self.res_label.grid(row=1, column=0, padx=20, pady=(20, 10))
        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"),
                                                        dynamic_resizing=True,
                                                        values=["600 dpi", "300 dpi", "Value Long Long Long"])
        self.optionmenu_1.grid(row=1, column=1, padx=20, pady=(20, 10))

        self.check1_label = customtkinter.CTkButton(self.tabview.tab("Install"),
                                                    text="Check 32 bit",
                                                    command="")
        self.check1_label.grid(row=0, column=0, padx=20, pady=20)
        self.check2_label = customtkinter.CTkButton(self.tabview.tab("Install"),
                                                    text="Check DLLs",
                                                    command="")
        self.check2_label.grid(row=1, column=0, padx=20, pady=20)

        # set default values
        self.optionmenu_1.set(self.default_res)
        self.combobox_1.set("My Super long Scanner")

    def select_src(self):
        # this will show UI to allow user to select source
        self.src = self.sm.open_source()
        if not self.src:
            logging.error("No source selected")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    scanner_list = twain.SourceManager(app)
    app.mainloop()
