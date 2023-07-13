# not_use_output.txtを読み込む
with open("texts/not_use_output.txt", mode="r") as f:
    lines = f.readlines()

# input.txtにlinesの内容が存在するかどうかを確認
with open("texts/input.txt", mode="r") as f:
    input_lines = f.readlines()

# 重複している行を削除
for line in lines:
    if line in input_lines:
        input_lines.remove(line)
        print("remove: " + line)

# input.txtにlinesの内容を追加
with open("texts/input_after_clean.txt", mode="a") as f:
    for line in input_lines:
        f.write(line)
