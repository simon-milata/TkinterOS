from dataclasses import dataclass


@dataclass(frozen=True)
class ThemeColors:
    """Tuple order: (light_theme_color/dark_theme_color)"""
    primary: tuple[str, str]
    highlight: tuple[str, str]
    off: tuple[str, str]
    bright: tuple[str, str]
    button: tuple[str, str]
    button_hover: tuple[str, str]
    button_font_color: tuple[str, str]
    font_color: tuple[str, str]
    
    @staticmethod
    def create():
        primary = ("#f7c948", "#0f1b2b")
        bright = ("#ffe29e", "#1562c6")
        return ThemeColors(
            primary=primary,
            highlight=("#ffd36b", "#104b98"),
            off=("#dfb44f", "#0e2847"),
            bright=bright,
            button=(primary[1], primary[0]),
            button_hover=(bright[1], bright[0]),
            button_font_color=primary,
            font_color=(primary[1], primary[0])
        )


@dataclass(frozen=True)
class ThemeFonts:
    family: str = "Segoe UI"
    family_bold: str = "Segoe UI bold"
    extra_large: int = 65
    large: int = 50
    big: int = 30
    medium: int = 24
    small: int = 18
    extra_small: int = 12
    button_font_size: int = big
    
    @staticmethod
    def create():
        big = 30
        return ThemeFonts(
            family="Segoe UI",
            family_bold="Segoe UI bold",
            large=60,
            big=big,
            medium=24,
            small=18,
            extra_small=12,
            button_font_size=big
        )


THEME_COLORS = ThemeColors.create()
THEME_FONTS = ThemeFonts.create()