#for lucky draw:
secret_number = [3,5,14,20,25,48]
guess_count = 0
guess_limit = 50
while guess_count <guess_limit:
    user_guess = int(input("Guess:"))
    guess_count = guess_count + 1 
    if user_guess in  secret_number:
        print(f"Congratulation your number is this..Lucky draw")
    else:
        print(f"Invalid Number! Unlucky ! Try next time")
    
    break