from project2_gui import *


def main():
    window = Tk()
    window.title('Student Grades')
    window.geometry('400x350')
    window.resizable(False, False)

    Gui(window)
    window.mainloop()


if __name__ == '__main__':
    main()