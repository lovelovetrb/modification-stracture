import CaboCha


def get_word(tree, chunk):
    surface = ""
    for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
        token = tree.token(i)
        features = token.feature.split(",")
        surface += token.surface
        # if features[0] == "名詞":
        #     surface += token.surface
        # elif features[0] == "形容詞":
        #     surface += features[6]
        #     break
        # elif features[0] == "動詞":
        #     surface += features[6]
        #     break
    return surface


def get_2_words(line):
    cp = CaboCha.Parser("-f1")
    print(cp.parseToString(line))
    tree = cp.parse(line)
    chunk_dic = {}
    chunk_id = 0
    chunk_length = 0
    replace_text = ""

    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_dic[chunk_id] = token.chunk
            chunk_id += 1
            chunk_length = chunk_id

    index = 0
    while True:
        # print(f"{index} {chunk_length}")
        if index >= chunk_length:
            break
        now_word = get_word(tree, chunk_dic[index])
        # @param link: Link to another chunk (係り先文節インデックス番号)
        if chunk_dic[index].link != -1:
            # どの程度係りに距離があるかを表す数値
            distance = chunk_dic[index].link - index
            # KNPによって係り受けが2つの文節以上に跨って発生しているところを抽出
            # 跨っている文節内の係り受けが1でなくなったところの直後に係り受けもとの文節を挿入する
            if distance >= 1:
                insert_text = chunk_dic[index]
                # DEBUG
                # print("insert_text: " + get_word(tree, insert_text))
                for i in range(index + 1, chunk_dic[index].link):
                    nextchunk = chunk_dic[i]
                    renextchunk = ""
                    if not i + 1 == chunk_length - 1:
                        replace_text += get_word(tree, nextchunk)
                        # DEBUG
                        # print("nextchunk: " + get_word(tree, nextchunk))
                    else:
                        replace_text += get_word(tree, chunk_dic[i])
                        replace_text += get_word(tree, insert_text)
                        index = index + distance - 1

            else:
                replace_text += now_word

        else:
            replace_text += now_word
        index += 1
    return replace_text


if __name__ == "__main__":
    # input.txtからテキストを1行ずつ読み込む
    with open("texts/input_after_clean.txt", mode="r") as f:
        lines = f.readlines()
    texts = []
    not_use_texts = []
    for line in lines:
        line = line.replace("\n", "")
        print(line)
        # 係り受け解析
        replace_text = get_2_words(line)
        if len(line) == len(replace_text):
            texts.append(line)
            texts.append(replace_text)
        else:
            not_use_texts.append(line)

    #  textsをファイルに出力
    with open("texts/output.txt", mode="w") as f:
        for text in texts:
            f.write(text + "\n")

    #  not_use_textsをファイルに出力
    with open("texts/not_use_output.txt", mode="w") as f:
        for text in not_use_texts:
            f.write(text + "\n")
