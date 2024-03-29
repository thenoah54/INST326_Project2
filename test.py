import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.title("Button Names")
        
        # Create buttons
        self.button_names = ['Button 1', 'Button 2', 'Button 3']
        self.buttons = []
        for idx, name in enumerate(self.button_names):
            button = tk.Button(self, text=name, command=lambda idx=idx: self.button_clicked(idx))
            button.pack(pady=5)
            self.buttons.append(button)
    
    def button_clicked(self, idx):
        button_name = self.button_names[idx]
        print("Button clicked:", button_name)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
