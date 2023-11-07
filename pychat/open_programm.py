import subprocess as sp
import time
import pyautogui
import speech_recognition as sr
import wave
import pyaudio

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


r = sr.Recognizer()
mic = sr.Microphone()


# アプリケーションを開く
memo = sp.Popen([r"C:\Windows\\notepad.exe",
                 r"C:\Users\Owner\OneDrive\OneDrive - 名古屋工業大学\デスクトップ\3年後期\メディア系演習Ⅱ\record.csv"])
time.sleep(2)

memo.kill()


while True:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 雑音対策
        audio = r.listen(source)

    print("Now to recognize it...")

    try:
        s = r.recognize_google(audio, language='ja-JP')
        print(s)
        if s == "こんにちは":
            pyautogui.press('1')

        # "ストップ" と言ったら音声認識を止める
        elif s == "さよなら":
            print("おつかれさまでした。")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
