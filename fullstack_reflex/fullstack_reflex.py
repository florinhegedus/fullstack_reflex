"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class MyState(rx.State):
    count: int = 0
    color: str = "red"


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
    button = rx.button(
        "Click me",  border_radius="15px", font_size="18px"
    )
    return button


def counter() -> rx.Component:
    counter = rx.hstack(
        rx.heading("Count: ", color=MyState.color),
        rx.heading(MyState.count),
    )
    return counter


class CounterState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1


def counter_increment() -> rx.Component:
    counter = rx.hstack(
        rx.heading(CounterState.count),
        rx.button(
            "Increment",
            on_click=CounterState.increment,
        ),
    )
    return counter


class CounterState2(rx.State):
    count: int = 0

    @rx.event
    def increment(self, amount):
        self.count += amount


def counter_increment_by_amount() -> rx.Component:
    counter = rx.hstack(
        rx.heading(CounterState2.count),
        rx.button(
            "Increment by 1",
            on_click=lambda: CounterState2.increment(1),
        ),
        rx.button(
            "Increment by 5",
            on_click=lambda: CounterState2.increment(5),
        ),
    )
    return counter
    

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        my_box(),
        my_div(),
        half_filled_progress(),
        round_button(),
        counter(),
        counter_increment(),
        counter_increment_by_amount(),
    )


app = rx.App()
app.add_page(index)
