from flet import *
from views import views_handler


def main:
    def route_change(route):
        print(page.route)
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )

    page.on_route_change  = route_change
    page.go('/')