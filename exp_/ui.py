import time

def name_handler(self) -> None:
  breakit = False
  while True:
      if breakit: break
      os.system("clear")
      self.ui.default_message(
          f"Ｃｕｒｒｅｎｔ ｎａｍｅ ｓｅｔ ｔｏ：'{self.name}'\nＴｏ ｇｏ ｂａｃｋ ｐｒｅｓｓ ［ ＥＮＴＥＲ ］"
      )
      name = input(self.color("> Ｎａｍｅ :", "white"))
      self.ui.primary_line("grey", 80)
      time.sleep(1)
      if name == " " or name == "": break
      names = name.split()
      for e in names:
          if not e.isalpha():
              self.ui.error_message(
                  "Ｓｔａｔｕｓ： Ｃｈａｎｇｉｎｇ Ｆａｉｌｅｄ\nＴｈｅ ｎａｍｅ ｃａｎ ｏｎｌｙ ｃｏｎｔａｉｎ ａｌｐｈａｂｅｔｓ"
              )

              break

          else:
              self.ui.success_message(
                  "Ｓｔａｔｕｓ： Ｎａｍｅ ｕｐｄａｔｅｄ ｓｕｃｃｅｓｓｆｕｌｌｙ！")
              self.name = name
              breakit = True
              break