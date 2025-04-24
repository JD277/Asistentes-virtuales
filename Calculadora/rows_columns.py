import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(
            controls=[
                ft.Text("A")
                ft.Text("B")
                ft.Text("C")

            ]
        ),
        ft.Column(
            controls=[
                ft.Text("AA")
                ft.Text("BB")
                ft.Text("CC")
            ]
        )
    )