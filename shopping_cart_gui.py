"""
Shopping Cart GUI - MVP
"""

import tkinter as tk
from dict_methods import add_item, sort_entries


class ShoppingCartGUI:
    """ GUI for managing shopping cart."""

    def __init__(self, root):
        """Initialises GUI.

        Args:
            root: The main tkinter window
        """
        self.root = root
        self.root.title("Shopping Cart Manager - MVP")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Initialises cart
        self.cart = {}

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

        # Current Cart Section
        cart_frame = tk.LabelFrame(
            self.root,
            text="Current Cart",
            padx=20,
            pady=20,
            font=("Arial", 10, "bold")
        )
        cart_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Cart display
        self.cart_display = tk.Text(
            cart_frame,
            height=10,
            width=50,
            font=("Arial", 10),
            state="disabled"
        )
        self.cart_display.pack(pady=5)

        # Buttons Frame
        buttons_frame = tk.Frame(cart_frame)
        buttons_frame.pack(pady=10)

        # Sort button
        sort_btn = tk.Button(
            buttons_frame,
            text="Sort Cart (A-Z)",
            command=self.sort_cart,
            bg="white",
            fg="orange",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        sort_btn.pack(side="left", padx=5)

        # Clear button
        clear_btn = tk.Button(
            buttons_frame,
            text="Clear Cart",
            command=self.clear_cart,
            bg="white",
            fg="red",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5
        )
        clear_btn.pack(side="left", padx=5)

        # Total Items Label
        self.total_label = tk.Label(
            self.root,
            text="Total Items: 0",
            font=("Arial", 30, "bold"),
            pady=10
        )
        self.total_label.pack()

    def add_item_to_cart(self):
        """Adds item to cart using add_item() function from dict_methods."""
        item_name = self.item_entry.get().strip()

        # Updates cart and refreshes UI after user adds item
        self.cart = add_item(self.cart, [item_name])
        self.item_entry.delete(0, tk.END)
        self.update_cart_display()

    def sort_cart(self):
        """Sorts cart alphabetically using sort_entries() function."""
        self.cart = sort_entries(self.cart)
        self.update_cart_display()

    def clear_cart(self):
        """Clears all items from cart."""
        self.cart = {}
        self.update_cart_display()

    def update_cart_display(self):
        """Updates cart display and total items count."""
        self.cart_display.config(state="normal")
        self.cart_display.delete("1.0", tk.END)

        if not self.cart:
            self.cart_display.insert(tk.END, "Cart is empty\n")
        else:
            for item, quantity in self.cart.items():
                self.cart_display.insert(tk.END, f"{item}: {quantity}\n")

        total_items = sum(self.cart.values())
        self.total_label.config(text=f"Total Items: {total_items}")


def main():
    """runs app"""
    root = tk.Tk()
    ShoppingCartGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
