def color(style: int, text_color: int, background_color: int, text: str):
    return f"\033[{style};{text_color};{background_color}m{text}\033[0m"