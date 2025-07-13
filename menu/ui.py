import misc_.ui as ui
import time
import survey
import os


class MenuInterface:

  def __init__(self) -> None:
    self.ui = ui.Messages()
    self.logged_in_user = None 

  def set_logged_in_user(self, user):
    self.logged_in_user = user

  def MenuUI(self) -> str:
    self.ui.default_message("                          ＭＡＩＮ ＭＥＮＵ")
    self.ui.leave_line()
    self.ui.leave_line()
    self.ui.primary_line("grey", 90)
    options = [
        'Ｍａｎａｇｅ Ａｃｃｏｕｎｔ\n', 'Ｃｒｅａｔｅ Ｌａｂ Ｇｒｏｕｐ\n', 'Ｖｉｅｗ Ｌａｂ Ｇｒｏｕｐｓ\n', 'Ｂａｃｋ\n'
    ]
    index = survey.routines.select(
        'Ｐｌｅａｓｅ  ｓｅｌｅｃｔ  ｏｎｅ  ｏｆ  ｔｈｅ  ｆｏｌｌｏｗｉｎｇ  ｏｐｔｉｏｎｓ:\n',
        options=options,
        focus_mark='> ',
        evade_color=survey.colors.basic('white'),
        insearch_color=survey.colors.basic('white'))
    if index == 3:
      os.system('clear')
      self.ui.indicator_message("                  Ｌｏｇｇｉｎｇ Ｏｕｔ")
      return ("AUTH",)
    elif index == 0:
      os.system('clear')
      self.ui.indicator_message("                  Ｍａｎａｇｅ Ａｃｃｏｕｎｔ")
      return ("MANAGE_ACCOUNT",)
    
    time.sleep(10)
