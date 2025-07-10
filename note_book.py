import pickle

class NoteBook:
    def __init__(self):
        self.notebook_dic = {}

    def notebook_write(self, title, desc):
        self.notebook_dic[title] = desc

    def delete_note(self, num):
        note_book_list = list(self.notebook_dic.keys())
        if num > 0 and num <= len(note_book_list):
            self.notebook_dic.pop(note_book_list[num - 1])
        else:
            print("Please Enter valid numbers to delete")

    def titles_print(self):
        for i, k in enumerate(self.notebook_dic, start=1):
            print(i, ".", k)

    def print_selected_num_title(self, num):
        notebook_list = list(self.notebook_dic.keys())
        if num <= len(notebook_list) and num > 0:
            print(notebook_list[num - 1])

    def save_disk(self):
        with open('notebook.pkl','wb') as f:
            pickle.dump(self.notebook_dic,f)

    def  load_data(self):
        with open('notebook.pkl','rb') as f:
            self.notebook_dic=pickle.load(f)


notebook = NoteBook()
notebook.load_data()
notebook.titles_print()
while True:
    user_input= input("Enter 'q' for exit or 't' for title show or 'd' for delete or v for view all titles or add title: ")
    if user_input=='q':
        break
    elif user_input=='t':
        notebook.print_selected_num_title(int(input("Enter you selected title:")))
    elif user_input=='d':
        notebook.delete_note(int(input("Enter num to delete: ")))
    elif user_input=='v':
        notebook.titles_print()
    else:
        des = input("Enter description : ")
        notebook.notebook_write(user_input, des)
        notebook.save_disk()



#notebook.notebook_write("Bush daily life", "I love sleeping. so me sleep always")
#notebook.notebook_write('Fahim daily life', 'Always do code and now become mad')


