import flet as ft

def app_bar(title: str):
    return ft.AppBar(
        title=ft.Text(
            value=title,
        ),
        color="#FFFFFF",
        bgcolor="#194E66"
    )
