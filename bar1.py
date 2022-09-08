from libqtile.bar import Bar
import os
import subprocess
from libqtile import widget
from libqtile.widget.clock import Clock
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.windowname import WindowName

# import psutil

from unicodes import right_arrow, left_arrow
from colors import onedark

bar = Bar(
    [
        widget.KeyboardLayout(
            configured_keyboards=["us", "ru"],
            foreground=onedark["yellow"],
            background=onedark["fg0"],
        ),
        widget.Spacer(length=10, background=onedark["fg0"]),
        GroupBox(
            disable_drag=True,
            active=onedark["gray"],
            inactive=onedark["dark-gray"],
            highlight_method="line",
            block_highlight_text_color=onedark["cyan"],
            borderwidth=0,
            highlight_color=onedark["fg0"],
            background=onedark["fg0"],
        ),
        widget.Spacer(length=5, background=onedark["fg0"]),
        right_arrow(onedark["bg0"], onedark["fg0"]),
        widget.CurrentLayout(background=onedark["bg0"], foreground=onedark["purple"]),
        right_arrow(onedark["fg1"], onedark["bg0"]),
        widget.Prompt(background=onedark["fg1"], foreground=onedark["yellow"]),
        right_arrow(onedark["bg"], onedark["fg1"]),
        WindowName(background=onedark["bg"], foreground=onedark["fg"]),
        # widget.Spacer(length=1000),
        left_arrow(onedark["bg"], onedark["fg1"]),
        widget.Spacer(length=10, background=onedark["fg1"]),
        widget.Systray(background=onedark["fg1"]),
        widget.Spacer(length=10, background=onedark["fg1"]),
        left_arrow(onedark["fg1"], onedark["bg0"]),
        # widget.StockTicker(
        #     apikey="PKR3R9BDWHNDQWJU",
        #     function="CRYPTO_INTRADAY",
        #     # function="DIGITAL_CURRENCY_DAILY",
        #     symbol="BTC",
        #     market="USD",
        #     foreground=onedark["fg"],
        #     max_chars=11,
        # ),
        # widget.Spacer(length=5, background=onedark["bg0"]),
        widget.OpenWeather(
            background=onedark["bg0"],
            foreground=onedark["blue"],
            location="Moscow",
            format=" {wind_speed} {icon} {temp}糖",
        ),
        widget.OpenWeather(
            background=onedark["bg0"],
            foreground=onedark["fg"],
            location="Moscow",
            format=" {sunrise}  {sunset}",
        ),
        # widget.Memory(
        #     format=" {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
        #     background=onedark["fg3"],
        #     foreground=onedark["fg"],
        # ),
        left_arrow(onedark["bg0"], onedark["fg1"]),
        widget.CPU(
            format=" {freq_current}GHz {load_percent}%",
            background=onedark["fg1"],
            foreground=onedark["purple"],
        ),
        # widget.Spacer(length=10, background=onedark["fg1"]),
        widget.ThermalZone(
            format=" {temp}糖",
            background=onedark["fg1"],
            fgcolor_high=onedark["yellow"],
            fgcolor_normal=onedark["fg"],
            fgcolor_critical=onedark["red"],
        ),
        # widget.Spacer(length=10, background=onedark["fg1"]),
        # left_arrow(onedark["fg3"], onedark["fg1"]),
        widget.Spacer(length=10, background=onedark["fg1"]),
        widget.Battery(
            format="{percent: 2.0%}",
            background=onedark["fg1"],
            foreground=onedark["dark-green"],
        ),
        widget.Spacer(length=10, background=onedark["fg1"]),
        # widget.Net(background=onedark["fg3"], foreground=onedark["dark-blue"]),
        left_arrow(onedark["fg1"], onedark["bg0"]),
        Clock(
            background=onedark["bg0"],
            foreground=onedark["blue"],
            format=" %d-%m %a",
        ),
        Clock(
            background=onedark["bg0"],
            foreground=onedark["fg"],
            format="%I:%M %p",
        ),
        widget.Spacer(length=10, background=onedark["bg0"]),
        left_arrow(onedark["bg0"], onedark["fg0"]),
        widget.Spacer(length=20, background=onedark["fg0"]),
    ],
    25,
    # margin=[5, 5, 0, 5],
    # opacity=1,
    opacity=0.88,
    background=onedark["bg"],
    # background='#00000000',
)
