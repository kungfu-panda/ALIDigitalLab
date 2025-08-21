from accs_.models import AuthUtils
from misc_.ui import Messages
import os
import getpass
import survey
import time
from termcolor import colored


class AccManageInterface:

  def __init__(self) -> None:
    self.auth = AuthUtils()
    self.gp = getpass
    self.logged_in_user: None = None
    self.ui = Messages()
    self.creds = None
    self.color = colored

  def delete_account(self):
    os.system("clear")
    options = ["Ｙｅｓ\n", "Ｎｏ\n"]
    index = survey.routines.select('\nＳＥＬＥＣＴ Ａ ＯＰＥＲＡＴＩＯＮ:\n',
                                   options=options,
                                   focus_mark='>',
                                   evade_color=survey.colors.basic('white'),
                                   insearch_color=survey.colors.basic('white'))
    if index == 0:
      os.system("clear")
      self.ui.default_message("Ｅｎｔｅｒ ｔｈｅ ｐａｓｓｗｏｒｄ ｔｏ ｄｅｌｅｔｅ ｔｈｅ ａｃｃｏｕｎｔ")
      password = self.gp.getpass("> Ｐａｓｓｗｏｒｄ :")
      self.ui.primary_line("grey", 80)
      time.sleep(1)
      ret = self.auth.del_user(self.logged_in_user, password)
      if ret:
        self.ui.error_message("Ｓｔａｔｕｓ： Ａｃｃｏｕｎｔ ｄｅｌｅｔｅｄ ｓｕｃｃｅｓｓｆｕｌｌｙ！")
        return ("AUTH", )
      elif not ret:
        self.ui.error_message(
            "Ｓｔａｔｕｓ： Ａｃｃｏｕｎｔ ｄｅｌｅｔｉｏｎ ｆａｉｌｅｄ\nＲｅａｓｏｎ： ｉｎｃｏｒｒｅｃｔ ｐａｓｓｗｏｒｄ")
        return ("MANAGE_ACCOUNT", self.logged_in_user)
    else:
      return ("MANAGE_ACCOUNT", self.logged_in_user)

  def handler(self) -> tuple:
    os.system('clear')
    self.creds = self.auth.get_details(self.logged_in_user)

    print("""
---------------------------------------------------------------------------------------------------------------

─█▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█─░█ ░█▄─░█ ▀▀█▀▀ 　 ░█▀▄▀█ ─█▀▀█ ░█▄─░█ ─█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▄▀█ ░█▀▀▀ ░█▄─░█ ▀▀█▀▀ 
░█▄▄█ ░█─── ░█─── ░█──░█ ░█─░█ ░█░█░█ ─░█── 　 ░█░█░█ ░█▄▄█ ░█░█░█ ░█▄▄█ ░█─▄▄ ░█▀▀▀ ░█░█░█ ░█▀▀▀ ░█░█░█ ─░█── 
░█─░█ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ─▀▄▄▀ ░█──▀█ ─░█── 　 ░█──░█ ░█─░█ ░█──▀█ ░█─░█ ░█▄▄█ ░█▄▄▄ ░█──░█ ░█▄▄▄ ░█──▀█ ─░█──

---------------------------------------------------------------------------------------------------------------


""")
    self.ui.primary_line("grey", 100)

    print(
        f"""\nＵＳＥＲＮＡＭＥ: {self.creds[2]}\n\nＮＡＭＥ: {self.creds[4]}\n\nＡＣＣＯＵＮＴ-ＴＹＰＥ: {self.creds[3]}\n\nＵＳＥＲ－ＩＤ: {self.creds[1]}
    
    """)
    self.ui.primary_line("grey", 100)
    options = [
        "Ｄｅｌｅｔｅ Ａｃｃｏｕｎｔ\n", "Ｇｏ Ｂａｃｋ\n"
    ]
    index = survey.routines.select('\nＳＥＬＥＣＴ Ａ ＯＰＥＲＡＴＩＯＮ:\n',
                                   options=options,
                                   focus_mark='>',
                                   evade_color=survey.colors.basic('white'),
                                   insearch_color=survey.colors.basic('white'))

    if index == 1:
      return ("MENU", self.logged_in_user)
    elif index == 0:
      ret = self.delete_account()
      return ret
