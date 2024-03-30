import tkinter as tk
from tkinter import Tk, font, Frame, Button


class App:
    def __init__(self, root):
        # setting title
        root.title("Scanner utility")
        root.configure(background="white")
        # control-outline-color: #FFBF63

        # setting window size
        width = 350
        height = 180

        # Creating a Font object of "TkDefaultFont"
        self.defaultFont = font.nametofont("TkDefaultFont")

        # Overriding default-font with custom settings
        # i.e changing font-family, size and weight
        self.defaultFont.configure(family="Noto Sans",
                                   size=12,
                                   weight=font.BOLD)

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        buttonFrame = Frame(root, bg="gray")
        buttonFrame.pack()
        borderFrame = Frame(buttonFrame, highlightbackground="#FFBF63", highlightcolor="#FFBF63",
                            highlightthickness=4, relief="flat")
        borderFrame.pack()
        btn_scan = Button(borderFrame, relief="flat", bg="white")
        btn_scan["justify"] = "center"
        btn_scan["text"] = "Scan"
        btn_scan.place(x=20, y=60, width=90, height=90)
        btn_scan.pack(side="left")
        btn_scan["command"] = self.GButton_893_command

        borderFrame2 = Frame(buttonFrame, highlightbackground="#FFBF63", highlightcolor="#FFBF63",
                            highlightthickness=4, relief="flat")
        borderFrame2.pack()
        btn_scan2pdf = Button(borderFrame2, borderwidth=2, relief="flat", bg="white")
        btn_scan2pdf["justify"] = "center"
        btn_scan2pdf["text"] = "Scan to PDF"
        # btn_scan2pdf.place(x=120, y=60, width=90, height=90)
        btn_scan2pdf.pack()
        btn_scan2pdf["command"] = self.GButton_899_command

        borderFrame3 = Frame(buttonFrame, highlightbackground="#FFBF63", highlightcolor="#FFBF63",
                            highlightthickness=4, relief="flat")
        borderFrame3.pack()
        btn_settings = Button(borderFrame3, borderwidth=2, relief="flat", bg="white")
        btn_settings["justify"] = "center"
        btn_settings["text"] = "Settings"
        btn_settings.place(x=220, y=60, width=90, height=90)
        btn_settings.pack()
        btn_settings["command"] = self.GButton_857_command

    def GButton_893_command(self):
        print("command")

    def GButton_899_command(self):
        print("command")

    def GButton_857_command(self):
        print("command")

    def GButton_482_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
