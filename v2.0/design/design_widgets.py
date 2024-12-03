from PyQt5.QtGui import *

class Color():
    black = 'black'
    # fon = '#D0605E' 
    fon = '#3967d1'
    white = 'white'
    yellow = 'yellow'
    yelllow = '#ffff00'
    bc_btn = '#00d5d5'
    bc_btn_hover = '#ffff00' 
    label = 'white'

class Fon:
    fon_color = f"background-color: {Color.fon}"
    # winter_fon_image = "image/winter-fon.jpg"
    fon_image = "background-image: url('winter-fon.jpg');"

class Btn:
    btn_design = f"""
                    QPushButton {{
                        border-radius: 40px;
                        background-color: {Color.bc_btn};
                        color: {Color.white};
                        padding: 10px;
                    }}
                    QPushButton:hover {{
                        background-color: {Color.bc_btn_hover};
                        color: {Color.black};
                    }}
                """
