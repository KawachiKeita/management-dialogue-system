import pyautogui
import threading as th

#display_size = pyautogui.size()
# print(display_size)
#Size(width=1920, height=1200)

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


def swim():
    openWave("swim.wav")


def lipsink():
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(1500, 600, 0.2, button='left')  # 開く
    pyautogui.dragTo(960, 600, 0.2, button='left')  # 閉じる
    pyautogui.dragTo(1500, 600, 0.2, button='left')
    pyautogui.dragTo(960, 600, 0.2, button='left')


def nod():
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(960, 650, 0.2, button='left')  # 首下
    pyautogui.moveTo(960, 600, 0.1)  # 首上
    pyautogui.dragTo(960, 650, 0.2, button='left')
    pyautogui.moveTo(960, 600, 0.1)


def bow():
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(1500, 900, 0.5, button='left')  # 口開けながらお辞儀


bowf = th.Thread(target=bow())
bowf.start()
voice = th.Thread(target=swim)
voice.start()


lipsink()
nod()
bow()
print(pyautogui.position())
