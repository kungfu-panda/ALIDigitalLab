from accs_.models import AuthUtils
from misc_.ui import Messages
import os
import getpass
import time

class AccManageInterface:
  def __init__(self) -> None:
    self.auth = AuthUtils()
    self.gp = getpass
    self.logged_in_user:None = None
    self.ui = Messages()
    self.creds = None

  def handler(self) -> tuple:
    os.system('clear')
    self.creds= self.auth.get_details(self.logged_in_user
                                     )
    #self.ui.default_message("--- Ｌｉｎｇｏｊａｍ")
    time.sleep(5)
    