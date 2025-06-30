from termcolor import colored
from auth_.models import AuthUtils
import getpass
import os
from misc_.ui import Messages

ui = Messages()


def login_handler() -> str:
    print("""
            ------------------------------------------
            |     ▒█░░░ ▒█▀▀▀█ ▒█▀▀█ ▀█▀ ▒█▄░▒█      |
            |     ▒█░░░ ▒█░░▒█ ▒█░▄▄ ▒█░ ▒█▒█▒█      |
            |     ▒█▄▄█ ▒█▄▄▄█ ▒█▄▄█ ▄█▄ ▒█░░▀█      |
            ------------------------------------------


""")
    choice = ui.input_message("Ｗｏｕｌｄ ｙｏｕ ｌｉｋｅ ｔｏ ｏｐｅｎ ｔｈｅ ｌｏｇｉｎ ｆｏｒｍ [Y/N]: ")

    if choice.lower().startswith("y"):
        os.system("clear")
        ui.primary_line("grey", 70)
        print(colored("        Ｅｎｔｅｒ ｙｏｕｒ ｃｒｅｄｅｎｔｉａｌｓ ｂｅｌｏｗ   ", "white"))
        ui.primary_line("grey", 70)
        username = ""
        password = ""
        ui.leave_line()
        ui.leave_line()
        ui.primary_line("grey", 60)
        username = input(colored("Ｕｓｅｒｎａｍｅ    :", "white"))
        ui.primary_line("grey", 60)
        ui.leave_line()
        ui.primary_line("grey", 60)
        password = getpass.getpass(colored("Ｐａｓｓｗｏｒｄ    :", "white"))
        ui.primary_line("grey", 60)
        ui.leave_line()
        ui.indicator_message("        Ａｕｔｈｅｎｔｉｃａｔｉｎｇ Ｉｎｆｏｒｍａｔｉｏｎ")
        auth_obj = AuthUtils()
        user_exists = auth_obj.user_exists(username)
        if user_exists == False:
            os.system("clear")
            ui.error_message(
                f"""Ｓｔａｔｕｓ： Ｌｏｇｉｎ Ｆａｉｌｅｄ\nＲｅａｓｏｎ： Ｔｈｅ ｕｓｅｒｎａｍｅ ＂{username}＂ ｄｏｅｓ ｎｏｔ ｅｘｉｓｔ"""
            )
            return "LOGIN"
        elif user_exists == True:
            os.system("clear")
            matched = auth_obj.verify_user(username, password)
            if matched:
                ui.leave_line()
                ui.success_message("    Ｓｔａｔｕｓ： Ｌｏｇｉｎ ｓｕｃｃｅｓｓｆｕｌ")

                return "MENU"
            else:
                os.system("clear")
                ui.error_message(
                    "Ｓｔａｔｕｓ： Ｌｏｇｉｎ Ｆａｉｌｅｄ\nＲｅａｓｏｎ： Ｉｎｖａｌｉｄ Ｐａｓｓｗｏｒｄ")
                return "LOGIN"

    else:
        return "AUTH"



