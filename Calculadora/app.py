import flet as ft

def main(page:ft.Page):
    """
        Esta es una función principal del programa que mostrara el hello world
    """
    label = ft.Text("Hello world ")
    btn = ft.Button("mostrar", on_click = btn_click)
    inputf = ft.TextField()
    output_label = ft.Text()
    def btn_click(e):
        output_label.value = f"Tu texto dice: {inputf.value}"
        page.update
    btn = ft.ElevatedButton("Mostrar", on_click=btn_click, icon=ft.Icons.DOCUMENT_SCANNER)
    page.add(label, inputf, btn, output_label)


ft.app(target = main, view=ft.WEB_BROWSER)