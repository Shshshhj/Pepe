"""Emoji

Available Commands:

.switch"""

import asyncio

from telethon import events


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    input_str = event.pattern_match.group(1)

    if input_str == "switch":

        await event.edit(input_str)

        animation_chars = [
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n[👉](t.me/NeoMatrix90)⬜⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬛[👉](t.me/NeoMatrix90)⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬜⬜⬜⬜⬜⬜\n⬜[👆](t.me/NeoMatrix90)⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜[👆](t.me/NeoMatrix90)⬜⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬛[👉](t.me/NeoMatrix90)⬜⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜[🔲](https://github.com/prono69/PepeBot)\n⬜⬛⬛[👉](t.me/NeoMatrix90)⬜⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜🔲\n⬜⬛⬛⬛[👉](t.me/NeoMatrix90)⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜[👆](t.me/NeoMatrix90)⬜🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬛[👉](t.me/NeoMatrix90)🔲\n⬜⬛⬛⬛⬛⬜⬜\n⬜⬛⬜⬜⬜⬜⬜\n⬛⬛⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛🔳\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛⬛",
        ]

        animation_interval = 0.5

        animation_ttl = range(11)

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
