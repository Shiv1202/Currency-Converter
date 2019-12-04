# Importing the required Modules

from tkinter import Tk, StringVar, ttk
from tkinter import *
import tkinter.messagebox          # For Message Box
import time                        # For Date and Time
import requests as req             # For requests 
from bs4 import *                  # For BeautifulSoup
from matplotlib import pyplot as plt                  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
from matplotlib import style

# Variable for Storing URL of website
url = "https://www.x-rates.com/table/?from=INR&amount=1"

# Header For my browser 
header = {
    "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

# Getting the access to webpage and Creating the Soup object
webpage = req.get(url, headers = header)
Soup = BeautifulSoup(webpage.text, 'html.parser')


style.use("ggplot")

fig3 = plt.Figure(figsize = (5, 3), dpi = 100)
ax3 = fig3.add_subplot(111)


# Class For Converter
class Convert:

    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter | Foreign Exchange Rates")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background = "#F2C496")


        #=============================== VAriables ===============================

        
        DateofConvert = StringVar()
        value_0 = StringVar()
        convert = DoubleVar()
        currency = DoubleVar()
        var1 = DoubleVar()
        var2 = DoubleVar()
        convert.set(1)
        DateofConvert.set(time.strftime("%d/%m/%y"))

        # ============================ Methods ==================================

            # ============= Method For Exit =================================
        def cExit():
            cExit = tkinter.messagebox.askyesno("Exit System", "Confirm if you want to exit")
            if (cExit > 0):
                root.destroy()
                return

            # ============= Method For Reset the Screen ====================
        def Reset():
            value_0.set("")
            convert.set(1)
            currency.set("0.00")
            var1.set(0)
            var2.set(0)
            
            # ============= Method For Converting the value ================
        def Converted_value():
            s = value_0.get()
            # ============== Fetch the value of rates from the table ======
            rate = Soup.find('table', class_ = 'tablesorter ratesTable').find('td', text = lambda x : x == s).find_next('td').get_text()
            canvasCal()
            x = float(convert.get() * float(rate))
            Final_value = str('%.2f' %(x))
            currency.set(Final_value)
            var1.set(Final_value)
            var2.set(convert.get())
            def animate():
                s = value_0.get()
                c1 = int(convert.get())
                u = Soup.find('table', class_ = 'tablesorter ratesTable').find('td', text = lambda x : x == s).find_next('td').get_text()
                c2 = (float(c1) * float(u)) 
                ax3.clear()
                ax3.scatter(c1 + c1, c2)
            animate()
            return Final_value

        def canvasCal():
            s = value_0.get()
            c1 = int(convert.get())
            u = Soup.find('table', class_ = 'tablesorter ratesTable').find('td', text = lambda x : x == s).find_next('td').get_text()
            c2 = (float(c1) * float(u))
            print(c1, c2)
            
            #ax3.scatter(c1, c2)
            scatter3 = FigureCanvasTkAgg(fig3, Frame_2ButtomL)
            scatter3.get_tk_widget().grid(row = 0, column = 0)
            #ax3.legend()
            ax3.set_xlabel('INR')
            ax3.set_ylabel('Converted Value')
            ax3.set_title('Currency Conversion')


        # ===================== Frames ==========================================
        Title_frame = Frame(self.root, bd = 10, width = 1350, height = 100, padx = 10, pady = 10, bg = "#F2C496", relief = RIDGE)
        Title_frame.grid(row = 0, column = 0)

        self.lbl_Title = Label(Title_frame, text = "Currency Converter | Foreign Exchange Rates", padx = 17, pady = 4, bd = 1, font = ('arial', 30, 'bold'), bg = "#02A9FC", width = 50)
        self.lbl_Title.pack()

        Main_frame = Frame(self.root, bd = 10, width = 1350, height = 700, padx = 11, pady = 10, bg = "#F2C496", relief = RIDGE)
        Main_frame.grid(row = 1, column = 0)

        Frame_1 = Frame(Main_frame, bd = 4, width = 100, height = 600, padx = 5, pady = 1,relief = RIDGE)
        Frame_1.grid(row = 0, column = 0)

        Frame_2 = Frame(Main_frame, bd = 4, width = 800, height = 600, padx = 0, pady = 2,relief = RIDGE)
        Frame_2.grid(row = 0, column = 1)

        Frame_2Top = Frame(Frame_2, width = 250, height = 300, bd = 4, padx = 80, pady = 2, relief = RIDGE)
        Frame_2Top.grid(row = 0, column = 0)

        Frame_2Buttom = Frame(Frame_2, width = 800, height = 300, bd = 4, padx = 5, pady = 2, relief = RIDGE)
        Frame_2Buttom.grid(row = 1, column = 0)

        Frame_2ButtomL = Frame(Frame_2Buttom, width = 450, height = 300, bd = 4, padx = 0, pady = 2, relief = RIDGE)
        Frame_2ButtomL.grid(row = 0, column = 0)

        Frame_2ButtomR = Frame(Frame_2Buttom, width = 350, height = 300, bd = 4, padx = 10, pady = 2, relief = RIDGE)
        Frame_2ButtomR.grid(row = 0, column = 1)

        Frame_3 = Frame(Main_frame, bd = 4, width = 100, height = 600, padx = 5, pady = 1,relief = RIDGE)
        Frame_3.grid(row = 0, column = 2)

        #=============================== Widgets =================================
        self.lblToday = Label(Frame_2Top, font = ('arial', 20, 'bold'), text = 'Todays Date', padx = 2, pady = 10, bd = 2, width = 18)
        self.lblToday.grid(row = 0, column = 0)
        self.lblDate = Label(Frame_2Top, font = ('arial', 20, 'bold'), textvariable = DateofConvert, padx = 2, pady = 10, bd = 2, width = 12, justify = 'center')
        self.lblDate.grid(row = 0, column = 1)

        #================================ Scale ==================================

        self.Converted = Scale(Frame_3, variable = var1, from_ = 0, to = 1000, length = 500, tickinterval = 50, orient = VERTICAL, bg = '#EA2A97', label = "Convert", font = ('arial', 10, 'bold'))
        self.Converted.grid(row = 0, column = 0, rowspan = 2)

        self.INR = Scale(Frame_1, variable = var2, from_ = 0, to = 1000, length = 500, tickinterval = 50, orient = VERTICAL, bg = '#EA2A97', label = "INR", font = ('arial', 10, 'bold'))
        self.INR.grid(row = 0, column = 0, rowspan = 2)

        #=========================== Labels for Frame_2 Top=======================

        self.lbl_INR = Label(Frame_2Top, font = ('arial', 20, 'bold'), text = "INR", padx = 2, pady = 10, width = 19, bd = 2)
        self.lbl_INR.grid(row = 1, column = 0)

        self.EntCurrency = Entry(Frame_2Top, font = ('arial', 20, 'bold'), textvariable = convert, bd = 2, width = 23, justify = 'center')
        self.EntCurrency.grid(row = 1, column = 1, pady = 10)

        self.Option = ttk.Combobox(Frame_2Top, textvariable = value_0, state = 'readonly', font = ('arial', 20, 'bold'), width = 20)
        self.Option['values'] = ("Select", "Argentine Peso", "Australian Dollar", "Bahraini Dinar", "Batwana Pula", "Brazilian Real", "British Pound", "Bruneian Dollar", "Bulgarian Lev", "Canadian Dollar", "Chilean Peso", "Chinese Yuan Renmimbi", "Colombian Peso", "Crotian Kuna", "Czech Koruna", "Danish Krone", "Emirati Dirhan", "Euro", "Hong Kong Dollar", "Hungarian Foint", "IceLandic Krona", "Indonesian Rupiah", "Iranian Rial", "Israeli Shekel", "Japanese Yen", "Kazakhstani Tenge", "Kuwaiti Dinar", "Libyan Dinar", "Malaysian Ringgit", "Mauritian Rupee", "Mexican Peso", "Nepalese Rupee", "New Zealand Dollar", "Norwegian Krone", "Omani Rial", "Pakistani Rupee", "Philippine Peso", "Polish Zloty", "Qatari Riyal", "Romanian New Leu", "Russian Ruble", "Saudi Arabian Riyal", "Singapore Dollar", "South African Rand", "South Korean Won", "Sri Lankan Rupee", "Swedish Krona", "Swiss Franc", "Taiwan New Dollar", "Thai Baht", "Trinidadian Dollar", "Turkish Lira", "US Dollar", "Venezuelan Bolivar", "")
        self.Option.current(0)
        self.Option.grid(row = 2, column = 0, padx = 38, pady = 10)

        self.lblCurrency = Label(Frame_2Top, font = ('arial', 20, 'bold'), textvariable = currency, bd = 2, width = 20, bg = 'white', pady = 2, padx = 2, relief = 'sunken')
        self.lblCurrency.grid(row = 2, column = 1)

        #============================== Canvas =================================

        self.canvas = Canvas(Frame_2ButtomL, width = 600, height = 300, bg = 'gray')
        #self.canvas.pack()
        #self.canvas.create_line(100, 250, 400, 250, width = 3)
        #self.canvas.create_line(100, 250, 100, 50, width = 3) 

        #============================= Buttons =================================

        self.btnconvert = Button(Frame_2ButtomR, text = "Convert", padx = 2, pady = 8, bd = 2, fg = "black", font = ('arial', 20, 'bold'), width = 14, height = 2, command = Converted_value)
        self.btnconvert.grid(row = 4, column = 0)

        self.btnReset = Button(Frame_2ButtomR, text = "Reset", padx = 2, pady = 7, fg = "black", font = ('arial', 20, 'bold'), width = 14, height = 2, command = Reset)
        self.btnReset.grid(row = 5, column = 0)

        self.btnExit = Button(Frame_2ButtomR, text = "Exit", padx = 2, pady = 8, fg = "black", font =('arial', 20, 'bold'), width = 14, height = 2, command = cExit)
        self.btnExit.grid(row = 6, column = 0)


# ============================ Driver Code For the program =========================
if __name__ == "__main__":
    root = Tk()                     # Object instance of Tk() Class
    application = Convert(root)     # Creating the Object of the Classs
    root.mainloop()                 # Running the main loop for the main window

