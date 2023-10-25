import flet as ft

def create_text_field(width):
    return ft.Container(
        width = width,
        height = 24,
        padding = 0,
        margin = 0,
        content = ft.TextField()
    )