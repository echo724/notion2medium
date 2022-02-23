from typing import Optional

from cleo.application import Application as BaseApplication
from cleo.formatters.style import Style
from cleo.io.inputs.input import Input
from cleo.io.io import IO
from cleo.io.outputs.output import Output

from notion2medium import __version__
from notion2medium.console.commands.publish import PublishCommand
from notion2medium.console.commands.select import SelectCommand


class Application(BaseApplication):
    def __init__(self) -> None:
        super(Application, self).__init__("notion2medium", __version__)
        self.add(PublishCommand())
        self.add(SelectCommand())

    def create_io(
        self,
        input: Optional[Input] = None,
        output: Optional[Output] = None,
        error_output: Optional[Output] = None,
    ) -> IO:
        io = super().create_io(input, output, error_output)

        formatter = io.output.formatter
        formatter.set_style(
            "ongoing", Style("light_gray", options=["bold", "dark"])
        )
        formatter.set_style("success", Style("light_gray", options=["bold"]))
        formatter.set_style("error", Style("red", options=["bold"]))
        formatter.set_style("code", Style("blue", options=["italic", "bold"]))
        formatter.set_style("highlight", Style("blue", options=["bold"]))
        formatter.set_style("dim", Style("default", options=["dark"]))
        formatter.set_style("question", Style("white"))
        formatter.set_style("info", Style("cyan", options=["bold"]))

        io.output.set_formatter(formatter)
        io.error_output.set_formatter(formatter)

        return io


def main() -> int:
    return Application().run()


if __name__ == "__main__":
    main()
