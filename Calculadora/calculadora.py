import flet as ft

# ==== Calculator class ==== #
class calculator(ft.Column):

    def __init__(self):
        # Call the constructor for the father class
        super().__init__()

        # Display input
        self.display = ft.TextField(
            value="0",
            text_align=ft.TextAlign.RIGHT,
            read_only=True,
            bgcolor=ft.colors.WHITE,
            border=ft.InputBorder.NONE,
            text_size=40,
            expand=True,
            height=80
        )

        # interface
        self.controls = [
            ft.Container(
                content=self.display,
                bgcolor=ft.colors.BLUE_GREY_900,
                padding=10,
                border_radius=15,
                shadow=ft.BoxShadow(
                    spread_radius=2,
                    blur_radius=10
                )
            ),
            #self.create_keyboard()
        ]

def main(page:ft.Page):

    page.title = "Calculadora"
    page.bgcolor = ft.colors.BLACK
    page.window_width = 600

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Container(
            content=calculator(),
            width=page.window_width*0.9,
            bgcolor=ft.colors.BLUE_GREY_900,
            border_radius=15,
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(main,view=ft.WEB_BROWSER)