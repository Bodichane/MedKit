import flet as ft 
from flet import *

def main(page):
    
   page.vertical_alignment = "center"
   page.horizontal_alignment = "center"

   def btn_view_1(e):
        pass
    
   def btn_view_2(e):
        pass
    
   def btn_view_3(e):
        pass

    # Create the main column, with some specified properties
   _main_column_ = Column(
        scroll="hidden",
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            # The first control is a row with two components: a menu button and two images
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(
                        icons.MENU_SHARP,
                        icon_size=25,
                        icon_color="#1A2C48",
                    ),
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=0,
                        controls=[
                            Text("Med", size=14, color="#1A2C48", weight="bold", font_family="Rubik"),
                            Text("Kit", size=14, color="#1A2C48", font_family="Rubik"),
                        ],
                    ),
                    ft.CircleAvatar(
                        foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
                        content=ft.Text("P"),
                        width=35,
                        height=35,
                    )
                ],
            ),
            # Add the search bar to the page
            Container(
                width=350,
                height=40,
                margin=margin.only(top=10),
                bgcolor="white",
                border_radius=10,
                padding=padding.only(top=10, left=21, right=21, bottom=15),
                animate=Animation(400, "decelerate"),
                content=Column(
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    alignment=MainAxisAlignment.START,
                    controls=[
                        Row(
                            spacing=10,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[
                                Icon(
                                    icons.SEARCH_ROUNDED,
                                    size=15,
                                    color="c",
                                ),
                                TextField(
                                    border_color="transparent",
                                    height=20,
                                    text_size=12,
                                    content_padding=2,
                                    cursor_color="#CFCFCF",
                                    cursor_width=1,
                                    hint_text="Search Doctors, appointments...",
                                    text_style=TextStyle(font_family="Rubik")
                                ),
                            ],
                        ),
                    ],
                ),
            ), 
             # A new column that displays upcoming appointments
            Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text("Upcoming appointments", size=13, weight="bold", color="#1A2C48", font_family="Rubik"),
                            TextButton(
                                content=Container(
                                    content=Column(
                                        [
                                            Text("View all", size=13, color="#828282", font_family="Rubik"),
                                        ]
                                    ),   
                                ),
                                on_click=btn_view_1, 
                                disabled=True,
                            ),
                        ],
                    ),
                    # Container to display the details of the first appointment (General check up)
                    Container(
                        width=310,
                        height=65,
                        bgcolor="white",
                        border_radius=10,
                        padding=padding.only(top=10, left=31, right=31, bottom=15),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        Image(
                                            src="./img/stethoscope.png",
                                            width=20,
                                            height=20,
                                            color="#1A2C48",
                                            fit=ft.ImageFit.CONTAIN,
                                            ),
                                        Text("General check up", size=12, weight="bold", color="#1A2C48", font_family="Rubik"),
                                        ElevatedButton(
                                            content=ft.Text("Aug 12", size=10, weight="bold", color="#1A2C48"),
                                            height=30,
                                            width=68,
                                            on_click=btn_view_1,
                                            style=ButtonStyle(
                                                bgcolor='#B0E3FD',
                                                shape={"": ft.RoundedRectangleBorder(radius=15)},
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    # Container to display the details of the second appointment (Cardiologist check-up)
                    Container(
                        width=310,
                        height=65,
                        margin=ft.margin.only(top=10),
                        bgcolor="white",
                        border_radius=10,
                        padding=padding.only(top=10, left=31, right=31, bottom=15),
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                Row(
                                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        Image(
                                            src="./img/heart-pulse.png",
                                            width=20,
                                            height=20,
                                            color="#1A2C48",
                                            fit=ft.ImageFit.CONTAIN,
                                            ),
                                        Text("Cardiologist check-up", size=12, weight="bold", color="#1A2C48", font_family="Rubik"),
                                        ElevatedButton(
                                            content=Text("Aug 28", size=10, weight="bold", color="#1A2C48"),
                                            height=30,
                                            width=68,
                                            on_click=btn_view_1,
                                            style=ButtonStyle(
                                                bgcolor='#B0E3FD',
                                                shape={"": RoundedRectangleBorder(radius=15)},
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            # A new column that displays Current medications
            Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text("Current medications", size=13, weight="bold", color="#1A2C48", font_family="Rubik"),
                            TextButton(
                                content=Container(
                                    content=Column(
                                        [
                                            Text("View all", size=13, color="#828282", font_family="Rubik"),
                                        ]
                                    ),   
                                ),
                                on_click=btn_view_2, 
                                disabled=True,
                            ),
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/aspirin.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Aspirin",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik"
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/vitamin-c.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Vitamin C",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik"
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/vitamin-d.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Vitamin D",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik"
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                        ],
                    ),
                ],
            ),
            # A new column that displays Find your doctor
            Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text("Find your doctor", size=13, weight="bold", color="#1A2C48", font_family="Rubik"),
                            TextButton(
                                content=Container(
                                    content=Column(
                                        [
                                            Text("View all", size=13, color="#828282", font_family="Rubik"),
                                        ]
                                    ),   
                                ),
                                on_click=btn_view_3, 
                                disabled=True,
                            ),
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/generalist.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "General",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/dent.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Dentist",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/adn.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Geneticist",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),           
                            ),
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Container(
                                width=103,
                                height=120,
                                margin=margin.only(top=7, bottom=20),
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=20),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/bequilles.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Surgeon",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                margin=margin.only(top=7, bottom=20),
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=15),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/virus.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Virologist",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),    
                            ),
                            Container(
                                width=103,
                                height=120,
                                margin=margin.only(top=7, bottom=20),
                                bgcolor="white",
                                border_radius=10,
                                padding=padding.only(top=10, left=21, right=21, bottom=20),
                                content=Column(
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                    controls=[
                                        Image(
                                            src=f"./img/cardiologie.png",
                                            fit=ft.ImageFit.CONTAIN,
                                        ),
                                        Column(
                                            [
                                                Text(
                                                    "Cardiolog",
                                                    color="#828282",
                                                    size=12,
                                                    font_family="Rubik",
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.END,  
                                        ),
                                    ],
                                ),           
                            ),
                        ],
                    ),
                ],
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
                                # Form class here...
                            ]
                        )
                    )
                ],
            ),
        )
   )
   page.update() 

if __name__ == "__main__":
    ft.app(target=main, assets_dir="img")