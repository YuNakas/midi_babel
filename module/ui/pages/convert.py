import flet as ft

def convert_view(return_top):
    ft.View(
        "/convert",
        [
            ft.AppBar(title=ft.Text("変換が完了しました"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Row(
                [
                    ft.ElevatedButton(
                        "Topへ戻る",
                        icon = "CHECK_CIRCLE_OUTLINE",
                        on_click = return_top
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ]
    )