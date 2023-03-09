import flet as ft
from flet import *

def main(page):

    def btn_click(e):
        pass

    _main_column_  = Column(
        scroll="hidden",
        expand=True,
        spacing=205,
        alignment=MainAxisAlignment.START,
        horizontal_alignment=CrossAxisAlignment.CENTER,
        controls=[
            Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Image(
                        src="./img/kit-medical.png",
                        width=180,
                        height=180,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                     Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=1,
                        controls=[
                            Text("Med", size=35, color="#1A2C48", weight="bold", font_family="Rubik"),
                            Text("kit", size=35, color="#1A2C48", font_family="Rubik"),
                        ],
                    ),
                    Text("Medical clinic at your fingertips", size=15, color="#1A2C48", font_family="Rubik"),
                ],
            ),
            ElevatedButton(
                content=Text("Start", size=15, weight="bold", color="white", font_family="Rubik"),
                height=40,
                width=340,
                on_click= lambda _: page.go('/main'),
                style=ButtonStyle(
                    bgcolor='#1A2C48',
                    shape={"": RoundedRectangleBorder(radius=10)},
                ), 
            ),    
        ],
    )  

   # set up some bg and main container
   # The general UI will copy that of a mobile app
    page.add(
        # this is just a bg container
        Container(
            width=1500,
            height=800,
            margin=-10,
            bgcolor="#F2F2F2",
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls =[
                    # Main container
                    Container(
                        width=380, 
                        height=600, 
                        bgcolor="#F4F4F4",
                        border_radius=40,
                        border=border.all(10, "#EDEDED"),
                        padding=padding.only(top=20, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE, # clip contents to container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                # main column here...
                                _main_column_,
                            ],
                        ),
                    ),
                ],
            ),
        ),
    )
    page.update() 

if __name__ == "__main__":
    ft.app(target=main, assets_dir="img")

