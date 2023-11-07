import wave
import pyautogui

filename = "gannbattekudasai"


def totaltime(file_name):
    wavf = file_name + '.wav'
    wr = wave.open(wavf, 'r')

    # waveファイルが持つ性質を取得

    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    return total_time


def lipsink(total_time):  # 口パク
    time = total_time / 4
    pyautogui.moveTo(960, 600)
    pyautogui.dragTo(1500, 600, time, button='left')
    pyautogui.dragTo(960, 600, time, button='left')
    pyautogui.dragTo(1500, 600, time, button='left')
    pyautogui.dragTo(960, 600, time, button='left')


lipsink(totaltime(filename))
