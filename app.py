import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("MedKit"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Start", on_click=lambda _: page.go("/main")),
                ],
            )
        )
        if page.route == "/main":
            page.views.append(
                ft.View(
                    "/main",
                    [
                        ft.AppBar(title=ft.Text(""), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
