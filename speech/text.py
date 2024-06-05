from gtts import gTTS
import tensorflow as tf

tf.compat.v1.disable_v2_behavior()

text = "안녕하세요. 파이썬과 40개의 작품들 입니다. 저는 장세민이고 실험용 예제문제입니다. 10초이상 말해야하니 과하게 하겠습니다."

tts = gTTS(text=text, lang='ko')
tts.save("./hi.mp3")
