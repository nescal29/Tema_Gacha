import subprocess
import random

def gacha() -> str:
    tema_num: int = 0

    # ファイルに書かれているテーマの数を取得
    with open('./tema_list.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()

            if not len(line):
                break
            else:
                tema_num += 1

    # print(tema_num)

    # 乱数の生成
    tema_rnd: int = random.randint(1, tema_num)
    # print(tema_rnd)

    # ファイルからテーマを取得
    with open('./tema_list.txt', encoding='utf-8') as f:
        for i in range(tema_rnd):
            tema: str = f.readline()

    # print(tema.rstrip('\n'))
    return tema.rstrip('\n')


if __name__ == '__main__':
    gacha()
