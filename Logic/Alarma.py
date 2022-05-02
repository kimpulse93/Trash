
import tkinter as tk
import tkinter.messagebox as mb

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_info = tk.Button(self, text="Информационное окно",
                             command=self.show_info)
        btn_warn = tk.Button(self, text="Окно с предупреждением",
                             command=self.show_warning)
        btn_error = tk.Button(self, text="Окно с ошибкой",
                              command=self.show_error)

        opts = {'padx': 800, 'pady': 5, 'expand': True, 'fill': tk.BOTH}
        btn_info.pack(**opts)
        btn_warn.pack(**opts)
        btn_error.pack(**opts)

    def show_info(self):
        msg = "Ваши настройки сохранены"
        mb.showinfo("Информация", msg)

    def show_warning(self):
        msg = "Временные файлы удалены не правильно"
        mb.showwarning("Предупреждение", msg)

    def show_error(self):
        msg = "Приложение обнаружило неизвестную ошибку"
        mb.showerror("Ошибка", msg)

if __name__ == "__main__":
    app = App()
    app.mainloop()
