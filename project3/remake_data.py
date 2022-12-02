import pandas as pd
from ast import literal_eval
import re

def remake_data():
    df = pd.read_csv('drop_data.csv')

    img = {
        "garen" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Garen.png",
        "galio" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Galio.png",
        "gangplank" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Gangplank.png",
        "gragas" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Gragas.png",
        "graves" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Graves.png",
        "gwen" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Gwen.png",
        "gnar" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Gnar.png",
        "nami" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nami.png",
        "nasus" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nasus.png",
        "nautilus" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nautilus.png",
        "nocturne" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nocturne.png",
        "nunu" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nunu.png",
        "nunuwillump" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nunu.png",
        "nidalee" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nidalee.png",
        "neeko" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Neeko.png",
        "nilah" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Nilah.png",
        "darius" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Darius.png",
        "diana" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Diana.png",
        "draven" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Draven.png",
        "ryze" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ryze.png",
        "rakan" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Rakan.png",
        "rammus" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Rammus.png",
        "lux" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Lux.png",
        "rumble" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Rumble.png",
        "renata" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Renata.png",
        "renataglasc" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Renata.png",
        "renekton" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Renekton.png",
        "leona" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Leona.png",
        "reksai" : "https://opgg-static.akamaized.net/meta/images/lol/champion/RekSai.png",
        "rell" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Rell.png",
        "rengar" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Rengar.png",
        "lucian" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Lucian.png",
        "lulu" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Lulu.png",
        "leblanc" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Leblanc.png",
        "leesin" : "https://opgg-static.akamaized.net/meta/images/lol/champion/LeeSin.png",
        "riven" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Riven.png",
        "lissandra" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Lissandra.png",
        "lillia" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Lillia.png",
        "masteryi" : "https://opgg-static.akamaized.net/meta/images/lol/champion/MasterYi.png",
        "maokai" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Maokai.png",
        "malzahar" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Malzahar.png",
        "malphite" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Malphite.png",
        "mordekaiser" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Mordekaiser.png",
        "morgana" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Morgana.png",
        "drmundo" : "https://opgg-static.akamaized.net/meta/images/lol/champion/DrMundo.png",
        "missfortune" : "https://opgg-static.akamaized.net/meta/images/lol/champion/MissFortune.png",
        "bard" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Bard.png",
        "varus" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Varus.png",
        "vi" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Vi.png",
        "veigar" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Veigar.png",
        "vayne" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Vayne.png",
        "vex" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Vex.png",
        "belveth" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Belveth.png",
        "velkoz" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Velkoz.png",
        "volibear" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Volibear.png",
        "braum" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Braum.png",
        "brand" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Brand.png",
        "vladimir" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Vladimir.png",
        "blitzcrank" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Blitzcrank.png",
        "viego" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Viego.png",
        "viktor" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Viktor.png",
        "poppy" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Poppy.png",
        "samira" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Samira.png",
        "sion" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sion.png",
        "sylas" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sylas.png",
        "shaco" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Shaco.png",
        "senna" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Senna.png",
        "seraphine" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Seraphine.png",
        "sejuani" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sejuani.png",
        "sett" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sett.png",
        "sona" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sona.png",
        "soraka" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Soraka.png",
        "shen" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Shen.png",
        "shyvana" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Shyvana.png",
        "swain" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Swain.png",
        "skarner" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Skarner.png",
        "sivir" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Sivir.png",
        "xinzhao" : "https://opgg-static.akamaized.net/meta/images/lol/champion/XinZhao.png",
        "syndra" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Syndra.png",
        "singed" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Singed.png",
        "thresh" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Thresh.png",
        "ahri" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ahri.png",
        "amumu" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Amumu.png",
        "aurelionsol" : "https://opgg-static.akamaized.net/meta/images/lol/champion/AurelionSol.png",
        "ivern" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ivern.png",
        "azir" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Azir.png",
        "akali" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Akali.png",
        "akshan" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Akshan.png",
        "aatrox" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Aatrox.png",
        "aphelios" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Aphelios.png",
        "alistar" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Alistar.png",
        "annie" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Annie.png",
        "anivia" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Anivia.png",
        "ashe" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ashe.png",
        "yasuo" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Yasuo.png",
        "ekko" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ekko.png",
        "elise" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Elise.png",
        "monkeyking" : "https://opgg-static.akamaized.net/meta/images/lol/champion/MonkeyKing.png",
        "wukong" : "https://opgg-static.akamaized.net/meta/images/lol/champion/MonkeyKing.png",
        "ornn" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ornn.png",
        "orianna" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Orianna.png",
        "olaf" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Olaf.png",
        "yone" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Yone.png",
        "yorick" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Yorick.png",
        "udyr" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Udyr.png",
        "urgot" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Urgot.png",
        "warwick" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Warwick.png",
        "yuumi" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Yuumi.png",
        "irelia" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Irelia.png",
        "evelynn" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Evelynn.png",
        "ezreal" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ezreal.png",
        "illaoi" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Illaoi.png",
        "jarvaniv" : "https://opgg-static.akamaized.net/meta/images/lol/champion/JarvanIV.png",
        "xayah" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Xayah.png",
        "zyra" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zyra.png",
        "zac" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zac.png",
        "janna" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Janna.png",
        "jax" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Jax.png",
        "zed" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zed.png",
        "xerath" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Xerath.png",
        "zeri" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zeri.png",
        "jayce" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Jayce.png",
        "zoe" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zoe.png",
        "ziggs" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Ziggs.png",
        "jhin" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Jhin.png",
        "zilean" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Zilean.png",
        "jinx" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Jinx.png",
        "chogath" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Chogath.png",
        "karma" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Karma.png",
        "camille" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Camille.png",
        "kassadin" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kassadin.png",
        "karthus" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Karthus.png",
        "cassiopeia" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Cassiopeia.png",
        "kaisa" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kaisa.png",
        "khazix" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Khazix.png",
        "katarina" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Katarina.png",
        "kalista" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kalista.png",
        "kennen" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kennen.png",
        "caitlyn" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Caitlyn.png",
        "kayn" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kayn.png",
        "kayle" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kayle.png",
        "kogmaw" : "https://opgg-static.akamaized.net/meta/images/lol/champion/KogMaw.png",
        "corki" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Corki.png",
        "quinn" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Quinn.png",
        "ksante" : "https://opgg-static.akamaized.net/meta/images/lol/champion/KSante.png",
        "kled" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kled.png",
        "qiyana" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Qiyana.png",
        "kindred" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Kindred.png",
        "taric" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Taric.png",
        "talon" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Talon.png",
        "taliyah" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Taliyah.png",
        "tahmkench" : "https://opgg-static.akamaized.net/meta/images/lol/champion/TahmKench.png",
        "trundle" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Trundle.png",
        "tristana" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Tristana.png",
        "tryndamere" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Tryndamere.png",
        "twistedfate" : "https://opgg-static.akamaized.net/meta/images/lol/champion/TwistedFate.png",
        "twitch" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Twitch.png",
        "teemo" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Teemo.png",
        "pyke" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Pyke.png",
        "pantheon" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Pantheon.png",
        "fiddlesticks" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Fiddlesticks.png",
        "fiora" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Fiora.png",
        "fizz" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Fizz.png",
        "heimerdinger" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Heimerdinger.png",
        "hecarim" : "https://opgg-static.akamaized.net/meta/images/lol/champion/Hecarim.png",
        "ghost" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerHaste.png",
        "heal" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerHeal.png",
        "barrier" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerBarrier.png",
        "exhaust" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerExhaust.png",
        "clarity" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerMana.png",
        "mark" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerSnowball.png",
        "teleport" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerTeleport.png",
        "flash" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerFlash.png",
        "smite" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerSmite.png",
        "ignite" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerDot.png",
        "cleanse" : "https://ddragon.leagueoflegends.com/cdn/12.22.1/img/spell/SummonerBoost.png",
        "precision" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7201_Precision.png",
        "domination" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7200_Domination.png",
        "sorcery" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7202_Sorcery.png",
        "resolve" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7204_Resolve.png",
        "inspiration" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/7203_Whimsy.png",
        "press the attack" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/PressTheAttack/PressTheAttack.png",
        "lethal tempo" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/LethalTempo/LethalTempoTemp.png",
        "fleet footwork" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/FleetFootwork/FleetFootwork.png",
        "conqueror" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Precision/Conqueror/Conqueror.png",
        "electrocute" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/Electrocute/Electrocute.png",
        "predator" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/Predator/Predator.png",
        "dark harvest" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/DarkHarvest/DarkHarvest.png",
        "hail of blades" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/HailOfBlades/HailOfBlades.png",
        "summon aery" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/SummonAery/SummonAery.png",
        "arcane comet" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/ArcaneComet/ArcaneComet.png",
        "phase rush" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Sorcery/PhaseRush/PhaseRush.png",
        "grasp of the undying" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/GraspOfTheUndying/GraspOfTheUndying.png",
        "aftershock" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/VeteranAftershock/VeteranAftershock.png",
        "guardian" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Resolve/Guardian/Guardian.png",
        "glacial augment" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/GlacialAugment/GlacialAugment.png",
        "unsealed spellbook" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/UnsealedSpellbook/UnsealedSpellbook.png",
        "first strike" : "https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Inspiration/FirstStrike/FirstStrike.png"
    }

    def toString(arg):
        return re.sub(r"[^0-9a-zA-Z]", "", arg)

    def toList(arg):
        return literal_eval(arg)

    def toLink(arg):
        arg = arg.lower()
        return img[arg]

    def toListLink(arg):
        lst = []
        for i in arg:
            j = re.sub(r"[^0-9a-zA-Z]", "", i)
            j = j.lower()
            lst.append(img[j])
        return lst

    def toElement(arg):
        return "|".join(arg)

    def toItem(arg):
        lst = []
        for i in arg:
            lst.append(re.sub(r"[^0-9a-zA-Z ]", "", i))
        return lst

    df["champion"] = df["champion"].apply(toString)

    df["items"] = df["items"].apply(toList)
    df["team_champs"] = df["team_champs"].apply(toList)
    df["enemy_champ"] = df["enemy_champ"].apply(toList)
    df["team"] = df["team"].apply(toList)
    df["enemy"] = df["enemy"].apply(toList)

    df['items'] = df['items'].apply(toItem)

    #enemy, enemy_champ 칼럼의 내용이 뒤섞여 있다. 바로 잡아 주자!
    for k in range(len(df)):
        for i in df['enemy_champ'][k]:
            j = re.sub(r"[^0-9a-zA-Z]", "", i)
            j = j.lower()
            if not j in img.keys():
                df.iat[k,21], df.iat[k,22] = df.iat[k,22], df.iat[k,21]
                break

    df["champion"] = df["champion"].apply(toLink)
    df["d_spell"] = df["d_spell"].apply(toLink)
    df["f_spell"] = df["f_spell"].apply(toLink)
    df["main_rune"] = df["main_rune"].apply(toLink)
    df["sub_rune"] = df["sub_rune"].apply(toLink)
    df["team_champs"] = df["team_champs"].apply(toListLink)
    df["enemy_champ"] = df["enemy_champ"].apply(toListLink)

    df["items"] = df["items"].apply(toElement)
    df["team_champs"] = df["team_champs"].apply(toElement)
    df["enemy_champ"] = df["enemy_champ"].apply(toElement)
    df["team"] = df["team"].apply(toElement)
    df["enemy"] = df["enemy"].apply(toElement)

    df.to_csv('remake_data.csv', index=False)