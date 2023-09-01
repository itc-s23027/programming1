import random

your_initial = input("あなたの名前の頭文字を入力してください: ").upper()

while True:
    random_letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    print(random_letter)
    
    if random_letter == your_initial:
        print(f"{your_initial}が表示されたので終了します。")
        break

