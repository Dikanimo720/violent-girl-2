import discord
from discord.ext import commands
import os
import threading

# 設定機器人意圖（不使用特權意圖）
intents = discord.Intents.default()
intents.message_content = True  # 允許讀取訊息內容

# 創建機器人實例（無前綴）
bot = commands.Bot(command_prefix='#', intents=intents)


# 處理訊息事件（無前綴指令）
@bot.event
async def on_message(message):
    # 忽略機器人自己的訊息
    if message.author == bot.user:
        return

    # 處理無前綴指令
    content = message.content.lower().strip()

    if content == 'hello':
        await message.channel.send(f'你好, {message.author.mention}!')
    elif content == 'mother':
        await message.channel.send(f'{message.author.mention}想說操你媽')
    elif content == 'help':
        help_text = """    

**可用指令：**
• `ping` - 檢查機器人延遲
• `hello` - 打招呼
• `mother` - 特殊問候
• `info` - 顯示機器人資訊
• `help` - 顯示此幫助訊息

**斜線指令：**
• `/ping`, `/hello`, `/mother`, `/info`
        """
        await message.channel.send(help_text)
    elif content == '吃大便':
        await message.channel.send('吃大便')

    elif content == '今天天氣如何':
        await message.channel.send('操你媽，閉嘴')

    elif content == '請問今天天氣如何':
        await message.channel.send('出大太陽')

    elif content == '戰士乾杯':
        await message.channel.send('乾杯！！')

    elif content == '幹嘛':
        await message.channel.send('幹嘛')

    elif content == '欸欸':
        await message.channel.send('白癡笨熊 回話')

    elif content == 'mother':
        await message.channel.send('操你媽')

    elif content == 'fxxk':
        await message.channel.send(':__:')

    else:
        print()

    # 確保仍然處理傳統前綴指令和斜線指令
    await bot.process_commands(message)


# 當機器人啟動時的事件
@bot.event
async def on_ready():
    print(f'已登入為 {bot.user.name} ({bot.user.id})')
    print('------')
    # 同步斜線指令
    try:
        synced = await bot.tree.sync()
        print(f"已同步 {len(synced)} 個斜線指令")
    except Exception as e:
        print(f"同步指令失敗: {e}")


# 傳統前綴指令（作為備用）
@bot.command()
async def ping(ctx):
    """檢查機器人是否在線"""
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')


@bot.command()
async def hello(ctx):
    """打招呼"""
    await ctx.send(f'你今天好嗎?, {ctx.author.mention}!')


@bot.command()
async def info(ctx):
    """顯示機器人資訊"""
    embed = discord.Embed(title="機器人資訊",
                          description="這是一個基礎 Discord 機器人",
                          color=0x00ff00)
    embed.add_field(name="開發者", value="你的名字", inline=False)
    embed.add_field(name="版本", value="1.0.0", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def 吃大便(ctx):
    """吃大便"""
    await ctx.send('吃大便')


@bot.command()
async def 請問今天天氣如何(ctx):
    """請問今天天氣如何"""
    await ctx.send('出大太陽')


@bot.command()
async def 戰士乾杯(ctx):
    """戰士乾杯"""
    await ctx.send('乾杯！！')


@bot.command()
async def 幹嘛(ctx):
    """幹嘛"""
    await ctx.send('幹嘛')


@bot.command()
async def 乾杯(ctx):
    """乾杯"""
    await ctx.send('乾杯')


@bot.command()
async def 今天天氣如何(ctx):
    """今天天氣如何"""
    await ctx.send('操你媽，閉嘴')


@bot.command()
async def mother(ctx):
    """操你媽"""
    await ctx.send('操你媽')


# 斜線指令
@bot.tree.command(name="ping", description="檢查機器人延遲")
async def ping_slash(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f'Pong! 延遲: {latency}ms')


@bot.tree.command(name="hello", description="打招呼")
async def hello_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f'你好, {interaction.user.mention}!')


@bot.tree.command(name="mother", description="操你媽")
async def mother_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention}想說操你媽')


@bot.tree.command(name="cup", description="戰士乾杯")
async def cup_slash(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention}想說戰士乾杯'
                                            )


@bot.tree.command(name="info", description="顯示機器人資訊")
async def info_slash(interaction: discord.Interaction):
    embed = discord.Embed(title="機器人資訊",
                          description="這是一個基礎 Discord 機器人",
                          color=0x00ff00)
    embed.add_field(name="開發者", value="你的名字", inline=False)
    embed.add_field(name="版本", value="1.0.0", inline=False)
    await interaction.response.send_message(embed=embed)


# 從環境變數獲取 Token
token = os.getenv('DISCORD_TOKEN')
if not token:
    print("請在 Secrets 中設置 DISCORD_TOKEN")
    print("前往 Discord Developer Portal 獲取你的 bot token")
else:
    # 運行 Discord 機器人
    bot.run(token)
