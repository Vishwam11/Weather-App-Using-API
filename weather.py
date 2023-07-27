from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()                                                                                         # tkinter window
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# function
def fetchweather():
    try:                                                                                                # try expect
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

                                                                                                      # weather api
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c3e760d6d0d590e8bd4d8ca76267c1b5"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid Entry!!")

# textarea
textfield = tk.Entry(root, justify="center", width=17, font=("Cooper", 25, "bold"), bg="#F5F5DC", border=0, fg="black")
textfield.place(x=290, y=40)
textfield.focus()

# search icon
Search_icon = PhotoImage(file="img/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", command=fetchweather)
myimage_icon.place(x=600, y=34)

# logo
Logo_image = PhotoImage(file="img/logo.png")
logo = Label(image=Logo_image)
logo.place(x=315, y=115)

# time
name = Label(root, font=("Cooper", 15, "bold"))
name.place(x=90, y=200)
clock = Label(root, font=("Cooper", 20, "bold"))
clock.place(x=90, y=230)

# label
label1 = Label(root, text="WIND", font=("Cooper", 15, 'bold'), fg="Black")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Cooper", 15, 'bold'), fg="Black")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Cooper", 15, "bold"), fg="Black")
label3.place(x=440, y=400)

label4 = Label(root, text="PRESSURE", font=("Cooper", 15, "bold"), fg="Black")
label4.place(x=650, y=400)

t = Label(font=("Cooper", 70, "bold"), fg="#4563fa")
t.place(x=590, y=180)
c = Label(font=("Cooper", 15, 'bold'))
c.place(x=590, y=280)

w = Label(text="...", font=("Cooper", 20, "bold"))
w.place(x=120, y=430)
h = Label(text="...", font=("Cooper", 20, "bold"))
h.place(x=280, y=430)
d = Label(text="...", font=("Cooper", 20, "bold"))
d.place(x=450, y=430)
p = Label(text="...", font=("Cooper", 20, "bold"))
p.place(x=670, y=430)

root.mainloop()
