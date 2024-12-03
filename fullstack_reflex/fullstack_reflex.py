"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def basic_button() -> rx.Component:
    return rx.button("Click me")
    

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        basic_button(),
    )


app = rx.App()
app.add_page(index)
