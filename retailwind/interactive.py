from textual import widgets
from textual.app import App
from textual.color import Color
from textual.containers import Horizontal
from textual.events import Click, Paste

from retailwind.translator import Translator

PRIMARY = Color(231, 146, 13)
# DARK = Color(39, 39, 42)
DARK = Color.parse("#3f3f46")


class TextArea(widgets.TextArea):
    """TextArea with custom style"""

    BINDINGS = [
        ("escape", "quit", "Leave app"),
    ]

    def on_mount(self):
        self.styles.padding = 0
        self.styles.border = ("round", PRIMARY.with_alpha(0.6))
        self.styles.scrollbar_size_vertical = 1
        self.styles.scrollbar_size_horizontal = 1
        self.styles.scrollbar_color = PRIMARY
        self.styles.scrollbar_background_active = "black"
        self.styles.scrollbar_background_hover = "black"
        self.styles.scrollbar_color_hover = PRIMARY.with_alpha(0.9)
        self.styles.scrollbar_color_active = PRIMARY.with_alpha(0.9)


class Footer(widgets.Footer):
    """Footer with custom style"""

    DEFAULT_CSS = (
        """
    $accent: #fbbf24;
    $accent-darken-1: #f59e0b;
    $accent-darken-2: #d97706;
    """
        + widgets.Footer.DEFAULT_CSS
    )

    def on_mount(self):
        self.styles.background = DARK


class ReTailwindApp(App):
    """Interactive app"""

    ENABLE_COMMAND_PALETTE = False
    BINDINGS = [
        ("f5", "prettify_input()", "Prettify input"),
        ("f8", "clear_input()", "Clear input"),
    ]

    input_area = TextArea("", language="html", id="input", theme="vscode_dark")
    output_area = TextArea(
        "",
        language="html",
        id="output",
        theme="vscode_dark",
    )

    def __init__(self, translator: Translator, *args, **kwargs):
        self.translator = translator
        super().__init__(*args, **kwargs)
        # self._disabled_messages = {Click}

    def compose(self):
        yield widgets.Header()
        yield Horizontal(self.input_area, self.output_area)
        yield Footer()

    def action_prettify_input(self):
        self.input_area.text = self.translator.prettify(self.input_area.text)
        self.update_output()

    def action_clear_input(self):
        self.input_area.text = ""
        self.update_output()

    def update_output(self):
        self.input_area.post_message(self.input_area.Changed(self.input_area))

    def on_mount(self):
        self.title = "retailwind"
        self.sub_title = "Reverse obfuscated tailwind classes"
        self.styles.background = Color(0, 0, 0, 0)
        # self.input_area.focus()
        self.output_area.styles.border = ("round", DARK)
        # self.capture_mouse(None)

    def on_click(self, event: Click):
        pass

    def on_paste(self, event: Paste):
        self.input_area.text = event.text

    def on_text_area_changed(self, msg: widgets.TextArea.Changed):
        area: widgets.TextArea = msg.text_area
        if area.id == "input":
            try:
                output = self.translator.html(area.text)
                self.output_area.text = output
            except BaseException:  # pylint: disable=broad-exception-caught
                pass
