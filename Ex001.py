import discord, ollama,os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user or not message.content:
        return
    async with message.channel.typing():
        try:
            res = ollama.chat(
                #swallow:20b-mxfp4
                #qwen3.5:9b
                #zundamon-ai
                model="zundamon-ai-3",
                think=False,
                messages=[
                    #{"role": "system","content": """"""},
                    {"role": "user","content": message.content},
                ],
            )
            content = res["message"]["content"].strip()

            if content:
                await message.reply(content+"\nQwen3-8b")
            else:
                await message.reply("応答がナイよう")
        except Exception as e:
            await message.reply(str(e))
client.run(os.getenv("DISCORD_BOT_CALL"))
#BOT TOKENはローカルの環境変数にいれてます。
