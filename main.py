from tkinter import Tk
from ui import CodeSnippetManagerUI
from database import create_database

def main():
    # Initialize database
    create_database()
    
    # Initialize Tkinter main window
    root = Tk()
    root.title("Code Snippet Manager")
    root.geometry("700x500")
    
    # Initialize and run the UI
    app = CodeSnippetManagerUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
