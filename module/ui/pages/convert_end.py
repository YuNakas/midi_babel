import flet as ft

def convert_end_view(return_top):
    return ft.View(
        "/convert_end",
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