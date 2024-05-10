from tkinter import *
from project2_user import *
from project2_voting_logic import *


class Gui:
    def __init__(self, window):
        self.user = User()
        self.voting = Voting()
        self.window = window

        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_id, text='Voter ID:\t\t')
        self.entry_id = Entry(self.frame_id, width=40)
        self.label_id.pack(padx=20, side='left')
        self.entry_id.pack(padx=20, side='left')
        self.entry_id.focus()
        self.frame_id.pack(anchor='w', pady=10)

        self.frame_status_message = Frame(self.window)
        self.label_status_message = Label(self.frame_status_message, text='')
        self.label_status_message.pack(pady=10)
        self.frame_status_message.pack()

        self.frame_admin_password = Frame(self.window)
        self.label_admin_password = Label(self.frame_admin_password, text='Please enter your password:\t')
        self.entry_admin_password = Entry(self.frame_admin_password, width=40)
        self.label_admin_password.pack(padx=20, side='left')
        self.entry_admin_password.pack(padx=20, side='left')
        self.frame_admin_password.pack(anchor='w', pady=10)
        self.frame_admin_password.pack_forget()

        self.frame_candidates = Frame(self.window)
        self.candidates = self.voting.candidate_list
        self.clicked = StringVar(self.window)
        self.clicked.set('')
        self.candidate_name = self.clicked
        self.label_select_candidate = Label(self.frame_candidates, text='Select Candidate:\t\t')
        self.candidate_dropdown = OptionMenu(self.frame_candidates, self.clicked, *self.voting.candidate_list)
        self.label_select_candidate.pack(padx=20, side='left')
        self.candidate_dropdown.pack(padx=20, side='left')
        self.frame_candidates.pack(anchor='w', pady=10)
        self.frame_candidates.pack_forget()

        self.frame_submit = Frame(self.window)
        self.button_submit = Button(self.frame_submit, text='SUBMIT', command=self.submit)
        self.button_submit.pack(pady=10)
        self.frame_submit.pack()

        self.frame_vote = Frame(self.window)
        self.button_vote = Button(self.frame_vote, text='VOTE', command=self.vote)
        self.button_vote.pack(pady=10)
        self.frame_vote.pack_forget()

        self.frame_submit_admin = Frame(self.window)
        self.button_submit_admin = Button(self.frame_submit_admin, text='SUBMIT', command=self.submit_admin)
        self.button_submit_admin.pack(pady=10)
        self.frame_submit_admin.pack_forget()

        self.frame_admin_funcs = Frame(self.window)
        self.label_admin_funcs = Label(self.frame_admin_funcs, text='Welcome, admin.')
        self.button_new_candidate = Button(self.frame_admin_funcs, text='New Candidate', command=self.new_candidate_button)
        self.button_count_vote = Button(self.frame_admin_funcs, text='Count Vote', command=self.count_vote_button)
        self.label_count_vote = Label(self.frame_admin_funcs, text='')
        self.button_cancel = Button(self.frame_admin_funcs, fg='red', text='CANCEL', command=self.cancel)
        self.label_admin_funcs.pack(pady=10)
        self.button_new_candidate.pack(pady=10)
        self.label_count_vote.pack(pady=10)
        self.button_count_vote.pack(pady=10)
        self.button_cancel.pack(pady=10)
        self.frame_admin_funcs.pack_forget()

        self.frame_new_candidate = Frame(self.window)
        self.label_candidate_name = Label(self.frame_new_candidate, text='Enter New Candidate\'s Name: ')
        self.entry_candidate_name = Entry(self.frame_new_candidate, width=40)
        self.button_submit_candidate = Button(self.frame_new_candidate, text='SUBMIT', command=self.new_candidate)
        self.button_back = Button(self.frame_new_candidate, text='BACK', command=self.back)
        self.label_candidate_name.pack(padx=20)
        self.entry_candidate_name.pack(padx=20)
        self.button_submit_candidate.pack(padx=10)
        self.button_back.pack(padx=10)

    def submit(self):
        try:
            is_admin = self.user.voter(self.entry_id.get())
            self.frame_id.pack_forget()
            self.frame_submit.pack_forget()
            self.label_status_message.config(text='')
            if is_admin:
                self.label_status_message.pack_forget()
                self.frame_admin_password.pack()
                self.label_status_message.config(fg='green', text='You\'ve entered an admin ID. Please enter your password')
                self.label_status_message.pack()
                self.frame_submit_admin.pack()
                self.entry_admin_password.focus()
            else:
                self.frame_candidates.pack()
                self.frame_vote.pack()
        except TypeError:
            self.label_status_message.config(fg='red', text='Invalid ID. Voter ID\'s are 8 digits long.')
        except ValueError:
            self.label_status_message.config(fg='red', text='Invalid ID. Voter ID\'s are numeric only.')
            self.frame_status_message.pack()
        except NameError:
            self.label_status_message.config(fg='red', text='Looks like you\'ve already voted! Please come back next year!')
            self.frame_status_message.pack()

    def vote(self):
        try:
            self.voting.add_vote(self.candidate_name.get())
            self.frame_candidates.pack_forget()
            self.frame_vote.pack_forget()
            self.clicked.set('')
            self.entry_id.delete(0, END)
            self.frame_id.pack()
            self.frame_submit.pack()
            self.label_status_message.config(text='')
        except NameError:
            self.label_status_message.config(fg='red', text='You must select a candidate to vote!')


    def submit_admin(self):
        if self.user.check_admin(self.entry_admin_password.get()):
            self.entry_admin_password.delete(0, END)
            self.frame_admin_password.pack_forget()
            self.label_status_message.pack_forget()
            self.frame_submit_admin.pack_forget()
            self.frame_admin_funcs.pack()
            self.label_count_vote.pack_forget()
        else:
            self.label_status_message.config(fg='red', text='You\'ve entered an incorrect password.')

    def new_candidate_button(self):
        self.label_status_message.pack_forget()
        self.frame_admin_funcs.pack_forget()
        self.frame_new_candidate.pack()
        self.entry_candidate_name.focus()

    def count_vote_button(self):
        self.label_count_vote.config(text=str(self.voting))
        self.label_count_vote.pack(pady=10)

    def cancel(self):
        self.frame_admin_funcs.pack_forget()
        self.entry_id.delete(0, END)
        self.frame_id.pack()
        self.label_status_message.config(text='')
        self.frame_status_message.pack()
        self.frame_submit.pack()
        self.entry_id.focus()

    def new_candidate(self):
        try:
            self.voting.add_candidate(self.entry_candidate_name.get())
            self.candidates = self.voting.candidate_list
            self.clicked.set('')
            menu = self.candidate_dropdown['menu']
            menu.delete(0, END)
            for candidate in self.candidates:
                menu.add_command(label=candidate, command=lambda value=candidate: self.clicked.set(value))
            self.label_status_message.config(fg='green', text=f'{self.entry_candidate_name.get()} added to options')
            self.label_status_message.pack()
            self.entry_candidate_name.delete(0, END)
            self.entry_candidate_name.focus()
        except ValueError:
            self.label_status_message.config(fg='red', text='You must enter a name')
            self.label_status_message.pack()
        except NameError:
            self.label_status_message.config(fg='red', text='This candidate already exists')
            self.label_status_message.pack()

    def back(self):
        self.frame_new_candidate.pack_forget()
        self.frame_admin_funcs.pack()
        self.label_count_vote.pack_forget()
