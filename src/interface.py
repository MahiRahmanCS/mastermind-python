import customtkinter

# Set dark mode FIRST, before creating any widgets
customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.geometry("600x300")

label = customtkinter.CTkLabel(root, text="Hello World", width=100, height=50)
label.pack()
root.mainloop()