
import os
import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
import pandas as pd

print(f"Arguments: {sys.argv}")

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if arg.startswith("-")]

REWRITE_METADATA = False

if "-U" in opts:
    print("update Metadata.txt files")
    REWRITE_METADATA = True
if "-help" in args:
    # 
    print("""Used to manage testing filesystem
\t-help\tprints help message
\t-U\tRe-create or update all metadata files""")
    sys.exit()

#start new tk dialog window and hide it
root = tk.Tk()
root.withdraw()

# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename(initialfile="Tests.xlsx", filetypes=[("xlsx","*.xlsx"),("xls","*.xls"),("xlsm","*.xlsm"),("xlsb","*.xlsb"),("odf","*.odf"),("ods","*.ods"),("odt","*.odt")])

print(filename)

df = pd.read_excel(io=filename, header=0)

directory = os.path.dirname(filename)
print(f"directory: {directory}")
dirs = [f.name for f in os.scandir(directory) if f.is_dir()]
print(f"Current dirs: {dirs}")


for row in df.itertuples(index=False):
    try:
        if not pd.isna(row.Tool):
            prefix = ''
            for char in row.Tool:
                if char.isupper():
                    prefix += char
            prefix += str(f"{row.Test_Number:.0f}")
            print(f"prefix: {prefix}")
            if prefix not in dirs or REWRITE_METADATA:
                try:
                    folder_path = os.path.join(directory, prefix)
                    if not REWRITE_METADATA:
                        print(f"make dir: {prefix}")
                        os.mkdir(folder_path)
                    metadata_file_path = os.path.join(folder_path, prefix  + "_metadata.txt")
                    _file = open(metadata_file_path, "w+")
                    _file.write(
                            f"Test: {int(row.Test_Number)}\n" +
                            f"Tool: {row.Tool}\n" +
                            f"Location: {row.Location}\n" +
                            f"Orientation: {row.Orientation}\n" +
                            f"LP Filter: {row.LP_Filter}\n" +
                            f"Offset Cancelation: {row.Offset_cancelation}\n" +
                            f"Load: {row.Load}\n" +
                            f"Test Description: {row.Test_Description}\n")
                    _file.close()
                    
                    if not REWRITE_METADATA:
                        # Made empty Data.txt file
                        mag_file_path = os.path.join(folder_path, prefix + ".txt")
                        _file_mag = open(mag_file_path, "w")
                        _file_mag.close()
                except OSError as error:
                    print(error)
        else:
            print(f"Tool field required to make directory for Test: {row.Test_Number}")
    except AttributeError:
        print("Make sure the spreadsheet has correct column names")
