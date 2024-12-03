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


def my_div() -> rx.Component:
    div = rx.el.div(
        rx.el.p("This is basic HTML text!"),
    )
    return div


def half_filled_progress() -> rx.Component:
    progress = rx.progress(
        value=50,
    )
    return progress


def round_button() -> rx.Component:
    button = rx.button("Click me",  border_radius="15px", font_size="18px")
    

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        my_box(),
        my_div(),
        half_filled_progress(),
        round_button(),
    )


app = rx.App()
app.add_page(index)
