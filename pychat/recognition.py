import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


while True:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source)  # 雑音対策
        audio = r.listen(source)

    print("Now to recognize it...")

    try:
        s = r.recognize_google(audio, language='ja-JP')
        print(s)

        # "ストップ" と言ったら音声認識を止める
        if s == "さよなら":
            print("おつかれさまでした。")
            break

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
