from twitchio.ext import commands
from remote_control import RemoteControl
from typing import Optional, Dict
import time
import math


class Chatbot(commands.Bot):
    blocker: Dict[str, float] = {}

    async def event_pubsub(self, data):
        pass

    def __init__(self, settings, loop):
        self.rc: Optional[RemoteControl] = None
        self.settings = settings
        self.progress = None
        super().__init__(
            irc_token=settings.get('irc_token'),
            client_id=settings.get('client_id'),
            nick=settings.get('bot_nick'),
            prefix=settings.get('prefix'),
            initial_channels=[settings.get('bot_channel')],
            loop=loop
        )

    def set_remote_control(self, rc: RemoteControl):
        self.rc = rc

    def set_progress(self, progress):
        self.progress = progress

    async def event_ready(self):
        """Called once when the bot goes online."""
        print(f"{self.settings.get('bot_nick')} ist online!")
        ws = self._ws  # this is only needed to send messages within event_ready
        await ws.send_privmsg(self.settings.get('bot_channel'), f"/me ist bereit!")

    async def event_message(self, ctx):
        """Runs every time a message is sent in chat."""

        # make sure the bot ignores itself and the streamer
        if ctx.author.name.lower() == "":  #self.settings.get('bot_nick').lower():
            return
        await self.handle_commands(ctx)

    @commands.command(name='da')
    async def da(self, ctx):
        print("da")
        self.progress.setValue(50)
        await ctx.send("Jo, bin do!")

    @commands.command(name='hilfe')
    async def hilfe(self, ctx):
        print("hilfe")
        await ctx.send("!da !hilfe")
        await ctx.send("Für andere Hilfe bin ich nicht zuständig.")

    @commands.command(name='info')
    async def info(self, ctx):
        print('info')
        if 'info' in self.blocker:
            runtime = time.time()-self.blocker["info"]
            if runtime < 600:
                await ctx.send("Die Information kann erst wieder in " + str(math.ceil(600 - runtime)) +
                               " Sekunden abgerufen werden!")
                return
        self.blocker["info"] = time.time()
        await ctx.send("Informationen kämen nun!")
        # await self.rc.show_item('Scene: PyCharm', 'Overlay: Info PyCharm')
