from PIL import Image

from gsuid_core.bot import Bot
from gsuid_core.help.utils import register_help
from gsuid_core.models import Event
from gsuid_core.sv import SV
from .change_help import get_change_help
from .get_help import ICON, get_help
from ..wutheringwaves_config import PREFIX

sv_waves_help = SV("waves帮助")
sv_waves_change_help = SV("waves替换帮助")


@sv_waves_help.on_fullmatch(f"帮助")
async def send_help_img(bot: Bot, ev: Event):
    await bot.send(await get_help(ev.user_pm))


@sv_waves_change_help.on_fullmatch((f"替换帮助", f"面板替换帮助"))
async def send_change_help_img(bot: Bot, ev: Event):
    await bot.send(await get_change_help(ev.user_pm))


register_help("WutheringWavesUID", f"{PREFIX}帮助", Image.open(ICON))
