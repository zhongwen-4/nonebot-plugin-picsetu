from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.plugin import PluginMetadata

import httpx, random
setu_cmd = on_command("setu", aliases={"色图", "涩图"})


__plugin_meta__ = PluginMetadata(
    name="涩图插件",
    description="随机获取一张涩图",
    type="application",
    homepage="https://github.com/zhongwen-4/nonebot-plugin-picsetu",
    supported_adapters={"~onebot.v11"},
    usage="发送[setu, 涩图, 色图]任意一个就可以获取图片啦"
)


@setu_cmd.handle()
async def setu_handle():
    a_randint = random.randint(1, 100)

    try:
        if a_randint < 20:
            await setu_cmd.send("稍等，图片正在赶来的路上")

            async with httpx.AsyncClient() as client:
                res = await client.get(
                    "https://api.lolicon.app/setu/v2"
                )
                url = await client.get(res.json()["data"][0]["urls"]["original"])

                if url.status_code == 200:
                    await setu_cmd.finish(MessageSegment.image(res.json()["data"][0]["urls"]["original"]))
                else:
                    await setu_cmd.finish("出错了，请重试")

        
        if a_randint < 70 and a_randint > 20:
            await setu_cmd.send("稍等，图片正在赶来的路上")

            async with httpx.AsyncClient() as client:
                res = await client.get(
                    "https://image.anosu.top/pixiv/json"
                )
                url = await client.get(res.json()[0]["url"])

                if url.status_code == 200:
                    await setu_cmd.finish(MessageSegment.image(res.json()[0]["url"]))
                else:
                    await setu_cmd.finish("出错了，请重试")


        if a_randint > 70:
            await setu_cmd.send("稍等，图片正在赶来的路上")
            async with httpx.AsyncClient() as client:
                res = await client.get(
                    "https://misaliu.top/api/randomfurry/?format=json"
                )

                url = await client.get(res.json()["url"])
                if url.status_code == 200:
                    await setu_cmd.finish(MessageSegment.image(res.json()["url"]))
                else:
                    await setu_cmd.finish("出错了，请重试")

    except KeyError as e:
        await setu_cmd.finish(f"图片链接获取失败，请重试，code: {e}")