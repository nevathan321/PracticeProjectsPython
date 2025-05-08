import tkinter 



button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]


row_count = len(button_values)
column_count = len(button_values[0])

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"] 

color_light_gray = "#D4D4d2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_orange = "#FF9500" 
color_white = "white"


#window setup

window = tkinter.Tk() #creates the Window 
window.title("calculator") #for the window title 
window.resizable(False, False) #disables resizing the window

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black, foreground=color_white, anchor="e", width = column_count)

label.grid(row=0, column=0, columnspan = column_count, sticky = "we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30), width=column_count-1, height=1, command = lambda value=value: button_clicked(value))
        
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
    
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        
        else: 
            button.config(foreground=color_white, background=color_dark_gray)
       
        button.grid(row = row+1, column=column)

    
frame.pack()

A = "0"
operator = None
B = None

def clear():
    global A, operator, B
    A = "0"
    operator = None
    B = None
    label["text"] = "0"

def remove_zero_decimal(num):
    if num % 1 == 0: 
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, A, operator, B

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                result = None

                if operator == "+":
                    result = numA + numB
                elif operator == "-":
                    result = numA - numB
                elif operator == "×":
                    result = numA * numB
                elif operator == "÷":
                    if numB == 0:
                        label["text"] = "Error"
                        return
                    else:
                        result = numA / numB

                if result is not None:
                    label["text"] = remove_zero_decimal(result)

                A = "0"
                B = None
                operator = None

        elif value in "-+×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"
                operator = value

    elif value in top_symbols:
        if value == "AC":
            clear()
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    else:
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] += value

#center the window whenever we open it

window.update() 
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int(screen_width/2) - int(window_width/2)
window_y = int(screen_height/2) - int(window_height/2)

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}") #sets the window size and position



window.mainloop() # to make sure the window stays open 