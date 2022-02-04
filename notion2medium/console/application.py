from email.mime import application
from cleo.application import Application
from notion2medium.console.commands.select import SelectCommand

command = SelectCommand()
application = Application()
application.add(command)

def main() -> int:
    return application.run()

if __name__ == '__main__':
    main()