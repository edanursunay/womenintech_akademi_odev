from random import randint

def guess(number):
    user_number = int(input("Sayı tahmin oyunu için 1-100 arasında bir tahminde bulun"))
    while number != user_number:
        if number < user_number:
            print("üzgünüm, daha küçük bir tahminde bulunmalısınız.")
        else:
            print("Üzgünüm, daha büyük bir tahminde bulunmalısınız.")
        user_number = int(input("Lütfen, yeniden bir tahminde bulunun!"))
    else:
        print("Tebrikler, doğru tahmin!")

guess(randint(1, 100))