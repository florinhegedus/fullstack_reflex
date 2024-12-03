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


class TextState(rx.State):
    text: str = ""

    @rx.event
    def update_text(self, new_text: str):
        self.text = new_text


def text_input():
    text_input_box = rx.vstack(
        rx.text(TextState.text),
        rx.input(
            default_value=TextState.text,
            on_blur=TextState.update_text,
        )
    )
    return text_input_box


def check_even(num: int):
    return num % 2 == 0


class EvenOddState(rx.State):
    count: int = 0
    text: str = "even"

    @rx.event
    def increment(self):
        self.count += 1
        if check_even(self.count):
            self.text = "even"
        else:
            self.text = "odd"


def counter_parity() -> rx.Component:
    counter = rx.hstack(
        rx.text(EvenOddState.count),
        rx.text(EvenOddState.text),
        rx.button("Increment", on_click=EvenOddState.increment),
    )
    return counter


class LoginState(rx.State):
    logged_in: bool = False

    def toggle_login(self):
        self.logged_in = not self.logged_in


def login_component() -> rx.Component:
    comp = rx.vstack(
        rx.cond(
            LoginState.logged_in,
            rx.heading("Logged in"),
            rx.heading("Not logged in")
        ),
        rx.button("Toggle login", on_click=LoginState.toggle_login),
    )
    return comp


class ListState(rx.State):
    items: list[str] = ["mere", "pere", "banane"]


def render_item(item: rx.Var[str]):
    return rx.list.item(item)


def render_list() -> rx.Component:
    list_comp = rx.box(
        rx.foreach(ListState.items, render_item)
    )
    return list_comp


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
        text_input(),
        counter_parity(),
        login_component(),
        render_list(),
    )


app = rx.App()
app.add_page(index)
