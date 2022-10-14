import random

def computer_guess(x):
    start = 1
    end = 100
    result = ""
    while result != "d":
        guess = random.randint(start, end)

        result = input(f"{guess} değeri aklından tuttuğun değerden büyükse(b) küçükse (k), doğruysa (d) giriniz.").lower()
        if result == "b":
            end = guess - 1
        elif result == "k":
            start = guess + 1
    print("Tebrikler, doğru tahmin")
    
computer_guess(29)
Tebrikler, doğru tahmin