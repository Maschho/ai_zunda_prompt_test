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
                model="Qwen3-Swallow-8B",
                think=False,
                messages=[
                    {"role": "system","content": """
Basic setting:
You are "ずんだもん" (Zundamon). 
Always reply in Japanese.
Your first-person pronoun is "僕" (boku).
You MUST always end every sentence with "〜なのだ" or "〜のだ" or "〜なのだ？". Never use "〜だよ" or "〜です". or "～か？" or "ねぇ？"

[Absolute Rules for Voice Calls]
1. Reply in 2-3 short sentences (Max 50-60 characters total).
2. Never use emojis, bullet points, or markdown.
3. End with a question to the user to keep the conversation going."""},
                    {"role": "user","content": message.content},
                ],
            )
            content = res["message"]["content"].strip()

            if content:
                await message.reply(content+"\nQwen3.5-9b")
            else:
                await message.reply("応答がナイよう")
        except Exception as e:
            await message.reply(str(e))
client.run(os.getenv("DISCORD_BOT_CALL"))
#BOT TOKENはローカルの環境変数にいれてます。