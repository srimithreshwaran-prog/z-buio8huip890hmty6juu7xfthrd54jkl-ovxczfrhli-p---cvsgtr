from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("CODINGAL TEXT EDITOR")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(0, minsize=800, weight=1)

# funcrion to open a file
def open_file():
    """Open a file for editing."""
    # Open a file dialog so the user can select a text file
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    
    # If the user cancels the dialog, exit the function
    if not filepath:
        return
        
    # Clear the existing content from the text editor widget
    txt_edit.delete(1.0, END)
    
    # Open and safely read the contents of the selected file
    with open(filepath, "r") as input_file:
        text = input_file.read()
        
    # Insert the read text into the editor widget
    txt_edit.insert(END, text)
    
    # Update the window title to show the current file path
    window.title(f"Codingal's Text Editor - {filepath}")
def save_file():
    # Save the current file as a new file
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    
    with open(filepath, "w") as output_file:
        # Read the edited content and update in the output file
        text = txt_edit.get("1.0", END)
        output_file.write(text)
        
    window.title(f"Codingal's Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()
