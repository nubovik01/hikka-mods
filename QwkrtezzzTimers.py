#                  _         _                   
#    __ ___      _| | ___ __| |_ ___ ____________
#   / _` \ \ /\ / / |/ / '__| __/ _ \_  /_  /_  /
#  | (_| |\ V  V /|   <| |  | ||  __// / / / / / 
#   \__, | \_/\_/ |_|\_\_|   \__\___/___/___/___|
#      |_|                                       
#                 © Copyright 2023
#              https://t.me/qwkrtezzz
#                   
# 🔒         Licensed under the GNU AGPLv3
# 🌐   https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @nbvkxd

from .. import loader, utils
from datetime import datetime

def getTime(month, day):
  now = datetime.now()
  date = datetime(now.year, month, day)

  if now.month > month or (now.month == month and now.day > day):
    date = datetime(now.year+1, month, day)
    timeToIt = abs(date-now)

  return timeToIt

class QwkrtezzzTimers(loader.Module):
  '''Таймеры до начала определённых событий'''

  strings = {'name': 'QwkrtezzzTimers'}

  @loader.command()
  async def summertime(self, message):
    """узнать сколько времени осталось до лета"""
    timeToSummer = getTime(6, 1)

    await utils.answer(message, (f'До лета осталось {timeToSummer.days} дней, {timeToSummer.seconds // 3600} часов, {timeToSummer.seconds // 60 % 60} минут, {timeToSummer.seconds % 60} секунд.\n'))
