import random

# なぞなぞクイズのリスト（問題、選択肢、正解インデックス、難易度）
quizzes = [
    # かんたん
    {"question": "パンはパンでも食べられないパンは？", "choices": ["フライパン", "メロンパン", "あんパン"], "answer": 0, "level": "かんたん"},
    {"question": "学校で一番早く走る動物は？", "choices": ["うさぎ", "チーター", "校長先生"], "answer": 2, "level": "かんたん"},
    {"question": "さかさまにすると軽くなるものは？", "choices": ["いす", "かさ", "ふくろ"], "answer": 1, "level": "かんたん"},
    {"question": "いつも怒っている野菜は？", "choices": ["トマト", "ピーマン", "ナス"], "answer": 0, "level": "かんたん"},
    {"question": "お茶を飲むときに使う花は？", "choices": ["さくら", "きく", "はなび"], "answer": 1, "level": "かんたん"},
    {"question": "空を飛ぶパンは？", "choices": ["ジャムパン", "食パン", "カレーパン"], "answer": 1, "level": "かんたん"},
    {"question": "目が10個ある魚は？", "choices": ["めだか", "いわし", "さば"], "answer": 0, "level": "かんたん"},
    {"question": "いつもお腹がすいている虫は？", "choices": ["カマキリ", "アリ", "ハチ"], "answer": 0, "level": "かんたん"},
    {"question": "お金を洗うと何になる？", "choices": ["きれい", "まね", "せんたく"], "answer": 1, "level": "かんたん"},
    {"question": "足が3本ある動物は？", "choices": ["いぬ", "ねこ", "いません"], "answer": 2, "level": "かんたん"},
    # ふつう
    {"question": "白い犬が好きな飲み物は？", "choices": ["ミルク", "コーヒー", "お茶"], "answer": 0, "level": "ふつう"},
    {"question": "いつも笑っている魚は？", "choices": ["タイ", "サバ", "イワシ"], "answer": 0, "level": "ふつう"},
    {"question": "お城の中にいる虫は？", "choices": ["アリ", "ハチ", "シロアリ"], "answer": 2, "level": "ふつう"},
    {"question": "おじいさんが好きな花は？", "choices": ["さくら", "ひまわり", "じいじ"], "answer": 2, "level": "ふつう"},
    {"question": "いつも走っている野菜は？", "choices": ["にんじん", "だいこん", "きゅうり"], "answer": 2, "level": "ふつう"},
    {"question": "お風呂に入るときに使う星は？", "choices": ["すいせい", "きんせい", "バスタブ"], "answer": 2, "level": "ふつう"},
    {"question": "お金を食べる虫は？", "choices": ["カネムシ", "カミキリムシ", "カネゴン"], "answer": 2, "level": "ふつう"},
    {"question": "いつも眠そうな鳥は？", "choices": ["ふくろう", "すずめ", "ひよこ"], "answer": 0, "level": "ふつう"},
    {"question": "お腹がすいている時に食べる花は？", "choices": ["さくら", "ひまわり", "はなまる"], "answer": 2, "level": "ふつう"},
    {"question": "いつも怒っている魚は？", "choices": ["タイ", "サバ", "イワシ"], "answer": 1, "level": "ふつう"},
    # むずかしい
    {"question": "世界で一番重いパンは？", "choices": ["フランスパン", "鉄パン", "食パン"], "answer": 1, "level": "むずかしい"},
    {"question": "逆立ちすると見えなくなるものは？", "choices": ["空", "地面", "自分"], "answer": 2, "level": "むずかしい"},
    {"question": "いつも逆さまにいる動物は？", "choices": ["コウモリ", "サル", "カエル"], "answer": 0, "level": "むずかしい"},
    {"question": "お金を持っている虫は？", "choices": ["カネムシ", "カミキリムシ", "カネゴン"], "answer": 0, "level": "むずかしい"},
    {"question": "いつも泣いている野菜は？", "choices": ["たまねぎ", "にんじん", "だいこん"], "answer": 0, "level": "むずかしい"},
    {"question": "お風呂に入るときに使う魚は？", "choices": ["サバ", "タイ", "バスタイ"], "answer": 2, "level": "むずかしい"},
    {"question": "いつも冷たい魚は？", "choices": ["サバ", "イワシ", "ヒラメ"], "answer": 0, "level": "むずかしい"},
    {"question": "お金を洗うと何になる？", "choices": ["まね", "きれい", "せんたく"], "answer": 0, "level": "むずかしい"},
    {"question": "いつも眠そうな動物は？", "choices": ["ナマケモノ", "ライオン", "ゾウ"], "answer": 0, "level": "むずかしい"},
    {"question": "逆立ちすると軽くなるものは？", "choices": ["いす", "かさ", "ふくろ"], "answer": 1, "level": "むずかしい"},
]

def get_rank(score):
    if score >= 27:
        return "Sランク"
    elif score >= 24:
        return "Aランク"
    elif score >= 18:
        return "Bランク"
    elif score >= 12:
        return "Cランク"
    else:
        return "Dランク"

def main():
    print("なぞなぞクイズ30問！3択から選んでね。\n")
    random.shuffle(quizzes)
    score = 0
    for idx, quiz in enumerate(quizzes[:30], 1):
        print(f"第{idx}問（難易度：{quiz['level']}）")
        print(quiz["question"])
        for i, choice in enumerate(quiz["choices"], 1):
            print(f"  {i}. {choice}")
        try:
            ans = int(input("答え（1-3）: "))
        except:
            ans = 0
        if ans - 1 == quiz["answer"]:
            print("正解！\n")
            score += 1
        else:
            print(f"不正解！正解は「{quiz['choices'][quiz['answer']]}」\n")
    print(f"あなたの正解数は {score}/30 です。ランク：{get_rank(score)}")

if __name__ == "__main__":
    main()