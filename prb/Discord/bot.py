import discord
from discord.ext import commands
from prb.Crawler.crawler import Crawler
from prb.Database.job import *
import datetime as dt


class DiscordBot(commands.Bot):
    def __init__(self, command_prefix="?", intents=discord.Intents.all()):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.crawler = Crawler()

    async def on_ready(self):
        print(f"Bot connecté au serveur.")

    async def on_message(self, message):
        channel = message.channel.name
        content = message.content
        attachments = message.attachments
        author = message.author
        mode = None
        winners, losers = [], []

        if author.bot:
            return

        if channel in ["screen-attaque", "screen-defense"]:
            mode = channel[7:].capitalize()
            url = None
            if len(attachments) > 0:
                url = message.attachments[0].url

            if content == "?perco":
                if url is None:
                    error = discord.Embed(
                        title="⚠️ Erreur ⚠️", color=0xFF0000)
                    error.add_field(
                        name="No attachment detected!", value="", inline=True)
                    await message.reply(embed=error)

                    return

                winners, losers, perco = self.crawler.process(url=url, mode=mode)

                if len(winners + losers) == 0:
                    error = discord.Embed(
                        title="⚠️ Erreur ⚠️", color=0xFF0000)
                    error.add_field(
                        name="Screen incorrect!", value="", inline=True)
                    await message.reply(embed=error)

                    return

                result = discord.Embed(
                    title="⚔️ {} de {}".format(mode, perco),
                    description="❗ Victoire **{}**vs**{}** ❗".format(len(winners), len(losers)), color=0x00ff00)
                result.add_field(
                    name="🎖️ Gagnants", value="".join([f"- {k}\n" for k in winners]), inline=True)
                result.add_field(
                    name="☠️ Perdants", value="".join([f"\n- {k}" for k in losers]), inline=True)
                reply = await message.reply(embed=result)
                await reply.add_reaction('✅')
                await reply.add_reaction('❌')

            elif "?link" in content:
                pass

            elif content == "?rank":
                rank_user = message.author.mention
                users_data = get_users_data()
                selected_user = next(
                    (item for item in users_data if item.get("discordID") == rank_user.replace("!", "")), {})
                rank_embed = discord.Embed(
                    title="#️⃣ Ranking", color=0x0088cc)
                rank_embed.add_field(name="Total :", value="#{} 🔹 {} pts\n {} attaques, {} defenses".format(
                    selected_user["totalRanking"], selected_user["totalScore"], selected_user["totalAttacks"],
                    selected_user["totalDefences"]), inline=False)
                rank_embed.add_field(name="{} :".format(dt.datetime.today().strftime('%B')),
                                     value="#{} 🔹 {} pts\n {} attaques, {} defenses".format(
                                         selected_user["monthlyRanking"], selected_user["monthlyScore"],
                                         selected_user["monthlyAttacks"],
                                         selected_user["monthlyDefences"]), inline=False)
                await message.reply(embed=rank_embed)

            else:
                if content[0] == "?":
                    help_embed = discord.Embed(
                        title="ℹ️ Guide Bot Commande", color=0x00ff00)
                    help_embed.add_field(
                        name="?perco", value="Saisir les screens perco attaque ou defense", inline=False)
                    help_embed.add_field(
                        name="?link", value="Linker tes persos à ton compte discord", inline=False)
                    help_embed.add_field(
                        name="?rank", value="Checker ton ranking total/mensuel et d'autres détails supplémentaires",
                        inline=False)
                    await message.reply(embed=help_embed)

            return


        elif channel in []:
            pass

        else:
            pass
