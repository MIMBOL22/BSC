import random
import hashlib


def get_words(words_file="words.txt"):
    with open(
        words_file
    ) as file:  # StackOverFlow - если 2 дебила это сила, то миллион дебилов, это ...
        return file.readlines()


def generate_table(vocab, seed):
    was = set()
    temp_table = []
    max_len = 0
    for i in range(16):
        temp_table.append([])
        for _ in range(16):
            word = random.choice(vocab)[:-1]
            while word in was or word in seed:
                word = random.choice(vocab)[:-1]
            was.add(word)
            if len(word) > max_len:
                max_len = len(word)
            temp_table[i].append(word)
    return temp_table, max_len


def hide_seed(temp_table, seed_arr, pass_hash_arr):
    for index, seed_word in enumerate(seed_arr):
        i, j = pass_hash_arr[index]
        temp_table[i][j] = seed_word
    return temp_table


def pretty_line(index, row, max_len):
    line = f'{hex(index)[2:].upper()}|{"|".join([w.ljust(max_len) for w in row])}'
    return f'{line}|\n |{"-"*(len(line)-2)}|'


def pretty_print(temp_table, max_len):
    print(" ", *[hex(i)[2:].ljust(max_len).upper() for i in range(16)], sep="|")
    print("_" *((16 * (max_len+1))+ 1))
    for index, row in enumerate(temp_table):
        print(pretty_line(index, row, max_len))


def main():
    seed = "mule zone tired worth peace census drastic squeeze setup trend man city "
    seed_arr = seed.replace(".", "").split()
    password = b"123456789"
    pass_hash = hashlib.md5(password).hexdigest()
    pass_hash_arr = [
        (int(pass_hash[i], 16), int(pass_hash[i + 1], 16))
        for i in range(0, len(pass_hash), 2)
    ]

    words = get_words()
    temp_table, max_len = generate_table(words, seed_arr)
    seed_max_len = max(list(map(len, seed_arr)))
    max_len = seed_max_len if seed_max_len > max_len else max_len
    temp_table = hide_seed(temp_table, seed_arr, pass_hash_arr)
    pretty_print(temp_table, max_len)

    print(
        "\n |--------------------------------------------------------------------------------------------|\n |    Pin:",
        str(password),
        "\n |--------------------------------------------------------------------------------------------|\n |    Seed:",
        seed,
        "\n |--------------------------------------------------------------------------------------------|\n |    Hash:",
        pass_hash,
        "\n |--------------------------------------------------------------------------------------------|",
    )


if __name__ == "__main__":
    main()
