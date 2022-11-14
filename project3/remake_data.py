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
        "ghost" : "https://w.namu.la/s/950867a5e46790325ccafeb601e7580a942ccf0aa50022898b2ddb7ea38e6fddc4ec882ba8a0ecc313b0cfefeff6f4954e20d627e499dc01a129739bcf15018043d6ae5f7d1793f5cb04a35675f70f85555510a6809b86a72a6d0cde9612fc7d",
        "heal" : "https://w.namu.la/s/6961d1124473759d5492d0b29a7354f5d8deaf6431fbd03173263e2e9402d936578b9e2bea7653f93a983729d3bde890f782cc8c3d8d00eab7c244d85d9311a929f91bb86278f2ae490ad1ef759b852e68586f6119f4afe9c76258efe462aa52",
        "barrier" : "https://w.namu.la/s/f0cc107a233455943c2641d041dd949abc5c91d45a801bb3b25d2ad06c07633c255f454ac580486e3ee7579f864f32cf72082f938ec10c55a2e327dd3b3a8f8a8fd3f66d8d5f0cba33f1c815ad749beda6d91110c7cd53968cc7480dfab46020",
        "exhaust" : "https://w.namu.la/s/4f4996c8454d7e817989ee88476cf4117618864949dcefe1d185307bfff64fa1f7059a92add55f4ae3694f075a70014aec5ae2bc75e9793e4d8ff34a112f0fa9390063c31aa85d1836aa778e966bb983cdcd65a3fbb35d94c37fe5377238c268",
        "clarity" : "https://w.namu.la/s/a6facee9c5614923e1ffa174fd42112e501cff342eb1304d8b0fb3e60e2be76c36381bf8b88b258aeccdaf8ac42b1a30d3dff379c92016e8dada5d39e48bc4d5995e1826f660789c7548d68fd79aef6962de7dacb08e668351d37b413389b993",
        "mark" : "https://w.namu.la/s/4c9e4a9a976d9cf9c3f4c7b047e7b52d5b4f0a0db5e34979a3fe55cbc244798ebfb74e9fe0899c8ffe4fecdb79666db0781029958598e304dea76ca0ef277bd8efb574b2af6c8cc0deb68abf760c3b90d21ebbb797ef4cef8dff57801f3f2654",
        "teleport" : "https://w.namu.la/s/ba76227f2c557fd336fc92c38ba02fa0777e3fc43be87edad3d7a9879c0a7d45c0e8093bc1c2c6eabcf738948addf75c38a44d929d553ef190f52c92ebbf56f2b8de74d8e9ebe1f62a9f2bb78af22ff7454105cadbd7d9a7396709913f80f4ab",
        "flash" : "https://w.namu.la/s/06e57b45dae92c3c3217b874b06b296e86d8f8b654938689157d39f056a2aa9c1e8aca57857745a589f829d822c75356fea9ec13ea39960a0d3d8cc5368680b99eca55f4ff8709d101cd02cd0e4296bb2ca5e3225631924da1b5856532eebfc2",
        "smite" : "https://w.namu.la/s/f218c440c8f3a36920acf376c5249044e565dc76fdbaa7e6f8dd006b6dbefb83c7a421c469bccff9d2296d1271eb9f37804e7444c14fcf99b5299e85ae0eecd5351d562397b2d46a1e1fcbe5f306de59341a26ccd5f5e66af9e69ac815570fc9",
        "ignite" : "https://w.namu.la/s/20c1855d0e01d36e63377a9f5c03688a587ba438ae860fae6e13befbb66f1449eff9dfbbce42d4cafc788babf8e2256d22a5bfd300e961e4e3772282121223106acfbaaa3e1d69f0d309bd88dfc490e102591354b880227ecd4ed7c6b8ae04a6",
        "cleanse" : "https://w.namu.la/s/a71a59618845164b5773752ba8db244fbfd804606ce651efa06fa7f936566fbb0cf067800dd5cec665fcfc407a01f84be177fa9de810d838c2839a5650918f8c41b524da387a31125f09a58c6591734c4250bdced9b184e7a5f488c1828dd6ad",
        "precision" : "https://w.namu.la/s/cd3c472ec918b7e7469c05f8fc7b9a975d754206bbeabda127d26fd62f897b971bb90170ecea805ceac555671cea41eaee25a444b1e5145ea564fe7e87ab833f9da73de197ce1e4a8fb472f2759116ed3550b076dd57839e4eea98499cd1c460",
        "domination" : "https://w.namu.la/s/8011864adfd062deaa75821f937dde17de6cd3a96a7e30a3c017bd441f4ef7dd1712bec84cadf3490ef8968e92c4d477da97c6dcc53ba60c9bd22b506e42ac6e4303cf93d55c673d3f90c26b40a4262b66476d937d04fe9cc81d9b360ba2b858",
        "sorcery" : "https://w.namu.la/s/8c6cc21b9463439cdde93f7ad5975eb4c9193b9ebde9e61640d981cc59b5a8823c64866cbb3fb6dcc3f7ba58501a5d62392974462946ac25d6fbdf1940a95abacd39bb3cd21a6cfcf8888b8674d88dfa922b0b3c0bb51e981347d1eaca377050",
        "resolve" : "https://w.namu.la/s/8fad45e8c86575c6aa8552d3b34ad272a4a1d169988145129698f09386639adc0df9b3914385b00215dfad124380f810ab8d13d1edd800fd1c5fa99e323b10129e500f662879aac62e7025928bd6a7d35c50f9fefe519f8a5b564ad45f1612a0",
        "inspiration" : "https://w.namu.la/s/03ba9cde067b89d789f9196b6b377d4ddaa6680328044bf0300e995fcd90e95c12e6902bf004a45c19ad5bfdf1c1068d235f52a6b9d92bc385403079af40a53ac6b08e6719657908a90b4639fade2500de2fd2543e35eb64b23616789138fc84",
        "press the attack" : "https://w.namu.la/s/e08502dd6b90c662971a418334fe7fbf1ab11cc01446965f7669d55c0ef9fb70e39a8ad5a98cf4707c48e7d0bdfaffee093102c718b5a4cebeb8bb62719b2e796554b4696244cef8c1bc3cecf230c3d3e9b725a9c3403bad003352af968f18d8",
        "lethal tempo" : "https://w.namu.la/s/541a182999bd0cfcf0cf679de4a1771a3b6c21073af1b7afa527fa4b4996627b05c063be2cef383613d51a7d52c2b8ec51c0d4135b022f64672c8f467eda81b7f68a37d998b27b18aa50fc4373e78bfc4cbf38567827741ddec394117a3a8d6f",
        "fleet footwork" : "https://w.namu.la/s/48c74f159a33a857b9c788b253a23d38e5bc676134bf4ad7a856a3c6ae9cca01a85f4729b544d50cd7af776d910bf31d93ae5fac6a74225b553a4154bf452272d896b3ea810f30e6631b5401941d36dafe6dc6fce13a29dd23d53c47cd5a8d59",
        "conqueror" : "https://w.namu.la/s/7d15d83e176aea3884e20fbf435fc81c11200dc3b59c79ec491fb67ab407a562db27e5ce65cd0bc3aee098b2558d2da0bced6e5bc6c8ad7c25d3ff48f7c154ac543dc40d3e296d079b120710baaff4334deb0f6d1a58ac6a63b0fc481b5c44b3",
        "electrocute" : "https://w.namu.la/s/8f8c2bdf9e11c41d63924d236b55c7e51e3424fba7a22f7bb2e73279f50d68bcb2d28790cff24fed2e6f2b71fd8473a01b41b4ae5cd478d032db844baa74e2dd4b6af9bccef02faa7d978ae5efdee9f2fae5e40947de498638385e28f4357da7",
        "predator" : "https://w.namu.la/s/e672ab95d044cd3b50dbffc3841b8d802d34bbee3cb6b0d67e1de90164e17fd479899a5dd77ff27941429d67ecc81fa4c6eacffae1c4ece96e3603167f82b3439ee898b02834ed65ba0616f0edbe9554a6e93c7488bf7e74b483d06755bdf9b1",
        "dark harvest" : "https://w.namu.la/s/634b1a0d73d6845b8a34fb629cd46ff2b4b3d27ae7b36d8645203b011c9517cc5ba4e0ed515b41e3b7d5707c7ad860766678ea09e0e076d6735482a131ef1244614f0c058611168c24cbc5b4d48a117d44ae6fd2e899c1108ca667a068c39814",
        "hail of blades" : "https://w.namu.la/s/f9913b876f44e37a450f1265b31bdab541bf77a3c85e6858a1b237eb77921aa38c311385cedbf95c0c051d24438e9a80fbe7e2ecba72db9b20850521e23a01398d9b93b0def5c5b4dbe305f2eac5bb23f11fb30251d78f59d2c46acfe0d8600e",
        "summon aery" : "https://w.namu.la/s/192a01ff0195ac5284426eca799356b3b0637d305f2ac69f3a5b871326e6c47931c206d00d703525cfb8c90c3972bcfba4d52b945b3f7f104c8c604abe123d180f1d90493d18ea4064e5978a90ca00a46ac83ca3c4cdb0028dde04fba6959871",
        "arcane comet" : "https://w.namu.la/s/082c5ef2f139974c715b1fc1087bbfac1119d28f4bff2041ad91ca28eacfd35515a4852499b509cce25eb7f5048baddb8c099285e5fbcf8192166fa4bc6931d710fbd7c933a817dcceda10823c656d87cdc1f43933e2c513b02831a0c79b16a9",
        "phase rush" : "https://w.namu.la/s/97521bf8e88cc5f44f5628c9d29bf339961769d29b77f7399ae83539a7d3de6eef77f81fecfad8bfebbc37a677accf7986a43df6c78333c6be5b1db50cccf1f7005670df2c071b003091f92f776aac1cf2c011be0015f49c04d39aa5ce93ca4b",
        "grasp of the undying" : "https://w.namu.la/s/e5192766397fd7d2cc767af2112e596e1810e80caa3f5ff8abb00448a2847d6958b8107039998273ddf5bca4c9c675e06892d89ea5b1281ca4be6944a88722bd104b1592451f9737b4ff649a6db4d9f595b7f25b2b7e5fe0df9ff8c61d867d71",
        "aftershock" : "https://w.namu.la/s/51e6396b4351bfbd2747c1df26ae6913e71c5570d42afd6515fbc4958bc10294c5f4e96f5b87ac37a2311e8ef01940ecc558fa7f0c4a424990de63984d23c8578f4049076f5e772d56576808d28a537fafa62f1614911e58cac7fdda8c44b5f5",
        "guardian" : "https://w.namu.la/s/2f9ea37b7ae85f8c4183c2f844add32c9394079e9e5f0f8e651e1b529ec672253c6c32341ee9348ed38146bcfd1326f8162f76893746c725c8c24cdbd16c9be8f67497dceed366088975666d72d79819c9466b102b9c3914dca36b8e419f83d6",
        "glacial augment" : "https://w.namu.la/s/8639eee67b8638fd6582798d61a4f1465ed9f468bad3ac636704be3a652093536925823db4604ad88ada89dc6d61f271eec8cf45302b1c002dc9c016969fe73ae77e42c75b53f3984bae249bc120a0da239b1b2554133426f42045eb61f8afe6",
        "unsealed spellbook" : "https://w.namu.la/s/7885920e6725fd914ba1d7b3fd314ae37ce5720dd7bb5726a493ee2db4063e2568b032dd014446f83160fa88eac6b97b19ba614db22ea36ef8906aab8090a68469b2302d73a0b6d24f799fd8087f4302933a9b9abca3816fae8972d9afaf65f6",
        "first strike" : "https://w.namu.la/s/403328112bf0954ed0d4bae80e2a9d5b06e0a365ad08fc18bd59ec24f44e080601de580b56abe51f1ac8df7effde5d7ef83f4f0cae208849b92fe7de491fd75f90110fef1040ac52e098881bbfc0e48589dd37aaf21311b2fecc5359c7167736"
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