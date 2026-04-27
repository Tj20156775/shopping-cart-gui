#!/usr/bin/env python3
"""
Shopping Cart GUI - MVP
"""

import tkinter as tk


class ShoppingCartGUI:
    """ GUI for managing shopping cart."""

    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart Manager - MVP")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Sets up UI
        self.setup_ui()

    def setup_ui(self):
        """Creates all UI components."""
        # Title
        title_label = tk.Label(
            self.root,
            text="Shopping Cart Manager",
            font=("Arial", 20, "bold"),
            pady=20
        )
        title_label.pack()


def main():
    """Runs app"""
    root = tk.Tk()
    ShoppingCartGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
