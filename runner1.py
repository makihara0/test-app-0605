import random

# ダミーの実在しそうな女性の名前リスト（姓＋名）
names = [
    "佐藤 美咲", "鈴木 彩花", "高橋 美優", "田中 さくら", "伊藤 愛", "渡辺 美穂", "山本 由紀", "中村 美月", "小林 優奈", "加藤 美咲",
    "吉田 彩乃", "山田 美和", "佐々木 里奈", "山口 美沙", "松本 亜美", "井上 美咲", "木村 友香", "林 美月", "斎藤 彩花", "清水 美穂",
    "山崎 美優", "森 由紀", "池田 美沙", "橋本 亜美", "阿部 美咲", "石川 友香", "山下 美和", "中島 美月", "小川 優奈", "前田 美穂",
    "藤田 彩乃", "後藤 里奈", "岡田 美沙", "長谷川 亜美", "村上 美咲", "近藤 友香", "石井 美月", "遠藤 彩花", "青木 美優", "坂本 美和",
    "福田 由紀", "太田 美沙", "三浦 亜美", "藤井 美咲", "西村 友香", "藤原 美月", "松田 彩花", "岡本 美優", "中野 美穂", "原田 美和"
]

# タイムをランダム生成（9.56～12.99）
runners = []
for name in names:
    time = round(random.uniform(9.56, 12.99), 2)
    runners.append({"name": name, "time": time})

# タイムが良い順（昇順）に並び替え
runners_sorted = sorted(runners, key=lambda x: x["time"])

# 結果を表示
for i, runner in enumerate(runners_sorted, 1):
    print(f"{i:2d}位: {runner['name']} - {runner['time']}秒")