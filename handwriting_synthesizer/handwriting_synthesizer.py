"""Welcome to Reflex!."""

from handwriting_synthesizer import styles

# Import all the pages.
from handwriting_synthesizer.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
