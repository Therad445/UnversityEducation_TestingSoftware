import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller):
        """

        :param controller:
        """
        super().__init__()
        self.title('PyTkCalc')
        self.controller = controller
        self.value_var = tk.StringVar()

        self._make_main_frame()
        self._make_entry()
        self._make_buttons()
        self._center_window()

    def main(self):
        self.mainloop()
        print('In main of view')

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_entry(self):
        ent = ttk.Entry(
            self.main_frm, justify='right', textvariable=self.value_var, state='disabled'
        )
        ent.pack(fill="x")

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        frm = ttk.Frame(outer_frm)
        frm.pack()

        buttons_in_row = 0
        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                frm = ttk.Frame(outer_frm)
                frm.pack()
                buttons_in_row = 0

            if caption == '+':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_plus_click(button))
                                 )
            elif caption == '-':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_minus_click(button))
                                 )
            elif caption == '/':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_divide_click(button))
                                 )
            elif caption == '*':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_multiply_click(button))
                                 )
            elif caption == 'C':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_clear_click(button))
                                 )
            elif caption == '=':
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_result_click(button))
                                 )
            else:
                btn = ttk.Button(
                    frm, text=caption, command=(lambda button=caption: self.controller.on_number_click(button))
                                 )
            btn.pack(side="left")
            buttons_in_row += 1

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )



# class View(tk.Tk):
#
#     def __init__(self, controller):
#         self.controller = controller
#         self.root = tk.Tk()
#         self.root.title("Calculator")
#         self.result = tk.Label(self.root, text="0", width=20, height=2, font=("Arial", 20))
#         self.result.grid(row=0, column=0, columnspan=4)
#         self.create_button("C", self.controller.clear, 1, 0)
#         self.create_button("±", None, 1, 1)
#         # self.create_button("√", self.controller.square_root, 1, 2)
#         self.create_button("/", lambda: self.controller.set_operation('divide'), 1, 3)
#         self.create_button("7", lambda: self.controller.on_number_clicked(7), 2, 0)
#         self.create_button("8", lambda: self.controller.on_number_clicked(8), 2, 1)
#         self.create_button("9", lambda: self.controller.on_number_clicked(9), 2, 2)
#         self.create_button("*", lambda: self.controller.set_operation('multiply'), 2, 3)
#         self.create_button("4", lambda: self.controller.on_number_clicked(4), 3, 0)
#         self.create_button("5", lambda: self.controller.on_number_clicked(5), 3, 1)
#         self.create_button("6", lambda: self.controller.on_number_clicked(6), 3, 2)
#         self.create_button("-", lambda: self.controller.set_operation('subtract'), 3, 3)
#         self.create_button("1", lambda: self.controller.on_number_clicked(1), 4, 0)
#         self.create_button("2", lambda: self.controller.on_number_clicked(2), 4, 1)
#         self.create_button("3", lambda: self.controller.on_number_clicked(3), 4, 2)
#         self.create_button("+", lambda: self.controller.set_operation('add'), 4, 3)
#         self.create_button("0", lambda: self.controller.on_number_clicked(0), 5, 0, columnspan=2)
#         self.create_button(".", None, 5, 2)
#         # self.create_button("=", self.controller.calculate, 5, 3)
#
#     def create_button(self, text, command, row, column, columnspan=1):
#         button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 20), command=command)
#         button.grid(row=row, column=column, columnspan=columnspan)
#
#     def update_result(self, value):
#         self.result.config(text=str(value))
#
#     def run(self):
#         self.root.mainloop()
#         print('In main of view')
#         self.result.

    # def print_result(self):
    #     pass
    #
    # def display_error(self):
    #     pass
    #
    # def get_first_argument_string(self):
    #     pass
    # pass
    #
    # def get_second_argument_string(self):
    #     pass

