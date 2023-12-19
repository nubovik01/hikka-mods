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
    """Узнать сколько времени осталось до лета"""
    timeToSummer = getTime(6, 1)

    await utils.answer(
      message, 
       (
         f'До лета осталось '
         f'{timeToSummer.days} дней, '
         f'{timeToSummer.seconds // 3600} часов, '
         f'{timeToSummer.seconds // 60 % 60} минут, '
         f'{timeToSummer.seconds % 60} секунд.'
       )
    )

  @loader.command()
  async def newyeartime(self, message):
    """Узнать сколько времени осталось до нового года"""
    timeToNewYear = getTime(12, 31)

    await utils.answer(
      message, 
       (
         f'До нового года осталось '
         f'{timeToNewYear.days} дней, '
         f'{timeToNewYear.seconds // 3600} часов, '
         f'{timeToNewYear.seconds // 60 % 60} минут, '
         f'{timeToNewYear.seconds % 60} секунд 🎄'
       )
    )

  @loader.command()
  async def qwzbirthday(self, message):
    """Узнать сколько времени до дня рождения разработчика этого модуля (Никиты/Qwkrtezzz)"""
    timeToBirthday = getTime(4, 9)

    await utils.answer(
      message, 
       (
         f'До дня рождения разработчика модуля QwkrtezzzTimers осталось '
         f'{timeToBirthday.days} дней, '
         f'{timeToBirthday.seconds // 3600} часов, '
         f'{timeToBirthday.seconds // 60 % 60} минут, '
         f'{timeToBirthday.seconds % 60} секунд 🎁 🎉'
       )
    )
