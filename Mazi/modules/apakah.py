import random
from Mazi.events import register
from Mazi import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Harus banget gua jawab?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Nanya Mulu lu"
                 ]
                 
KENAPA_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "Harus banget gua jawab?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Nanya Mulu lu"
                 ]
                 
BAGAIMANA_STRING = ["Tau ya", 
                 "Ngapa si ?", 
                 "Jamet", 
                 "Diem Jamet", 
                 "Berisik lu", 
                 "Bacot",
                 "Astaghfirullah, Anj",
                 "Ya Allah, coli mulu?",
                 "Apaansi nanya mulu lu",
                 "Emang bener?",
                 "Mana gua tau ",
                 "Lu tanya gua, terus gua tanya siapa?",
                 "Nanya Mulu lu"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
    
@register(pattern="^/kenapa ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(KENAPA_STRING))
    
@register(pattern="^/bagaimana ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(BAGAIMANA_STRING))
