from curses import termattrs
import os
from datetime import datetime as dt
import pandas as pd
import speech_recognition as sr
import wave
import pyaudio
import subprocess as sp
import time
import pyautogui
import threading as th
import re

#パスの設定
sp.Popen([r"CubismViewer5.exeのパス",
          r"influencer.moc3のパス"])
time.sleep(15)

# 開きたいWavファイルを引数


def openWave(name):
    # 開きたいファイルをここに
    wf = wave.open(name, "r")

    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # チャンク単位でストリームに出力し音声を再生
    chunk = 1024
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()


# openWave("0_otama.wav")


def writeTxt(file_name, myCheck):
    if not myCheck:   # notを付与することで、Falseの場合に実行（真(True)でない）
        with open(file_name, "w") as f:   # ファイルを作成
            f.write("\"kadai\",\"kigen\"")
    # else:   出されている課題名と期限までの残り日数を表示


def audioData():
    r = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        with mic as source:
            r.adjust_for_ambient_noise(source)  # 雑音対策
            audio = r.listen(source)

        try:
            audio_text_data = r.recognize_google(audio, language='ja-JP')
            print(audio_text_data)
            break
        except sr.UnknownValueError:
            print("もう一回言ってもらっていいですか。")
            # openWave()
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

    return audio_text_data


def lipsink():  # 口パク
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(1500, 600, 0.4, button='left')
    pyautogui.dragTo(960, 600, 0.4, button='left')
    pyautogui.dragTo(1500, 600, 0.4, button='left')
    pyautogui.dragTo(960, 600, 0.4, button='left')


def nod():  # うなづく
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(960, 650, 0.2, button='left')
    pyautogui.moveTo(960, 600, 0.1)
    pyautogui.dragTo(960, 650, 0.2, button='left')
    pyautogui.moveTo(960, 600, 0.1)


def bow():  # お辞儀
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(1500, 900, 0.8, button='left')


def totaltime(file_name):
    wavf = file_name + '.wav'
    wr = wave.open(wavf, 'r')

    # waveファイルが持つ性質を取得

    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    return total_time

# 並列処理のため関数を定義


def speak(voice, motion):
    voice_th = th.Thread(target=voice)
    motion_th = th.Thread(target=motion)
    voice_th.start()
    motion_th.start()
    time.sleep(3)


def kadai():
    now = dt.now()
    df = pd.read_csv("record.csv")

    file_name_kadai = "kadai.txt"
    f = open(file_name_kadai, "w", encoding='utf8')  # ファイルを作成
    f.write("現在時刻 " + str(now) + "\n\n")
    for i in range(len(df)):
        kigen = dt.fromisoformat(str(df['kigen'][i]))
        f.write(df['kadai'][i] + " " + str((kigen - now).days + 1) + "日後 \n")


def setteing():
    pyautogui.moveTo(175, 38, 0.5)  # アニメーション
    pyautogui.click()
    pyautogui.moveTo(175, 280, 0.5)  # カーソル追従の設定を開く
    pyautogui.click()

    pyautogui.moveTo(1140, 460, 0.5)  # 目玉X
    pyautogui.click()
    pyautogui.moveTo(1140, 515, 0.5)  # マウス右Xに設定
    pyautogui.click()

    pyautogui.moveTo(1140, 477, 0.5)  # 目玉Y
    pyautogui.click()
    pyautogui.moveTo(1140, 542, 0.5)  # マウス右Y
    pyautogui.click()

    pyautogui.moveTo(1140, 558, 0.5)  # 口開閉
    pyautogui.click()
    pyautogui.moveTo(1140, 578, 0.5)  # マウス左
    pyautogui.click()

    pyautogui.moveTo(1140, 578, 0.5)  # 体の回転
    pyautogui.click()
    pyautogui.moveTo(1140, 640, 0.5)  # マウス右X
    pyautogui.click()

    pyautogui.moveTo(920, 820, 0.5)  # OK
    pyautogui.click()

    pyautogui.moveTo(960, 600)  # 中央に持ってく


def mouikkai():
    openWave("voice\example.wav")


def yorosiku():
    openWave("voice\yorosiku.wav")


def hazimemasite():
    openWave("voice\hazimemasite.wav")


def deteirukadai():
    openWave("voice\deteirukadai.wav")


def nannno():
    openWave("voice\220_otama.wav")


def soretteitumade():
    openWave("voice\soretteitumade.wav")


def nenngappi():
    openWave("voice\example.wav")


def ryoukai():
    openWave("voice\ryoukai.wav")


def hoka():
    openWave("voice\example.wav")


def dono():
    openWave("2voice\20_otama.wav")


def otsukaresamadesita():
    openWave("voice\otsukaresamadesita.wav")


# def ryoukaidesu():
#     openWave("220_otama.wav")


def gannbattekudasai():
    openWave("voice\gannbattekudasai.wav")


def suimasenn():
    openWave("voice\220_otama.wav")


def homeru():
    openWave("voice\homeru.wav")


def owarimasitaka():
    openWave("voice\owarimasitaka.wav")


def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    #setteing()
    #sp.call('PAUSE', shell=True)
    #time.sleep(3)

    print("けいたさん、はじめまして")  # システム開始の合図
    speak(yorosiku, bow)
    
    #パスの設定
    memo = sp.Popen([r"notepad.exeのパス",
                     r"kadai.txtのパス"])
    time.sleep(5)
    memo.kill()

    file_name = 'record.csv'                             # 検索ファイル名を設定
    file_path = os.path.join(current_path, file_name)  # パスとファイル名を結合
    print(file_path)
    # 検索ファイルがあればTrueを返し、なければFalseを返す（ブール型boolと呼ぶ）。
    myCheck = os.path.isfile(file_path)
    writeTxt(file_name, myCheck)  # witeTxt関数へ、変数を引数に渡して実行
    df = pd.read_csv(file_name)

    while True:

        print("Say something...")

        with mic as source:
            r.adjust_for_ambient_noise(source)  # 雑音対策
            audio = r.listen(source)

        print("Now to recognize it ...")
        nod()

        try:

            s = r.recognize_google(audio, language='ja-JP')
            print(s)
            if s == "こんにちは":
                print("けいたさん、はじめまして")
                speak(hazimemasite, bow)

            if s == "課題が出た":
                print("なんの課題が出たか教えてもらってもいいですか")
                speak(nannno, lipsink)

                kadai = audioData()

                print("それっていつまでですか")
                speak(soretteitumade, lipsink)

                print("----年--月--日")

                while True:
                    before_words = audioData()

                    target_words_1 = "年"
                    target_words_2 = "月"
                    target_words_3 = "日"

                    if target_words_1 in before_words:
                        if target_words_2 in before_words:
                            if target_words_3 in before_words:
                                after_words = re.search(
                                    '(.*)(年)(.*)(月)(.*)(日)', before_words)
                                break
                            else:
                                print("あ、年月日でお願いします。")
                                speak(nenngappi, lipsink)
                        else:
                            print("あ、年月日でお願いします。")
                            speak(nenngappi, lipsink)

                    else:
                        print("あ、年月日でお願いします。")
                        speak(nenngappi, lipsink)

                year = after_words.group(1)
                month = after_words.group(3)
                day = after_words.group(5)

                kigen = "{}-{:0>2}-{:0>2}".format(year, month, day)
                df = df.append({'kadai': kadai, 'kigen': kigen},
                               ignore_index=True)  # 追加
                print(df)
                df.to_csv('record.csv', index=False)
                print("了解です、頑張ってください。")
                speak(ryoukai, bow)

            elif s == "課題が終わった":
                print("どの課題が終わったんですか。\\me:")
                speak(owarimasitaka, lipsink)
                kadai_fin = audioData()
                print("おつかれさまです。")
                speak(homeru, lipsink)
                drop_index = df.index[df['kadai'] == kadai_fin]  # 削除

                df = df.drop(drop_index)
                print(df)
                df.to_csv('record.csv', index=False)

            elif s == "課題見せて":
                print("了解です")
                speak(ryoukai, lipsink)
                speak(deteirukadai, lipsink)
                #パスの設定
                memo = sp.Popen([r"notepad.exeのパス",
                                 r"record.csvのパス"])
                time.sleep(5)
                memo.kill()
                print(df)

            # "さよなら"と言ったら音声認識を止める
            elif s == "さよなら":
                print("けいたさん、頑張ってください。")
                # 音声再生と口パクを同時に実行するための並列処理
                speak(gannbattekudasai, bow)
                break
            else:
                print("すいません、もう一回言ってもらっていいですか。")
                speak(mouikkai, lipsink)

        except sr.UnknownValueError:
            print("すいません、もう一回言ってもらっていいですか。")
            speak(mouikkai, lipsink)
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

        print("他に何かありますか？")
        #speak(hoka, lipsink)


if __name__ == '__main__':
    ### parameter ###
    current_path = os.getcwd()                        # パス設定（カレントディレクトリ）

    ### call function ###
    kadai()
    main()
