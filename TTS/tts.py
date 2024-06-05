from gtts import gTTS
import tensorflow as tf

text = "안녕하세요. 파이썬과 40개의 작품들 입니다. 저는 장세민이고 실험용 예제문제입니다. 10초이상 말해야하니 과하게 하겠습니다."

tts = gTTS(text=text, lang='ko')
tts.save("./hi.mp3")

import winsound

# 재생할 음성 파일 경로
file_path = "./hi.mp3"

def play_sound(file_path):
    # winsound.PlaySound 함수를 사용하여 음성 파일을 스피커로 출력합니다.
    winsound.PlaySound(file_path, winsound.SND_FILENAME)

# 음성 파일 재생 함수 호출
play_sound(file_path)
