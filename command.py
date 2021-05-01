from janome.tokenizer import Tokenizer

t = Tokenizer()

def anlys(discord_msg: str):
    
    # 単語分割
    for word in t.tokenize(discord_msg):
        # 単語の正規化
        return_str: str = normalization(str(word.surface))

        if return_str == '>temagacha':
            return 0


# 単語の正規化をする関数
def normalization(word: str):
    word = word.lower()
    return token


if __name__ == '__main__':
    anlys(dis_str)
