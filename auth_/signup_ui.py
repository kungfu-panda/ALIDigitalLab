import getpass
from termcolor import colored
from auth_.models import AuthUtils
import time
from misc_.ui import Messages
import os
import survey


class SignUpHandler:

    def __init__(self) -> None:
        self.color = colored
        self.auth_obj = AuthUtils()
        self.username: None = None
        self.password: None = None
        self.type: None = None
        self.ui = Messages()

    def password_handler(self) -> bool:
        while True:
            os.system("clear")
            self.ui.default_message("Ｅｎｔｅｒ ｔｈｅ ｎｅｗ Ｐａｓｓｗｏｒｄ")
            password = getpass.getpass(self.color("> Ｐａｓｓｗｏｒｄ :", "white"))
            if password == " " or password == "": break
            confirm_password = getpass.getpass(
                self.color("> Ｃｏｎｆｉｒｍ Ｐａｓｓｗｏｒｄ :", "white"))
            self.ui.primary_line("grey", 80)
            time.sleep(1)
            if password != confirm_password:
                self.ui.error_message(
                    "Ｓｔａｔｕｓ： Ｃｈａｎｇｉｎｇ Ｆａｉｌｅｄ\nＲｅａｓｏｎ： Ｐａｓｓｗｏｒｄｓ ｄｏｅｓ ｎｏｔ ｍａｔｃｈ"
                )
                break
            self.ui.success_message("Ｓｔａｔｕｓ： Ｐａｓｓｗｏｒｄ ｕｐｄａｔｅｄ ｓｕｃｃｅｓｓｆｕｌｌｙ！")
            self.password = password
            break

    def username_handler(self) -> bool:
        while True:
            os.system("clear")
            self.ui.default_message(
                f"Ｃｕｒｒｅｎｔ ｕｓｅｒｎａｍｅ ｓｅｔ ｔｏ：'{self.username}'\nＴｏ ｇｏ ｂａｃｋ ｐｒｅｓｓ ［ ＥＮＴＥＲ ］"
            )
            username = input(self.color("> Ｕｓｅｒｎａｍｅ :", "white"))
            self.ui.primary_line("grey", 80)
            time.sleep(1)
            user_exists = self.auth_obj.user_exists(username)
            if username == " " or username == "": break

            if not username.isalnum():
                self.ui.error_message(
                    "Ｓｔａｔｕｓ： Ｃｈａｎｇｉｎｇ Ｆａｉｌｅｄ\nＴｈｅ ｕｓｅｒｎａｍｅ ｃａｎ ｏｎｌｙ ｃｏｎｔａｉｎ ｎｕｍｂｅｒｓ \nａｎｄ ａｌｐｈａｂｅｔｓ"
                )
                break
            else:
                if user_exists:
                    self.ui.error_message(
                        f"Ｓｔａｔｕｓ： Ｃｈａｎｇｉｎｇ Ｆａｉｌｅｄ\nＲｅａｓｏｎ： Ｔｈｅ ｕｓｅｒｎａｍｅ ＂{username}＂ ｉｓ \nａｌｒｅａｄｙ ｔａｋｅｎ"
                    )
                else:
                    self.ui.success_message(
                        "Ｓｔａｔｕｓ： Ｕｓｅｒｎａｍｅ Ｕｐｄａｔｅｄ Ｓｕｃｃｅｓｓｆｕｌｌｙ！")
                    self.username = username
                    break


    def type_handler(self) -> None:
        self.ui.default_message(f"Ｃｕｒｒｅｎｔｌｙ ｓｅｌｅｃｔｅｄ ＇{self.type}＇")
        self.ui.primary_line("grey", 80)
        options = ["Ｓｔｕｄｅｎｔ", "Ｔｅａｃｈｅｒ"]
        index = survey.routines.select(
            'Ｃｈｏｏｓｅ ａｎ ａｃｃｏｕｎｔ ｔｙｐｅ :\n',
            options=options,
            focus_mark='>',
            evade_color=survey.colors.basic('white'),
            insearch_color=survey.colors.basic('white'))
        self.ui.primary_line("grey", 80)
        self.type = options[index]
        self.ui.success_message(f"Ｓｔａｔｕｓ： Ａｃｃｏｕｎｔ ｔｙｐｅ ｕｐｄａｔｅｄ ｔｏ ＇{self.type}＇")

    def create_user(self) -> str:
        if self.username == None or self.password == None or self.type == None:
            os.system("clear")
            self.ui.error_message(
                "Ｓｔａｔｕｓ： Ａｃｃｏｕｎｔ ｃｒｅａｔｉｏｎ ｆａｉｌｅｄ\nＲｅａｓｏｎ： Ｐｌｅａｓｅ ｆｉｌｌ ｉｎ ａｌｌ ｔｈｅ ｄｅｔａｉｌｓ"
            )
            return "SIGNUP"
        else:
            os.system("clear")
            self.auth_obj.add_user(self.username, self.password, self.type)
            self.ui.success_message(
                "Ｓｔａｔｕｓ： Ａｃｃｏｕｎｔ Ｃｒｅａｔｅｄ Ｓｕｃｃｅｓｓｆｕｌｌｙ!")
            return "AUTH"
        
    def mapper(self) -> None:
        os.system("clear")

    def main_display(self) -> str:
        print("""
------------------------------------------------
|    ▒█▀▀▀█ ▀█▀ ▒█▀▀█ ▒█▄░▒█ 　 ▒█░▒█ ▒█▀▀█    |
|    ░▀▀▀▄▄ ▒█░ ▒█░▄▄ ▒█▒█▒█ 　 ▒█░▒█ ▒█▄▄█    | 
|    ▒█▄▄▄█ ▄█▄ ▒█▄▄█ ▒█░░▀█ 　 ░▀▄▄▀ ▒█░░░    |
------------------------------------------------\n\n
""")
        self.ui.primary_line("grey", 100)
        options = [
            "Ｕｓｅｒｎａｍｅ", "Ｐａｓｓｗｏｒｄ", "Ｔｙｐｅ", "Ｃｏｎｆｉｒｍ", "Ｇｏ Ｂａｃｋ"
        ]
        index = survey.routines.select(
            'Ｐｌｅａｓｅ ｓｅｌｅｃｔ ｔｈｅ ｏｐｔｉｏｎｓ ｔｏ ｆｉｌｌ ｉｎ ｔｈｅ ｃｒｅｄｅｎｔｉａｌｓ:\n',
            options=options,
            focus_mark='> ',
            evade_color=survey.colors.basic('white'),
            insearch_color=survey.colors.basic('white'))
        if index == 4:
            os.system("clear")
            self.username = None
            self.password = None
            self.type = None
            self.ui.indicator_message(
                "Ｙｏｕ ｗｉｌｌ ｂｅ ｒｅｄｉｒｅｃｔｅｄ ａｎｄ ｙｏｕｒ \nｃｈａｎｇｅｓ ｗｉｌｌ ｂｅ ｃｌｅａｒｅｄ")
            return "AUTH"
        elif index == 2:
            os.system("clear")
            self.type_handler()
            return "SIGNUP"
        elif index == 1:
            os.system("clear")
            self.password_handler()
            return "SIGNUP"
        elif index == 0:
            self.username_handler()
            return "SIGNUP"
        elif index == 3:
            return self.create_user()
