# created by @eve_enryu

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg import SYNTAX
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="firmware(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = f"firmware"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


@borg.on(admin_cmd(pattern="xspecs(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = f"specs"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @xiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


@borg.on(admin_cmd(pattern="fastboot(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = f"fastboot"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBoot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


@borg.on(admin_cmd(pattern="recovery(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = f"recovery"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


@borg.on(admin_cmd(pattern="pb(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = f"pb"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


@borg.on(admin_cmd(pattern="of(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = f"of"
    await event.edit("```Processing```")
    async with borg.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await event.delete()
            await borg.forward_messages(event.chat_id, response.message)
        await borg.send_read_acknowledge(conv.chat_id)


SYNTAX.update(
    {
        "xiaomi": "**Plugin :** `Xiaomi`\
        \n\n__**For Xiaomeme devices only!**__\
        \n\n**Syntax :** `.firmware` (codename)\
        \n**Usage : **Get lastest Firmware\
        \n\n**Syntax :** `.pb` (codename)\
        \n**Usage : **Get latest PBRP\
        \n\n**Syntax :** `.xspecs` (codename)\
        \n**Usage : **Get quick spec information about device\
        \n\n**Syntax :** `.fastboot` (codename)\
        \n**Usage : **Get latest fastboot MIUI\
        \n\n**Syntax :** `.recovery` (codename)\
        \n**Usage : **Get latest recovery MIUI\
        \n\n**Syntax :** `.of` (codename)\
        \n**Usage : **Get latest ORangeFox Recovery"
    }
)
