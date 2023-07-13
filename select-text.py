import mlmt

pretrained_model_name = "cl-tohoku/bert-base-japanese-whole-word-masking"

scorer = mlmt.MLMScorer(pretrained_model_name, use_cuda=True)

# output.txtから文章を1行ずつ読み込み、結果を配列に格納
with open("output.txt", mode="r") as f:
    lines = f.readlines()

scores = scorer.score_sentences(lines)

print("input_sentence, score")
for sentence, score in zip(lines, scores):
    print(sentence, score)
