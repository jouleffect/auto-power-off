import tkinter as tk
import os

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        prompt = 'Shutting Down'
        self.label = tk.Label(self, text="", width=30, height=10)
        self.label.pack()        
        self.button = tk.Button(self, text="Cancel!", command=self.ferma)
        self.button.pack()
        self.remaining = 0
        self.countdown(10)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
            #os.system("systemctl poweroff")
        else:
        	self.label.configure(text="The system will shutdown in %d" % self.remaining)
        	self.remaining = self.remaining - 1
        	self.after(1000, self.countdown)            

    def ferma(self):
    	self.destroy()

if __name__ == "__main__":
    app = ExampleApp()
    app.mainloop()