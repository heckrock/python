import random
#rock = 1
#paper = 2
#sissors = 3
while True:
    my_rps_draw=int(input('''
Pick an option:
1) Rock
2) Paper
3) Sissors
'''))
    cpu_rps_draw=random.randint(1,3)

    if my_rps_draw==1:
        print('''
            You drew
                  _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''')
    elif my_rps_draw==2:
        print('''
          You drew
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
          ''')
    elif my_rps_draw==3:
        print('''
          You drew
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
          ''')
    else:
        print("Invalid option!")

    if cpu_rps_draw==1:
        print('''
          CPU drew
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
          ''')
    elif cpu_rps_draw==2:
         print('''
          CPU drew
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
          ''')
    else:
         print('''
          CPU drew
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
          ''')

    if my_rps_draw==1:
         if cpu_rps_draw==1:
           result="Draw"
         elif cpu_rps_draw==2:
            result="CPU wins"
         else:
            result="You win"
    elif my_rps_draw==2:
         if cpu_rps_draw==1:
           result="You win"
         elif cpu_rps_draw==2:
            result="Draw"
         else:
            result="CPU wins"
    elif my_rps_draw==3:
      if cpu_rps_draw==1:
           result="CPU wins"
      elif cpu_rps_draw==2:
            result="You win"
      else:
            result="Draw"
    else:
      "..."
    print(f"Result: {result}")
    exit_game=input("Play again? ")
    if exit_game=="N" or exit_game=="n" or exit_game=="No" or exit_game=="no":
        break
