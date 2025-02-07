from dearpygui.dearpygui import (
    get_viewport_client_width,
    get_viewport_client_height,
    mutex,
    window,
    add_text,
    add_button,
    split_frame,
    set_item_pos,
    delete_item
)


class ErrorMessage:

    def __init__(self, title: str, message: str, width: int, height: int, button_width: int):
        viewport_width = get_viewport_client_width()
        viewport_height = get_viewport_client_height()
        with mutex():
            with window(
                    label=title,
                    modal=True,
                    no_move=True,
                    no_collapse=True,
                    no_resize=True,
                    no_close=True,
                    no_title_bar=True,
                    width=width,
                    height=height
            ) as self.error_message_window:
                add_text(message)
                error_button = add_button(
                    label="Ok",
                    width=button_width,
                    user_data=[self.error_message_window],
                    callback=self.close_error_message
                )
        split_frame()
        set_item_pos(
            self.error_message_window,
            [viewport_width // 2 - width // 2, viewport_height // 2 - height // 2]
        )
        set_item_pos(
            error_button,
            [width // 2 - button_width // 2, height - height // 3]
        )

    def close_error_message(self):
        delete_item(self.error_message_window)
