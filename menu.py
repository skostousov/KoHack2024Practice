import sys
class Menu:
  def __init__(self):
    self.choices = {
      "1":self.otherfunction,
      "2":self.anotherfunction,
      "3":self.quit
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
    print("1. First function\n2. Second function\n3. Quit")
  def otherfunction(self):
    pass
  def anotherfunction(self):
    pass
  def quit(self):
    sys.exit(0)

if __name__ == "__main__":
  Menu().run()
