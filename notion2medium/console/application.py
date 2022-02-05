from cleo import Application as BaseApplication

from notion2medium import __version__
from notion2medium.console.commands.publish import PublishCommand

class Application(BaseApplication):
    def __init__(self) -> None:
        super(Application,self).__init__(
            "notion2medium",__version__
        )
        self.add(PublishCommand())

def main() -> int:
    return Application().run()

if __name__ == '__main__':
    main()