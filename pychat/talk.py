import os
import datetime
import pandas as pd

now = datetime.datetime.now()
print(now)


def writeTxt(file_name, myCheck):
    if not myCheck:   # notを付与することで、Falseの場合に実行（真(True)でない）
        with open(file_name, "w") as f:   # ファイルを作成
            f.write("\"kadai\",\"kigen\"")


def main():
    print("あ、どうもどうも")  # システム開始の合図
    # 検索ファイルがあればTrueを返し、なければFalseを返す（ブール型boolと呼ぶ）。
    myCheck = os.path.isfile(file_path)
    writeTxt(file_name, myCheck)  # witeTxt関数へ、変数を引数に渡して実行
    df = pd.read_csv(file_name)

    while True:
        s = input("me:")

        if s == "課題が出た":
            print("なんの課題が出たか教えてもらってもいいですか")
            kadai = input("課題名を入力:")
            print("それっていつまでですか")
            print("期限を入力")
            year = input("西暦:")
            month = input("月:")
            day = input("日:")
            kigen = "{}/{}/{}".format(year, month, day)
            df = df.append({'kadai': kadai, 'kigen': kigen},
                           ignore_index=True)  # 追加
            print(df)
            df.to_csv('record.csv', index=False)
            print("了解です、頑張ってください。")
        elif s == "課題が終わった":
            kadai_fin = input("どの課題が終わったんですか。\nme:")
            print("おつかれさまです。")
            drop_index = df.index[df['kadai'] == kadai_fin]  # 削除
            df = df.drop(drop_index)
            print(df)
            df.to_csv('record.csv', index=False)

        elif s == "課題一覧見せて":
            print("はいはい、分かりました。")
            print(df)
        elif s == "さよなら":
            print("それでは、おつかれさまでした。")
            break
        else:
            print("すいません、もう一回言ってもらっていいですか。")


if __name__ == '__main__':
    ### parameter ###
    current_path = os.getcwd()                        # パス設定（カレントディレクトリ）
    file_name = 'record.csv'                             # 検索ファイル名を設定
    file_path = os.path.join(current_path, file_name)  # パスとファイル名を結合
    print(file_path)

    ### call function ###
    main()
