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

@loader.tds
class QwkrtezzzTimers(loader.Module):
  """Таймеры до начала определённых событий"""

  strings_ru = {
    "name": "QwkrtezzzTimers",
    "timeUntilSpring": "До весны осталось {} дней, {} часов, {} минут, {} секунд",
    "timeUntilSummer": "До лета осталось {} дней, {} часов, {} минут, {} секунд",
    "timeUntilAutumn": "До осени осталось {} дней, {} часов, {} минут, {} секунд",
    "timeUntilWinter": "До зимы осталось {} дней, {} часов, {} минут, {} секунд",
    "timeUntilQwzBirthday": "До дня рождения разработчика модуля QwkrtezzzTimers осталось {} дней, {} часов, {} минут, {} секунд 🎁 🎉",
    "timeUntilNewYear": "До Нового Года осталось {} дней, {} часов, {} минут, {} секунд"
  }

  strings_en = {
    "name": "QwkrtezzzTimers",
    "timeUntilSpring": "{} days, {} hours, {} minutes, {} seconds left until spring",
    "timeUntilSummer": "{} days, {} hours, {} minutes, {} seconds left until summer",
    "timeUntilAutumn": "{} days, {} hours, {} minutes, {} seconds left until autumn",
    "timeUntilWinter": "{} days, {} hours, {} minutes, {} seconds left until winter",
    "timeUntilQwzBirthday": "There are {} days, {} hours, {} minutes, {} seconds left until the birthday of the QwkrtezzzTimers module developer",
    "timeUntilNewYear": "{} days, {} hours, {} minutes, {} seconds left until New Year",
    "_cmd_doc_springtime": "Find out how much time is left until spring",
    "_cmd_doc_summertime": "Find out how much time is left until summer",
    "_cmd_doc_autumntime": "Find out how much time is left until autumn",
    "_cmd_doc_wintertime": "Find out how much time is left until winter",
    "_cmd_doc_newyeartime": "Find out how much time is left until New Year",
    "_cmd_doc_qwzbirthday": "Find out how much time is left until the birthday of the developer of this module (Nikita/Qwkrtezzz)",
    "_cls_doc": "Timers until certain events start"
  }

  async def springtimecmd(self, message):
    """Узнать сколько времени осталось до весны"""
    timeToSpring = getTime(3, 1)

    await utils.answer(message, self.strings("timeUntilSpring").format(timeToSpring.days, timeToSpring.seconds // 3600, timeToSpring.seconds // 60 % 60, timeToSpring.seconds % 60))

  async def summertimecmd(self, message):
    """Узнать сколько времени осталось до лета"""
    timeToSummer = getTime(6, 1)

    await utils.answer(message, self.strings("timeUntilSummer").format(timeToSummer.days, timeToSummer.seconds // 3600, timeToSummer.seconds // 60 % 60, timeToSummer.seconds % 60))

  async def autumntimecmd(self, message):
    """Узнать сколько времени осталось до осени"""
    timeToAutumn = getTime(9, 1)

    await utils.answer(message, self.strings("timeUntilAutumn").format(timeToAutumn.days, timeToAutumn.seconds // 3600, timeToAutumn.seconds // 60 % 60, timeToAutumn.seconds % 60))

  async def wintertimecmd(self, message):
    """Узнать сколько времени осталось до зимы"""
    timeToWinter = getTime(12, 1)

    await utils.answer(message, self.strings("timeUntilWinter").format(timeToWinter.days, timeToWinter.seconds // 3600, timeToWinter.seconds // 60 % 60, timeToWinter.seconds % 60))

  async def newyeartimecmd(self, message):
    """Узнать сколько времени осталось до нового года"""
    timeToNewYear = getTime(12, 31)

    await utils.answer(message, self.strings("timeUntilNewYear").format(timeToNewYear.days, timeToNewYear.seconds // 3600, timeToNewYear.seconds // 60 % 60, timeToNewYear.seconds % 60))

  async def qwzbirthdaycmd(self, message):
    """Узнать сколько времени осталось до дня рождения разработчика этого модуля (Никиты/Qwkrtezzz)"""
    timeToBirthday = getTime(4, 9)

    await utils.answer(message, self.strings("timeUntilQwzBirthday").format(timeToBirthday.days, timeToBirthday.seconds // 3600, timeToBirthday.seconds // 60 % 60, timeToBirthday.seconds % 60))