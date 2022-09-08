import os
from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import random

from bar1 import bar

from colors import onedark

mod = "mod4"
terminal = "kitty"
browser = "brave"

# Random Wallpaper on Save
path = "/home/dencho/Downloads/Wallpapers/Architecture/"
items = os.listdir(path)
wallpaper_list = []
for i in items:
    wallpaper_list.append(os.path.join(path, i))

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "l", lazy.layout.grow_main(), desc="Grow window to the left"),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.shrink_main(),
        desc="Grow window to the right",
    ),
    # Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # My keys
    Key([mod], "b", lazy.spawn(browser), desc="Open Brave browser"),
    Key([mod, "control"], "w", lazy.spawn("rofi -show drun"), desc="open dmenu"),
    Key(
        [mod],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
]

# groups = [Group(i) for i in "1234567"]
groups = [
    Group(
        "1",
        label="",
        matches=[],
        layout="monadtall",
    ),
    Group("2", label="", layout="monadtall"),
    Group(
        "3",
        label="爵",
        matches=[
            # Match(wm_class="brave"),
            # Match(wm_class="firefox"),
        ],
        layout="monadtall",
    ),
    Group(
        "4",
        label="",
        layout="floating",
    ),
    Group("5", label="", matches=[Match(wm_class="Spotify")], layout="stack"),
    Group("6", label="", layout="monadtall"),
    Group("7", label="", layout="monadtall"),
    # Group("8", label="", layout="monadtall"),
    # Group("9", label="", layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.MonadThreeCol(
        border_width=2,
        change_ratio=0.01,
        border_focus=onedark["cyan"],
        border_normal="#282c34",
        single_border_width=None,
        # margin=7,
    ),
    layout.MonadTall(
        border_width=2,
        change_ratio=0.01,
        border_focus=onedark["cyan"],
        border_normal="#282c34",
        single_border_width=None,
        # margin=15,
    ),
    layout.Floating(
        border_width=2,
        # fullscreen_border_width=0,
        border_focus="#75777b",
        border_normal="#282c34",
        max_border_width=2,
    ),
]

widget_defaults = dict(
    font="JetBrains Mono Medium",
    fontsize=16,
    padding=7,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper=random.choice(wallpaper_list),
        # wallpaper="~/Downloads/Wallpapers/jose-vega-final-painting.jpg",
        # wallpaper="~/Downloads/Wallpapers/terraform-studios-1nyan-citystreet-part1-v001-002-pd.jpg",
        wallpaper_mode="fill",
        top=bar,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"
