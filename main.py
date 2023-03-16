import requests 
from tkinter import *
from tkinter import ttk
from win32com.client import Dispatch
import webbrowser
from PIL import ImageTk, Image
# Default values for country and category
country = 1
category = 0


def speak(str):
      speak=Dispatch("SAPI.SpVoice")
      speak.Speak(str)


def change_country(c):
    global country 
    country = c
    print(country)


def change_category(c):
    global category 
    category = c
    print(category)


def redirect(url):
    webbrowser.open(url)


# Defining dictionaries for country and category

countries = {
    1: "in",
    2: "us",
    3: "gb",
    4: "ca",
    5: "au"
    }


categories = {
    0: "",
    1: "business", 
    2: "entertainment", 
    3: "general", 
    4: "health", 
    5: "science", 
    6: "sports", 
    7: "technology"
    }


country_full_form = {
    1: "India",
    2: "US",
    3: "UK",
    4: "Canada",
    5: "Australia"
}


def speak(str):
      
      speak=Dispatch("SAPI.SpVoice")
      speak.Speak(str)


def get_newsHeadlines(country, category):
    apiKey = "0daf3716ab06409599baabc93d4bd8df"
    
    # country = countries[country]
    # category = categories[category]

    # https://newsapi.org/v2/top-headlines?country=us&apiKey=0daf3716ab06409599baabc93d4bd8df

    if category == 0:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={apiKey}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={apiKey}"
    
    response = requests.get(url).json()
    # print(d)

    article = response["articles"]
    return article
    pass


def GUI_Newspaper(country, category):

    country_name = country_full_form[country]
    country = countries[country]
    category = categories[category]



    headline = []
    # content = []
    url = []

    # getting article response from the website
    article = get_newsHeadlines(country, category)


    # adding title and url into the list
    for a in article:
        headline.append(a['title'])
        # content.append(a['content'])
        url.append(a['url'])



    # GUI
    root  = Tk()

    # Icon
    root.wm_iconbitmap("Newspaper3.ico")


    # root.title(f"{country_name}'s {category} News")

    # root.geometry("1280x760")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    print(width, height)

    root.geometry(f"{width}x{height}")

    root.title(f"{country_name}'s {category} News")

    # Create A Main Frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_scrollbar_2 = ttk.Scrollbar(main_frame, orient=HORIZONTAL, command=my_canvas.xview)
    my_scrollbar_2.pack(side=BOTTOM, fill=X)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    my_canvas.configure(xscrollcommand=my_scrollbar_2.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas)

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    # Adding an image using PIL
    image = Image.open('Speaker.png')

    # Resizing image
    image = image.resize((20, 20), Image.ANTIALIAS)

    speaker = ImageTk.PhotoImage(image)

    count = 0

    for i in range(len(headline)):
        if len(headline) == 0:
            label = Label(second_frame, text = f"No {category} news available from {country_name}").grid(row= 1, column=0, sticky='w')
            break
        else:
            label = Label(second_frame, font = ("Times New Roman",13, "bold"), text = headline[i], padx = 5, pady = 5).grid(row=count, column=0, sticky='w')
            # label = Label(second_frame, text = "     ").grid(row=count, column=1, sticky='w')
            button = Button(second_frame, image = speaker, text = "read",padx = 25, pady = 5, font = ("Times New Roman",12, "bold"), command = lambda x = headline[i]: speak(x)).grid(row = count, column = 2)
            # speak(headline[i])
            # label = Label(second_frame, text = content[i]).grid(row=count + 1, column=0, sticky='w')
            # label = Label(second_frame, text = url[i]).grid(row=count + 1, column=0, sticky='w')

            # "#7587eb"

            button = Button(second_frame, text = "link", padx = 69, pady = 5, font = ("Times New Roman",12, "bold"), bg= "#88bcfc", command = lambda x = url[i]: redirect(x)).grid(row = count +1, column = 0)

            count = count + 2



    # for i in range(len(headline)):
    #     speak(headline[i])

    root.mainloop()
        

        
    pass


def create_GUI():
    root = Tk()

    # Adding icon
    root.wm_iconbitmap("Newspaper3.ico")


    def Submit_button():
        root.destroy()
        GUI_Newspaper(country, category)
        pass


    root.geometry('500x630')
    root.maxsize(500, 630)
    root.minsize(500, 630)
    root.title('News App')


    colors = ["#430f58", "#6643b5", "#8594e4", "#d5def5", "black"] # BG, L, Button, Submit, Text



    #adding simple frame 

    frame1 = Frame(root, bg=colors[0],width=470,height=600,highlightcolor="yellow",highlightbackground=colors[4],  
        highlightthickness=10)
    frame1.pack(expand=True, fill=BOTH)




    # adding label for countryyand category on both side
    label_Country = Label(frame1, text = "Country Name",font=("ariel",20),bg=colors[1],fg=colors[4]).place(x=50,y=70)

    label_Category = Label(frame1, text = "Categories",font=("ariel",20),bg=colors[1],fg=colors[4]).place(x=300,y=70)



    # Defining Font
    Font_Norm_button = ("ariel",16)



    # Country buttons
    button_India = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="India", padx = 50, command = lambda: change_country(1)).place(x=50,y=150)
    button_US = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="United States", padx = 10, command = lambda: change_country(2)).place(x=50,y=200)
    button_UK = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="United Kingdom", command = lambda: change_country(3)).place(x=50,y=250)
    button_Can = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Canada", padx = 37, command = lambda: change_country(4)).place(x=50,y=300)
    button_Au = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Australia", padx = 33, command = lambda: change_country(5)).place(x=50,y=350)



    # Category buttons
    button_Buisness = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Business", padx = 22, command = lambda: change_category(1)).place(x=300,y=150)
    button_Entertainment = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Entertainment", command = lambda: change_category(2)).place(x=300,y=200)
    button_General = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="General", padx = 28, command = lambda: change_category(3)).place(x=300,y=250)
    button_Health = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Health", padx = 36, command = lambda: change_category(4)).place(x=300,y=300)
    button_Science = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Science", padx = 28, command = lambda: change_category(5)).place(x=300,y=350)
    button_Sports = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Sports", padx = 36, command = lambda: change_category(6)).place(x=300,y=400)
    button_Tech = Button(frame1,font= Font_Norm_button,fg= colors[4],bg= colors[2], text="Technology", padx = 14, command = lambda: change_category(7)).place(x=300,y=450)


    # Submit Button
    button_Submit = Button(frame1,font=("ariel",20),fg= colors[4],bg= colors[3], text="Submit",padx=50, command = Submit_button).place(x=150,y=530)

    root.mainloop()


def main():
    create_GUI()
    pass




if __name__ == "__main__":
    main()
    pass