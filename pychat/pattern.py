import re


while True:
    before_words = input("期限はいつまで？")

    target_words = "年"
    if target_words in before_words:
        after_words = re.search('(.*)(年)(.*)(月)(.*)(日)', before_words)
        break
    else:
        print("----年--月--日で入力してください。")


# 抽出した文字列を表示する
print(after_words.group(1), after_words.group(3), after_words.group(5))
