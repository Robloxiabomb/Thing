import emoji
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from random import choice
import time
import keyboard
from pygame import mixer
#I know functions is spelt wrong. Don't judge me
class Colors:
  Black=  u'\u001b[30m'
  Red = u'\u001b[31m'
  Green = u'\u001b[32m'
  Yellow= u'\u001b[33m'
  Blue= u'\u001b[34m'
  Magenta=  u'\u001b[35m'
  Cyan = u'\u001b[36m'
  White = u'\u001b[37m'
  Reset = u'\u001b[0m'
  Bold = u'\u001b[1m'
  Underline = u'\u001b[4m'
  reversedColor = u'\u001b[7m'
  OrangeBG = "\033[48:5:208m"
  BYellow = u'\u001b[33;1m'
  BGBlack = u'\u001b[40m'
def boardLayout(Board):
  print('              Board Layout')
  print('     1  ', ' 2', '   3  ', ' 4  ', ' 5  ', ' 6  ', ' 7')
  for x in range(len(Board)):
    if x == 5:
      print(str(x+1) + ' | '+' | '.join(Board[x]),'|')
      print('  ⌞__________________________________⌟')
    else:  
      print(str(x+1) + ' | '+' | '.join(Board[x]),'|')
      print('  +----+----+----+----+----+----+----⫞')
  print('\n')
#TIL - The short right tac unicode character exists but the left one does not. I spent over an hour trying to find that.
def Tutorial():
  f = open('tutorial.txt', 'r')
  TutorialArray = f.read().split(';')
  endCount = 0
  keyCount = 1
  Key = ''
  os.system('cls' if os.name == 'nt' else 'clear')
  exec(TutorialArray[0])
  while True:
    Key = keyboard.read_key()
    while Key not in ['up','down','esc']:
      Key = keyboard.read_key()
    if keyCount == len(TutorialArray)-1 and Key == 'down':
      keyCount = 1
    os.system('cls' if os.name == 'nt' else 'clear')

    if Key == 'up' and keyCount > 0:
      keyCount-=1
      exec(TutorialArray[keyCount])
    elif Key == 'down' and endCount < 10 and keyCount == 15:
      exec(TutorialArray[keyCount])
      endCount += 1
    elif Key == 'down' and keyCount < len(TutorialArray):
      keyCount+=1
      exec(TutorialArray[keyCount])
    elif Key == 'esc':
      print('Ok get ready to start the game.')
      time.sleep(2)
      break
    time.sleep(0.3)
def pinput(Board, i, powerCount):
  p1p2 = [emoji.emojize(':skull:'), emoji.emojize(':vampire:')]
  items = ['t']
  row = 2
  column = 2
  RorY = p1p2[i%2]
  chipChoice = '1'
  while items[int(chipChoice)-1]== 't':
    Flag = False
    valid = False
    while not valid:
      boardLayout(Board)
      print(Colors.Bold + RorY + "'s turn" + Colors.Reset)
      count = 1
      items = ['c']
      print(str(count) +'. Chip')
      count += 1
      if powerCount[i%2] > 0:
        print(str(count) + emoji.emojize('. :bat:'), powerCount[(i%2)], 'remaining')
        count += 1
        items.append('b')
      if powerCount[i%2+2] > 0:
        print(str(count) + emoji.emojize('. :ghost:'), powerCount[(i%2)+2], 'remaining')
        count += 1
        items.append('g')
      if powerCount[i%2+4] > 0:
        print(str(count) + emoji.emojize('. :zombie:'), powerCount[(i%2)+4],'remaining')
        items.append('z')
        count += 1
      print(str(count) + '. Tutorial')
      items.append('t')
      chipChoice = input('')
      
      
      try:
        if int(chipChoice) < 1 or int(chipChoice) > len(items):
          os.system('cls' if os.name == 'nt' else 'clear')
          print(Colors.Red + 'ERROR: ENTER A NUMBER BETWEEN 1 AND',str(len(items))+Colors.Reset)
        else:
          valid = True
          os.system('cls' if os.name == 'nt' else 'clear')
      except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colors.Red + 'ERROR: ENTER A NUMBER'+Colors.Reset)
    while not Flag:
      boardLayout(Board)
      if items[int(chipChoice)-1] == 'z' or items[int(chipChoice)-1] == 'b':
        row = input(RorY+' Enter which row you want to clear [1-6]:\n')
      if items[int(chipChoice)-1] not in ['z', 't', 'ch']:
        column = input(RorY+ ' Enter which column you want to place your item in [1-7]:\n')
      try:
        if int(column) < 1 or int(column) > 7:
          os.system('cls' if os.name == 'nt' else 'clear')
          print(Colors.Red + 'ERROR: NUMBER NOT IN RANGE'+Colors.Reset)
        elif int(row) < 1 or int(row)>6:
          os.system('cls' if os.name == 'nt' else 'clear')
          print(Colors.Red + 'ERROR: NUMBER NOT IN RANGE ENTER A NUMBER BETWEEN 1 AND 6' + Colors.Reset)
        
        elif items[int(chipChoice)-1] == 'c':
          Flag = True
          return RorY, int(column),False,'c'
        elif items[int(chipChoice)-1] == 'b':
          powerCount[i%2] -= 1
          Flag = True
          return RorY, False, int(row), 'b'
        elif items[int(chipChoice)-1] == 'g':
          powerCount[(i%2)+2]-=1
          Flag = True
          return RorY, int(column), False, 'g'
        elif items[int(chipChoice)-1] == 'z':
          powerCount[(i%2)+4]-=1
          return RorY, False, int(row), 'z'
          Flag = True
        elif items[int(chipChoice)-1] == 't':
          Tutorial()
          Flag = True
      except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colors.Red + 'ERROR: ENTER A NUMBER'+Colors.Reset)
def floatingRemover(Board):
  Rnum = 6
  Cnum = 7
  Flag = True
  while Flag:
    Flag = False
    for i  in range(1, Rnum):
      for j in range(Cnum):
          if Board[i][j] == emoji.emojize(':black_circle:') and Board[i-1][j] != emoji.emojize(':black_circle:'):
            Flag = True
            Board[i][j] = Board[i-1][j]
            Board[i-1][j] = emoji.emojize(':black_circle:')
def batBomb(Board,column, row):
  time.sleep(0.5)
  column, row = int(column), int(row)
  os.system('cls' if os.name == 'nt' else 'clear')
  Board[row-1][column-1] = emoji.emojize(':bat:')
  boardLayout(Board)
  row = row - 1
  column = column - 1
  mixer.Channel(1).play(mixer.Sound('Songs\Explosion.wav'))
  if column - 1 >= 0:
    Board[row][column-1] = emoji.emojize(':collision:')
  if column + 1 <= 6:
    Board[row][column+1] = emoji.emojize(':collision:')
  if row +1 <= 5:
    Board[row+1][column] = emoji.emojize(':collision:')
  if row-1 >= 0:
    Board[row-1][column] = emoji.emojize(':collision:')
  os.system('cls' if os.name == 'nt' else 'clear')
  boardLayout(Board)
  time.sleep(1)
  mixer.Channel(1).stop
  if column - 1 >= 0:
    Board[row][column-1] = emoji.emojize(':black_circle:')
  if column + 1 <= 6:
    Board[row][column+1] = emoji.emojize(':black_circle:')
  if row +1 <= 5:
    Board[row+1][column] = emoji.emojize(':black_circle:')
  if row-1 >= 0:
    Board[row-1][column] = emoji.emojize(':black_circle:')
  Board[row][column] = emoji.emojize(':black_circle:')
  floatingRemover(Board)
def ghost(Board, column):
  mixer.Channel(1).play(mixer.Sound('Songs\Ghost Moan.wav'))
  for i in range(len(Board)):
    Board[i][int(column)-1] = emoji.emojize(':ghost:')
    Board[i-1][int(column)-1] = emoji.emojize(':black_circle:')
    time.sleep(0.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    boardLayout(Board)
  mixer.Channel(1).stop()
  Board[-1][int(column)-1] = emoji.emojize(':black_circle:')
def zombie(Board,row):
  mixer.Channel(1).play(mixer.Sound('Songs\Zombie Groan.wav'))
  for i in  range(len(Board[int(row)-1])):
    Board[int(row)-1][i] = emoji.emojize(':zombie:')
    Board[int(row)-1][i-1] = emoji.emojize(':black_circle:')
    time.sleep(0.4)
    os.system('cls' if os.name == 'nt' else 'clear')
    boardLayout(Board)
  mixer.Channel(1).stop
  Board[int(row)-1][-1] = emoji.emojize(':black_circle:')
  floatingRemover(Board)
def chip(RorY,Board, column):
  Flag = False
  for i in range(len(Board)):
    boardCheck = Board[::-1]
    if boardCheck[i][int(column)-1] == emoji.emojize(':black_circle:'):
      boardCheck[i][int(column)-1] = RorY
      Flag = True
      break
  if Flag == True:
    Board = boardCheck[::-1]
    return True
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colors.Red + 'ERROR: SPACES FULL'+Colors.Reset)
    return False
def chipPlacement(Board, RorY, column, row,id):
  if id == 'c':
    chip(RorY, Board, column)
    return chip
  elif id == 'g':
    ghost(Board,column)
  elif id == 'z':
    zombie(Board,row)
  else:
    batBomb(Board, column, row)
def winCheck(Board):
  Cnum = 7
  Rnum = 6
  #Vertical
  for i in range(Rnum-3):
    for j in range(Cnum):
      winCol = {Board[i][j], Board[i+1][j], Board[i+2][j], Board[i+3][j]}
      if len(winCol) == 1 and winCol != {emoji.emojize(':black_circle:')}:
        return list(winCol)[0] + ' wins'
  
  #Horizontal
  for i in range(Rnum):
    for j in range(Cnum-3):
      winRow = {Board[i][j], Board[i][j+1], Board[i][j+2], Board[i][j+3]}
      if len(winRow) == 1 and list(winRow)[0] != emoji.emojize(':black_circle:'):
        return list(winRow)[0]+ ' wins'
  
  
  #Left Diagonal
  for i in range(Rnum-3):
    for j in range(Cnum-3):
      winDR = {Board[i][j], Board[i+1][j+1], Board[i+2][j+2], Board[i+3][j+3]}
      if len(winDR) == 1 and list(winDR)[0] != emoji.emojize(':black_circle:'):
        return list(winDR)[0] + ' wins'
  
  #Right Diagonal
  for i in range(Rnum-3):
    for j in range(3, Cnum):
      winDL = {Board[i][j], Board[i+1][j-1], Board[i+2][j-2], Board[i+3][j-3]}
      if len(winDL) == 1 and list(winDL)[0] != emoji.emojize(':black_circle:'):
        return list(winDL)[0] + ' wins'
  return ''
def bloodFall(RorY, Board):
  os.system('cls' if os.name == 'nt' else 'clear')
  mixer.Channel(1).play(mixer.Sound('Songs\Scream.wav'))
  time.sleep(3)
  mixer.Channel(2).play(mixer.Sound('Songs\SCHLUUUUURP.wav'), 100)
  RorY = emoji.emojize(':drop_of_blood:')
  count = 0
  columns = [1, 2, 3, 4, 5, 6, 7]
  for i in range(len(Board[-1])):
    Board[0][i] = RorY
  while count < 35:
    column = choice(columns)
    Flag = False
    for i in range(len(Board)):
      if Board[i][column-1] != emoji.emojize(':drop_of_blood:'):
        Board[i][column-1] = RorY
        Flag = True
        if i%2 == 1:
          os.system('cls' if os.name == 'nt' else 'clear')
          boardLayout(Board)
        break
    if Flag == True:
      count += 1
      time.sleep(0.2)
    else:
      columns.remove(column)
  mixer.stop