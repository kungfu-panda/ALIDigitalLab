import os
from misc_ import home
from misc_ import auth
from auth_.models import AuthUtils
from auth_.login_ui import login_handler
from auth_.signup_ui import SignUpHandler

auth_utils = AuthUtils()
auth_utils.create_user_table()


CURR_SLIDE: str = "HOME"
SLIDES: dict = {
  "HOME": home.handler,
  "AUTH": auth.handler,
  "LOGIN": login_handler,
  "SIGNUP": SignUpHandler().main_display
}

while True:
  try:
    print("\033[0m")
    os.system("clear")
    next = SLIDES[CURR_SLIDE]()
    CURR_SLIDE = next
  except KeyboardInterrupt:
    print("Force Shutting.....")
    break
