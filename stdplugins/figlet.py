"""Figlet plugin for PepeBot
\n\nCreated By @s_n_a_p_s
Ported by @NeoMatrix90 (Legend)"""

import pyfiglet

from uniborg import SYNTAX
from uniborg.util import admin_cmd, edit_or_reply


@borg.on(admin_cmd(pattern="figlet ?(.*)", allow_sudo=True))
async def figlet(event):
    if event.fwd_from:
        return
    CMD_FIG = {
        "slant": "slant",
        "3D": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
    }
    input_str = event.pattern_match.group(1)
    if ":" in input_str:
        text, cmd = input_str.split(":", maxsplit=1)
    elif input_str is not None:
        cmd = None
        text = input_str
    else:
        await edit_or_reply(
            event,
            "**Do You think this is Funny?**\n\n"
            "__Try this Blek Mejik:__\n\n"
            "```.help figlet```",
        )
        return
    if cmd is not None:
        try:
            font = CMD_FIG[cmd]
        except KeyError:
            await edit_or_reply(event, "`Invalid selected font.`")
            return
        result = pyfiglet.figlet_format(text, font=font)
    else:
        result = pyfiglet.figlet_format(text)
    await edit_or_reply(event, "‌‌‎`{}`".format(result))


SYNTAX.update(
    {
        "figlet": ".figlet text or **.figlet text : type\
    \n USAGE: Make the text Stylish\
    \n NOTE: Nospace must be given after : and type\
    \n EXAMPLE : `.figlet hello :digi`\
    \n\n STYLE LIST: `slant`, `3D`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi`"
    }
)
