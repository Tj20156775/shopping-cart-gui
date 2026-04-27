
==== Package Justification ====


=== Why Tkinter ===

I chose Tkinter because it's Python's built in standard library for creating GUIs, it didn't require additional installations or dependencies, and seemed to be the most straight forward to use.  

=== Trade-offs Considered ===

Alternatives I looked at included PyQt5, Kivy, CustomTkinter, they offered better UI or flexibility but add dependencies, complexity, and longer development time. Because the GUI requirements were minimal, I focused on delivering an MVP rather than a fully featured interface.

=== MVP Philosophy Alignment ===  

It fits the MVP approach because it focuses only on the core usable features needed, without adding complexity.

=== Limitation and Workaround ===

Limitation:
Tkinter wasn't auto refreshinng UI elements when the data changed, everything had to be manually updated.

Workaround:
I added a method (update_cart_display) that is called after every action add, sort, clear. Now it ensures the UI reflects the current state of the cart.