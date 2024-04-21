import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.command()
async def help(ctx):
    await ctx.send(f'Merhaba {bot.user}! Görünüşe göre yardıma ihtiyacın var, iste bu bot için kullanabilecegin komutlar(Lütfen komutların basına nokta(.) koyunuz: hello(merhabalasma) chat(ne hakkında konuşmak istiyorsun) cevre(eğer daha fazla bilgi istiyorsan oneri komutuna yönlendirir) oneri(doğayı korumak için ne yapabiliriz sorusuna cevaplar) resim(doğa ile ilgili bir resim gönderir)')
    time.sleep(1)
    await ctx.send(f'Haydi biraz çevre hakkında bahsedelim!')


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum! Görünüşe göre sen de bir çevreseversin.')
    time.sleep(1)
    await ctx.send(f'Haydi biraz çevre hakkında bahsedelim!')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Hangi konu konuşalım?')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız .oneri komutunu kullanın böylece size daha fazla yardımcı olabilirim')

@bot.command()
async def oneri(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.')

@bot.command()
async def resim(ctx):
    with open(r'M1L3\images\indir.jpg','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')