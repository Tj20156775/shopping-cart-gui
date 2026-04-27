#!/usr/bin/env python3
"""
Shopping Cart GUI - MVP
"""

import tkinter as tk


class ShoppingCartGUI:
    """GUI for managing shopping cart."""

    def __init__(self, root):
        """Initialises GUI.

        Args:
            root: The main tkinter window
        """
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

        # Item Section
        add_frame = tk.LabelFrame(
            self.root,
            text="Add Items",
            padx=20,
            pady=20,
            font=("Arial", 15, "bold")
        )
        add_frame.pack(padx=20, pady=10, fill="x")

        # Item entry
        tk.Label(add_frame, text="Item Name:", font=("Arial", 10)).grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.item_entry = tk.Entry(add_frame, width=30, font=("Arial", 10))
        self.item_entry.grid(row=0, column=1, padx=10, pady=5)

        # Adds button
        add_btn = tk.Button(
            add_frame,
            text="Add to Cart",
            command=self.add_item_to_cart,
            bg="white",
            fg="green",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        add_btn.grid(row=0, column=2, padx=10, pady=5)

    def add_item_to_cart(self):
        """place holder for Adding item to cart """
        item_name = self.item_entry.get().strip()
        print(f"Would add: {item_name}")
        self.item_entry.delete(0, tk.END)


def main():
    """Runs app"""
    root = tk.Tk()
    ShoppingCartGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
