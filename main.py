"""
Created on Aug 17, 2011

@author: Mikhail Denisenko

NEEDS https://github.com/twain/twain-dsm
https://github.com/twain/twain-dsm/tree/master/Releases/dsm_020403/windows/64

"""
from io import BytesIO
import twain
import tkinter
from tkinter import ttk
import logging
from PIL import Image, ImageTk

# root = Tk()
# root.title("scan.py")
#
# if len(sys.argv) != 2:
#     messagebox.showerror("Error", "Usage: python scan.py <filename>")
#     exit(1)
#
# outpath = sys.argv[1]
#
#
# def scan():
#     try:
#         result = twain.acquire(
#             outpath,
#             ds_name="C:/Windows/System32/twain_32/", # C:\Windows\System32\twain_32
#             dpi=300,
#             frame=(0, 0, 8.17551, 11.45438),  # A4
#             pixel_type="bw",
#             parent_window=root,
#         )
#     except:
#         messagebox.showerror("Error", traceback.format_exc())
#         sys.exit(1)
#     else:
#         sys.exit(0 if result else 1)
#
#
# root.after(1, scan)
# root.mainloop()
#
# from io import BytesIO
# import twain
# import tkinter
# from tkinter import ttk
# import logging
# import PIL.ImageTk
# import PIL.Image
#
# scanned_image = None

root = tkinter.Tk()
root.title("Scan Utility")
root.geometry("240x150")

scanner_list = twain.SourceManager(root)


class ScanUtility:

    def __init__(self, sm=None, ds_id=None):
        self.sm = sm
        self.src = None
        self.frm = ttk.Frame(root, padding=10)
        self.frm.grid()
        self.scanned_image = Image
        ttk.Button(self.frm, text="Select source", command=self.select_src).grid(column=0, row=0)
        ttk.Button(self.frm, text="Scan", command=self.scan).grid(column=0, row=1)

    def select_src(self):
        # this will show UI to allow user to select source
        self.src = self.sm.open_source()
        if not self.src:
            logging.error("No source selected")

    def scan(self):
        # this will show UI to allow user to select source
        if self.src:
            self.src.request_acquire(show_ui=False, modal_ui=False)
            (handle, remaining_count) = self.src.xfer_image_natively()
            bmp_bytes = twain.dib_to_bm_file(handle)
            img = Image.open(BytesIO(bmp_bytes), formats=["bmp"])
            width, height = img.size
            factor = 600.0 / width
            # Storing PhotoImage in global variable to prevent it from being deleted once this function exits
            # since PhotoImage has a __del__ destructor
            self.scanned_image = ImageTk.PhotoImage(img.resize(size=(int(width * factor), int(height * factor))))
            self.frm.destroy()
            ttk.Label(root, image=self.scanned_image).pack(side="left", fill="both", expand=1)
        else:
            print("User clicked cancel")


logging.basicConfig(level=logging.DEBUG)



# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scan = ScanUtility(scanner_list)
    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
