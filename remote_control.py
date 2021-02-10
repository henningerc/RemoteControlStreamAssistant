import asyncio
import simpleobsws
from settings import Settings


class RemoteControl:
    def __init__(self, settings, loop):
        self.ws = simpleobsws.obsws(
            host=settings.get('remote_host'),
            port=settings.get('remote_port'),
            password=settings.get('remote_password'),
            loop=loop)
        loop.run_until_complete(self.ws.connect())
        self.ws.register(self.on_event)
        self.ws.register(self.on_switchscenes, 'SwitchScenes')

    async def on_event(self, data):
        # Print the event data. Note that `update-type` is also provided in the data
        # print('New event! Type: {} | Raw Data: {}'.format(data['update-type'], data))
        print("---")

    async def on_switchscenes(self, data):
        print('Scene switched to "{}". It has these sources: {}'.format(data['scene-name'], data['sources']))

    async def change_scene(self, scene_name):
        result = await self.ws.call('SetCurrentScene', {'scene-name': scene_name})
        print(result)

    async def show_item(self, scene, item):
        result = await self.ws.call('SetSceneItemProperties', {'scene-name': scene,
                                                               'item': item,
                                                               'visible': True})
        print(result)
