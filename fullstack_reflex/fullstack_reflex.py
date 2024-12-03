"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def my_button() -> rx.Component:
    return rx.button("Click me")


def my_box() -> rx.Component:
    box = rx.box(
        rx.text("This is inside my_box"),
        my_button(),
    )
    return box
    

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        my_box(),
    )


app = rx.App()
app.add_page(index)
