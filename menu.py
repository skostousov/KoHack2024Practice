class Menu:
  def __init__(self):
    self.choices = {
      "1":self.otherfunction(),
      "2":self.otherfunction
    }
    pass
  def run(self):
    while True:
      self.display_menu()
      choice = input()
      action = self.choices.get(choice)
      if action:
        action()
      else:
        print(f"{choice} is not a valid choice")
  def display_menu(self):
    pass
  def otherfunction(self):
    pass
  def anotherfunction(self):
    pass

if __name__ == "__main__":
  Menu().run()
