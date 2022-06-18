import random
play_game = 'c'  
  
while play_game == 'c':
  def play():
      user = input("what's yout choice? Rock(r), Paper(p), Sissor(s)")
      computer = random.choice(['r', 'p', 's'])

      if user == computer:
          return 'It\'s a tie!'

        
      if is_win(user, computer):
          return 'You won!'

      
      return 'You lost!'      

  def is_win (player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

  print(play())               
  play_game = input("Continue (c): ")