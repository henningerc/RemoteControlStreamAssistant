import simpleobsws


class RemoteControlController:
    def __init__(self, data, loop):
        settings = data.settings
        self.data = data
        self.ws = simpleobsws.obsws(
            host=settings.get('remote_host'),
            port=settings.get('remote_port'),
            password=settings.get('remote_password'),
            loop=loop)
        loop.run_until_complete(self.ws.connect())
        self.ws.register(self.on_event)
        self.ws.register(self.on_switchscenes, 'SwitchScenes')
        self.ws.register(self.on_switch_scene_item, 'SceneItemVisibilityChanged')
        self.ws.register(self.on_toggle_mute, 'SourceMuteStateChanged')

    async def on_event(self, data):
        # Print the event data. Note that `update-type` is also provided in the data
        # print('New event! Type: {} | Raw Data: {}'.format(data['update-type'], data))
        pass

    async def on_switchscenes(self, data):
        await self.data.status.set_scene(data['scene-name'])

    async def on_switch_scene_item(self, data):
        await self.data.status.set_overlay_visible(data['scene-name'], data['item-name'], "True" if data['item-visible'] else "False")

    async def on_toggle_mute(self, data):
        await self.data.status.set_mute(data["sourceName"], data["muted"])

    async def get_scene(self):
        result = await self.ws.call('GetCurrentScene')
        await self.data.status.set_scene(result['name'])

    async def get_mute(self, source):
        result = await self.ws.call('GetMute', {'source': source})
        await self.data.status.set_mute(result['name'], result['muted'])

    async def get_scene_item(self, scene, source):
        result = await self.ws.call("GetSceneItemProperties", {"scene-name": scene, "item": source})
        await self.data.status.set_overlay_visible(scene, source, "True" if result["visible"] else "False")

    async def change_scene(self, scene_name):
        await self.ws.call('SetCurrentScene', {'scene-name': scene_name})

    async def toggle_scene_item_visibility(self, scene_name, scene_item):
        result = await self.ws.call("GetSceneItemProperties", {"scene-name": scene_name, "item": scene_item})
        await self.ws.call(
            "SetSceneItemRender",
            {"scene-name": scene_name, "source": scene_item, "render": not result["visible"]})

    async def toggle_mute(self, source):
        await self.ws.call("ToggleMute", {"source": source})

    async def hide_scene_item(self, scene_name, scene_item):
        await self.ws.call("SetSceneItemRender", {"scene-name": scene_name, "source": scene_item, "render": False})

    async def show_scene_item(self, scene_name, scene_item):
        await self.ws.call("SetSceneItemRender", {"scene-name": scene_name, "source": scene_item, "render": True})

    async def show_item(self, scene, item):
        result = await self.ws.call('SetSceneItemProperties', {'scene-name': scene,
                                                               'item': item,
                                                               'visible': True})
        print(result)

    async def set_mute(self, source, value):
        result = await self.ws.call('SetMute', {'source': source, 'mute': value})
        print(result)
