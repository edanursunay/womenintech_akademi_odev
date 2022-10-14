import random
player_score = computer_score = 0
computer_choice = 0

def print_result(winner = "Bilgisayar"):
    print(f"Bilgisayarın Seçimi: {computer_choice}\n\nKazanan: {winner}")
    global player_score, computer_score
    if winner == "Bilgisayar":
        computer_score += 100
    else:
        player_score += 100

print("Taş Kağıt Makas Oyununa Hoş geldiniz!\n" + "-"*37)

while True:
    print("\n1 - Taş\n2 - Kağıt \n3 - Makas\nOyundan çıkmak isterseniz bu değerler dışında bir değer giriniz")
    player_choice = int(input("Seçiminizi yapınız"))
    computer_choice = random.choice([1, 2, 3])

    if player_choice == computer_choice:
        print("Beraber, yeniden oynayınız")
    elif player_choice == 1:
        if computer_choice == 2:
            print_result()
        elif computer_choice == 3:
            print_result("Kullanıcı")
    elif player_choice == 2:
        if computer_choice == 1:
            print_result("Kullanıcı")
        elif computer_choice == 3:
            print_result()
    elif player_choice == 3:
        if computer_choice == 1:
            print_result()
        elif computer_choice == 2:
            print_result("Kullanıcı")     
    else:
        break

print(f"\n\nKullanıcı skoru {player_score} - Bilgisayarın skoru {computer_score}")
if player_score > computer_score: print("Kazanan Kullanıcı")
elif player_score < computer_score: print("Kazanan Bilgisayar")
else: print("Oyun Berabere")