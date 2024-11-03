from tkinter import Tk, Label, Entry, Button, Toplevel, messagebox, Frame, Scrollbar, Listbox
from tkinter.scrolledtext import ScrolledText
from database import add_snippet, get_snippets, delete_snippet

class CodeSnippetManagerUI:
    def __init__(self, root):
        self.root = root
        self.build_ui()

    def build_ui(self):
        # Title input
        Label(self.root, text="Title:").pack()
        self.title_entry = Entry(self.root, width=60)
        self.title_entry.pack()
        
        # Language input
        Label(self.root, text="Language:").pack()
        self.language_entry = Entry(self.root, width=30)
        self.language_entry.pack()
        
        # Tags input
        Label(self.root, text="Tags (comma-separated):").pack()
        self.tags_entry = Entry(self.root, width=60)
        self.tags_entry.pack()
        
        # Code input
        Label(self.root, text="Code:").pack()
        self.code_text = ScrolledText(self.root, wrap="word", width=80, height=15)
        self.code_text.pack()
        
        # Buttons
        Button(self.root, text="Add Snippet", command=self.add_snippet).pack()
        Button(self.root, text="View Snippets", command=self.view_snippets).pack()

    def add_snippet(self):
        title = self.title_entry.get()
        code = self.code_text.get("1.0", "end-1c")
        language = self.language_entry.get()
        tags = self.tags_entry.get()

        if not title or not code:
            messagebox.showwarning("Input Error", "Title and Code are required!")
            return

        add_snippet(title, code, language, tags)
        messagebox.showinfo("Success", "Snippet added successfully!")
        
        # Clear fields
        self.title_entry.delete(0, "end")
        self.language_entry.delete(0, "end")
        self.tags_entry.delete(0, "end")
        self.code_text.delete("1.0", "end")

    def view_snippets(self):
        snippets = get_snippets()

        # Create a new window
        view_window = Toplevel(self.root)
        view_window.title("Saved Snippets")

        # Create a frame and a scrollbar
        frame = Frame(view_window)
        frame.pack(pady=10)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        # Listbox to display snippets
        self.snippet_listbox = Listbox(frame, width=80, height=20, yscrollcommand=scrollbar.set)
        self.snippet_listbox.pack()

        scrollbar.config(command=self.snippet_listbox.yview)

        # Add snippets to the listbox
        for snippet in snippets:
            self.snippet_listbox.insert("end", f"ID: {snippet[0]} | Title: {snippet[1]} | Language: {snippet[3]}")

        # Buttons to view, edit, and delete
        Button(view_window, text="View Code", command=self.view_code).pack(pady=5)
        Button(view_window, text="Delete Snippet", command=self.delete_snippet).pack(pady=5)

    def view_code(self):
        selected = self.snippet_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a snippet to view!")
            return

        snippet_id = self.snippet_listbox.get(selected).split("|")[0].split(":")[1].strip()
        snippets = get_snippets()
        code = next(snippet[2] for snippet in snippets if snippet[0] == int(snippet_id))

        # Create a new window to display code
        code_window = Toplevel(self.root)
        code_window.title("Snippet Code")
        code_text = ScrolledText(code_window, wrap="word", width=80, height=15)
        code_text.pack()
        code_text.insert("1.0", code)
        code_text.config(state="disabled")

    def delete_snippet(self):
        selected = self.snippet_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "Please select a snippet to delete!")
            return

        snippet_id = self.snippet_listbox.get(selected).split("|")[0].split(":")[1].strip()
        delete_snippet(int(snippet_id))
        messagebox.showinfo("Deleted", "Snippet deleted successfully!")
        self.view_snippets()  # Refresh the list
