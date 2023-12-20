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

# meta developer: @nbvkxd

from .. import loader, utils
from datetime import datetime

def getTime(month, day):
  now = datetime.now()
  date = datetime(now.year, month, day)

  if now.month > month or (now.month == month and now.day > day):
    date = datetime(now.year+1, month, day)

  return abs(date-now)

def getTimezone():
  return datetime.now().astimezone().tzinfo

@loader.tds
class QwkrtezzzTimers(loader.Module):
  """Таймеры до начала определённых событий"""

  strings_ru = {
    "name": "QwkrtezzzTimers",
    "timeUntilEvent": "До {} осталось {}d, {}h, {}m, {}s ({}) {}",
    "spring": "весны 🏖",
    "summer": "лета ☀️",
    "autumn": "осени 🍁",
    "winter": "зимы ❄️ ☃️",
    "newYear": "нового года 🎄",
    "qwzBirthday": "дня рождения разработчика модуля QwkrtezzzTimers 🎉 🎁"
  }

  strings_en = {
    "name": "QwkrtezzzTimers",
    "timeUntilEvent": "Until {} left {}d, {}h, {}m, {}s ({}) {}",
    "spring": "spring 🏖",
    "summer": "summer ☀️",
    "autumn": "autumn 🍁",
    "winter": "winter ❄️ ☃️",
    "newYear": "New Year 🎄",
    "qwzBirthday": "the birthday of the QwkrtezzzTimers module developer 🎉 🎁",
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

    await utils.answer(message, self.strings("timeUntilEvent").format(
      self.strings("spring"),
      timeToSpring.days,
      timeToSpring.seconds // 3600,
      timeToSpring.seconds // 60 % 60, 
      timeToSpring.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))

  async def summertimecmd(self, message):
    """Узнать сколько времени осталось до лета"""
    timeToSummer = getTime(6, 1)

    await utils.answer(message, self.strings("timeUntilEvent").format(
      self.strings("summer"),
      timeToSummer.days, 
      timeToSummer.seconds // 3600, 
      timeToSummer.seconds // 60 % 60, 
      timeToSummer.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))

  async def autumntimecmd(self, message):
    """Узнать сколько времени осталось до осени"""
    timeToAutumn = getTime(9, 1)

    await utils.answer(message, self.strings("timeUntilEvent").format(
      self.strings("autumn"),
      timeToAutumn.days,
      timeToAutumn.seconds // 3600,
      timeToAutumn.seconds // 60 % 60,
      timeToAutumn.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))

  async def wintertimecmd(self, message):
    """Узнать сколько времени осталось до зимы"""
    timeToWinter = getTime(12, 1)

    await utils.answer(message, self.strings("timeUntilEvent").format(
      self.strings("winter"),
      timeToWinter.days,
      timeToWinter.seconds // 3600,
      timeToWinter.seconds // 60 % 60,
      timeToWinter.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))

  async def newyeartimecmd(self, message):
    """Узнать сколько времени осталось до нового года"""
    timeToNewYear = getTime(12, 31)

    await utils.answer(message,self.strings("timeUntilEvent").format(
      self.strings("newYear"),
      timeToNewYear.days, 
      timeToNewYear.seconds // 3600, 
      timeToNewYear.seconds // 60 % 60,
      timeToNewYear.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))

  async def qwzbirthdaycmd(self, message):
    """Узнать сколько времени осталось до дня рождения разработчика этого модуля (Никиты/Qwkrtezzz)"""
    timeToBirthday = getTime(4, 9)

    await utils.answer(message, self.strings("timeUntilEvent").format(
      self.strings("qwzBirthday"),
      timeToBirthday.days, 
      timeToBirthday.seconds // 3600, 
      timeToBirthday.seconds // 60 % 60, 
      timeToBirthday.seconds % 60,
      getTimezone(),
      utils.ascii_face()
    ))
