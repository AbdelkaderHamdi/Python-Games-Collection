import random
counter= 0
while counter<3: 
    user_choice= input("choose one (rock✊ , paper✋ , scissors✌️ ): ").strip()
    
    emojis = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️' }    

    machine_choice= random.choice(list(emojis.keys()))

    print(f"Bot chose: {machine_choice}{emojis[machine_choice]}")

    if user_choice == machine_choice:
      print("Draw! It's a tie.\n")
      
    elif (user_choice == 'rock' and machine_choice == 'scissors') or \
        (user_choice == 'paper' and machine_choice == 'rock') or \
        (user_choice == 'scissors' and machine_choice == 'paper'):
      print("You won!🤩\n")
      counter+=1

    else:
      print("Bot won!😞\n")
      counter+=1

