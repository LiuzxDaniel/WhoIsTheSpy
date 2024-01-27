from easygui import *
from random import *
from undercover_wordsbank import wordsdic

msgbox('谁是卧底小游戏！', '谁是卧底', 'start game!')

def winorlose(pnum, bnum, wnum):
    if pnum <= bnum + wnum:
        return '卧底胜利'
    if bednum == 0 and whitenum == 0:
        return '平民胜利'

while True:
    words = [i for i in wordsdic.items()]
    playercheck = []
    ranwords = randint(0, len(wordsdic)-1)
    wordslis = []
    people = 0
    peoplenum = 0
    bednum = 0
    whitenum = 0
    bedindex = []
    peoplelis = []
    whiteindex = None

    people = buttonbox('人数选择(默认为3人)：', '谁是卧底', choices=('3', '4', '5', '6'))
    if people:
        people = int(people)
    if not people:
        people = 3
    if people != 3:
        whiteboard = buttonbox('白板(默认为关闭)：', '谁是卧底', choices=('开启', '关闭'))
        if whiteboard == '开启':
            whitenum = 1
            bednum = round(people / 3) - 1
            peoplenum = people - bednum - whitenum

        else:
            bednum = round(people / 3)
            peoplenum = people - bednum
            whitenum = 0

        del whiteboard

    else:
        bednum = round(people / 3)
        peoplenum = people - bednum
        whitenum = 0
    player = [str(i)+'号玩家' for i in range(1, people+1)]
    msgbox(f'本局有{peoplenum}个平民，{bednum}个卧底，{whitenum}个白板', '谁是卧底')
    peoplelis = [i for i in range(people)]

    if whitenum:
        whiteindex = choice(peoplelis)
        del peoplelis[whiteindex]

    if bednum == 1:
        bedindex.append(choice(peoplelis))
        del peoplelis[bedindex[0]-1]
    
    if bednum == 2:
        for i in range(0 ,2):
            bedindex.append(choice(peoplelis))
            del peoplelis[bedindex[i]]

    for i in range(people):
        msgbox(player[i]+'词语查询', '谁是卧底', '查看')
        if i == whiteindex:
            msgbox('白板\n小心别被别人看到了！', '谁是卧底')
            playercheck.append('白板')
        elif i in bedindex:
            msgbox(words[ranwords][0]+'\n小心别被别人看到了！', '谁是卧底')
            playercheck.append('卧底')
        else:
            msgbox(words[ranwords][1]+'\n小心别被别人看到了！', '谁是卧底')
            playercheck.append('平民')

    for i in playercheck:
        if i == '卧底':
            wordslis.append(words[ranwords][0])
        elif i == '平民':
            wordslis.append(words[ranwords][1])
        else:
            wordslis.append('白板')

    while True:
        diepeople = multchoicebox('出局人员：', '谁是卧底', player)
        if diepeople:
            player = list(set(player) - set(diepeople))
            player.sort()
            for i in range(len(diepeople)):
                name = playercheck[int(diepeople[i][0])-1]
                if name == '平民':
                    peoplenum -= 1
                elif name == '卧底':
                    bednum -= 1
                else:
                    whitenum -= 1
            win = winorlose(peoplenum, bednum, whitenum)
            if win:
                if win == '卧底胜利':
                    msgbox('卧底胜利', '谁是卧底', '解开底牌')
                else:
                    msgbox('平民胜利', '谁是卧底', '解开底牌')
                break

    text = ''
    for i in range(len(playercheck)):
        playercheck[i] = f'{i+1}号玩家是{playercheck[i]} 词语是：{wordslis[i]}'
        text += playercheck[i]+'\n'

    choiceexit = indexbox(text, '谁是卧底', ['进入下一轮游戏', '退出游戏'])
    if choiceexit:
        break
    if choiceexit==None:
        break
