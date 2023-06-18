MENU_STATE_PROP = 'menu_state'
MENU_ITEM_ABOUT_ME = 'about_me'
MENU_ITEM_PROJECTS = 'projects'


class MenuState():
  def __init__(self, active_item: str = None) -> None:
    self.__menu_state = {
      MENU_ITEM_ABOUT_ME: False,
      MENU_ITEM_PROJECTS: False
    }

    if active_item and type(active_item) is str:
      self.__menu_state[active_item] = True
  

  def __getattr__(self, __name: str) -> bool:
    return self.__get_active_state(__name)
  

  def __getitem__(self, __name: str) -> bool:
    return self.__get_active_state(__name)


  def __get_active_state(self, __name):
    try:
      return self.__menu_state[__name]
    except KeyError:
      raise KeyError(f'Item "{__name}" is not valid.')

