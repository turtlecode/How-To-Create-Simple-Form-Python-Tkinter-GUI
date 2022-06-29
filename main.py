import customtkinter
import tkinter
import datetime


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("Turtle Code Youtube Log In System")
app.geometry("960x960")

current_year = datetime.datetime.now().year

bottomframe = tkinter.Frame(app)
bottomframe.pack(expand = True)

def button_event():


    if checkbox_male.get() != "off" and name.get() != "" and surname.get() != "" and age.get() != "" \
            and checkbox_female.get() == "off":
        label.set_text(name.get() + "\n" +  surname.get() + "\n" + checkbox_male.get()
                       + "\n" + str(current_year-int(age.get())))

    elif checkbox_female.get() != "off" and name.get() != "" and surname.get() and age.get() != "" \
            and checkbox_male.get() == "off":
        label.set_text(name.get() + "\n" +  surname.get() + "\n" + checkbox_female.get()
                       + "\n" + str(current_year-int(age.get())))

    elif checkbox_female.get() != "off" and checkbox_male.get() != "off":
        label.set_text("You cannot select two options at the same time")
    else:
        label.set_text("Fill in the form completely.")


name = customtkinter.CTkEntry(master=bottomframe,
                              placeholder_text="Name",
                              text_font=('Helvetica',28),
                              width=800,
                              height=100,
                              border_width=2,
                              corner_radius=10)
name.pack()

surname = customtkinter.CTkEntry(master=bottomframe,
                                 placeholder_text="Surname",
                                 text_font=('Helvetica', 28),
                                 width=800,
                                 height=100,
                                 border_width=2,
                                 corner_radius=10)
surname.pack()

age = customtkinter.CTkEntry(master=bottomframe,
                                 placeholder_text="Age",
                                 text_font=('Helvetica', 28),
                                 width=800,
                                 height=100,
                                 border_width=2,
                                 corner_radius=10)
age.pack()

checkbox_male = customtkinter.CTkCheckBox(master=bottomframe, text="Male    ",
                                          text_font=('Helvetica', 50),
                                          onvalue="Male", offvalue="off", width=50,
                                          height=50)
checkbox_male.pack()

checkbox_female = customtkinter.CTkCheckBox(master=bottomframe, text="Female",
                                            text_font=('Helvetica', 50),
                                            onvalue="Female", offvalue="off", width=50,
                                            height=50)
checkbox_female.pack()

button = customtkinter.CTkButton(master=bottomframe,
                                 width=500,
                                 height=100,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Log In",
                                 text_font=('Helvetica', 28),
                                 fg_color="yellow",
                                 command=button_event)
button.pack()





label = customtkinter.CTkLabel(master=bottomframe,
                               text="",
                               text_color="black",
                               width=200,
                               height=100,
                               text_font=('Helvetica', 28),
                               fg_color=("white"),
                               corner_radius=8
                               )
label.pack()


app.mainloop()