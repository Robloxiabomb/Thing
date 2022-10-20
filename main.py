from functoins import *

print('By: Leo M.')
mixer.init()
SpookySong = mixer.Sound('Songs\SpookySong.wav')
mixer.Channel(3).play(SpookySong, 1000)
mixer.Channel(3).set_volume(0.1)
print(
Colors.Bold + Colors.Yellow + Colors.BGBlack + '''  
  ______    ______   __    __  __    __  ________   ______   ________   '''+Colors.Red+'''     __    __ '''+ Colors.Yellow + '''
 /      \  /      \ /  \  /  |/  \  /  |/        | /      \ /        |'''+Colors.Red + '''      /  |  /  |'''+Colors.Yellow+'''
/$$$$$$  |/$$$$$$  |$$  \ $$ |$$  \ $$ |$$$$$$$$/ /$$$$$$  |$$$$$$$$/  '''+Colors.Red +'''     $$ |  $$ |'''+Colors.Yellow+'''
$$ |  $$/ $$ |  $$ |$$$  \$$ |$$$  \$$ |$$ |__    $$ |  $$/    $$ |   '''+Colors.Red +'''      $$ |__$$ |'''+Colors.Yellow+'''
$$ |      $$ |  $$ |$$$$  $$ |$$$$  $$ |$$    |   $$ |         $$ |   '''+Colors.Red +'''      $$    $$ |'''+Colors.Yellow+'''
$$ |   __ $$ |  $$ |$$ $$ $$ |$$ $$ $$ |$$$$$/    $$ |   __    $$ |   '''+Colors.Red +'''      $$$$$$$$ |'''+Colors.Yellow+'''
$$ \__/  |$$ \__$$ |$$ |$$$$ |$$ |$$$$ |$$ |_____ $$ \__/  |   $$ |   '''+Colors.Red +'''            $$ |'''+Colors.Yellow+'''
$$    $$/ $$    $$/ $$ | $$$ |$$ | $$$ |$$       |$$    $$/    $$ |   '''+Colors.Red +'''            $$ |'''+Colors.Yellow+'''
 $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$$$$$$$/  $$$$$$/     $$/    '''+Colors.Red +'''            $$/ ''' + Colors.Reset
)
print(Colors.OrangeBG + Colors.Black + Colors.Bold + ''' _   _    __    __    __    _____  _    _  ____  ____  _  _ 
( )_( )  /__\  (  )  (  )  (  _  )( \/\/ )( ___)( ___)( \( )
 ) _ (  /(__)\  )(__  )(__  )(_)(  )    (  )__)  )__)  )  ( 
(_) (_)(__)(__)(____)(____)(_____)(__/\__)(____)(____)(_)\_)''' + Colors.Reset)
input('Press enter to continue:\n')
Board = [[emoji.emojize(':black_circle:')]*7 for i in range(6)]
powerCount = [3]*6
i = 0





Tutorial()
while emoji.emojize(':black_circle:') in Board[0]:
  RorY,column,row,id = pinput(Board, i, powerCount)
  while chipPlacement(Board,RorY,column,row,id) == False:
    RorY, column,row,id = pinput(Board, i, powerCount)
    chipPlacement(Board,RorY,column,row,id)
  WorL = winCheck(Board, RorY)
  if WorL == '':
    pass
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    boardLayout(Board)
    input(WorL + ' Press enter to continue: \n')
    break
  os.system('cls' if os.name == 'nt' else 'clear')
  i += 1
if emoji.emojize(':black_circle:') not in Board[0]:
  os.system('cls' if os.name == 'nt' else 'clear')
  boardLayout(Board)
  input('Draw! Press enter to continue: \n')


bloodFall(RorY, Board)