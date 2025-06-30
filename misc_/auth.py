import termcolor
import survey
import misc_.ui as ui
import os

def handler() -> str:

  print("""
----------------------------------------------------------------------------------------
|  ░█▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█░▒█ ▒█▀▀▀ ▒█▄░▒█ ▀▀█▀▀ ▀█▀ ▒█▀▀█ ░█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀▀█ ▒█▄░▒█  |
|  ▒█▄▄█ ▒█░▒█ ░▒█░░ ▒█▀▀█ ▒█▀▀▀ ▒█▒█▒█ ░▒█░░ ▒█░ ▒█░░░ ▒█▄▄█ ░▒█░░ ▒█░ ▒█░░▒█ ▒█▒█▒█  |
|  ▒█░▒█ ░▀▄▄▀ ░▒█░░ ▒█░▒█ ▒█▄▄▄ ▒█░░▀█ ░▒█░░ ▄█▄ ▒█▄▄█ ▒█░▒█ ░▒█░░ ▄█▄ ▒█▄▄▄█ ▒█░░▀█  |
----------------------------------------------------------------------------------------

""")

  options = ['Ｌｏｇｉｎ\n', 'Ｓｉｇｎ Ｕｐ\n', 'Ｂａｃｋ\n']
  index = survey.routines.select(
      'Ｐｌｅａｓｅ  ｓｅｌｅｃｔ  ｏｎｅ  ｏｆ  ｔｈｅ  ｆｏｌｌｏｗｉｎｇ  ｏｐｔｉｏｎｓ:\n',
      options=options,
      focus_mark='> ',
      evade_color=survey.colors.basic('white'),
      insearch_color=survey.colors.basic('white'))

  if index == 0:
    return "LOGIN"
  elif index == 1:
    return "SIGNUP"
  elif index == 2:
    os.system("clear")
    ui.Messages().indicator_message("            Ｂａｃｋｉｎｇ ｔｏ ｈｏｍｅ ｐａｇｅ")
    return "HOME"
  else:
    return "err"
