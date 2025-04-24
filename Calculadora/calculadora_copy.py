import flet as ft
from sympy import sympify, SympifyError

def main(page: ft.Page):
    page.title = "Calculadora con SymPy"
    page.vertical_alignment = "center"

    # Elementos de la interfaz
    input_expr = ft.TextField(label="Ingresa una expresión matemática", width=300)
    output_result = ft.Text("Resultado aparecerá aquí", size=20)
    btn_calculate = ft.ElevatedButton(
        "Calcular",
        icon=ft.icons.CALCULATE,
        on_click=lambda e: calculate_expression(e),
    )

    def calculate_expression(e):
        """Evalúa la expresión ingresada usando SymPy."""
        try:
            expr = sympify(input_expr.value)  # Convierte el string a expresión simbólica
            result = expr.evalf()  # Calcula el resultado numérico
            output_result.value = f"Resultado: {result}"
        except SympifyError:
            output_result.value = "¡Error! Expresión no válida."
        page.update()

    # Agregar elementos a la página
    page.add(
        ft.Column(
            [
                ft.Text("Calculadora con SymPy", size=24, weight="bold"),
                input_expr,
                btn_calculate,
                output_result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)