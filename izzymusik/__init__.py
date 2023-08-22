from izzymusik.core.bot import Anony
from izzymusik.core.dir import dirr
from izzymusik.core.git import git
from izzymusik.core.userbot import Userbot
from izzymusik.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
