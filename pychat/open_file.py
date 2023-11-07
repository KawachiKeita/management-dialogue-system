import subprocess as sp
from datetime import datetime as dt
import pandas as pd
import time

file_name = "test.txt"
f = open(file_name, "w", encoding='utf8')  # ファイルを作成
now = dt.now()
# opneWave()

df = pd.read_csv("record.csv")

print("今出ている課題です")  # 情報セキュリティ、データベース論、実践研究セミナー、メディア系演習Ⅱ


file_name = "kadai.txt"
f = open(file_name, "w", encoding='utf8')  # ファイルを作成
f.write("更新日時 " + str(now) + "\n\n")
for i in range(len(df)):
    kigen = dt.fromisoformat(str(df['kigen'][i]))
    f.write(df['kadai'][i] + " " +
            str((kigen - now).days + 1) + "日後 \n")

# time.sleep(5)

memo = sp.Popen([r"C:\Windows\\notepad.exe",
                 r"C:\Users\Owner\OneDrive\OneDrive - 名古屋工業大学\デスクトップ\3年後期\メディア系演習Ⅱ\kadai.txt"])

# time.sleep(3)
# memo.kill()
