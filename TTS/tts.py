import os
import json
from gtts import gTTS

# 디렉토리 설정
input_dir = 'session2'
output_dir = 'sample'

# output_dir이 없다면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# JSON 파일들을 순회하며 utterance 키의 값을 추출하여 mp3로 저장
file_counter = 1
try:
    for filename in os.listdir(input_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            print(f"Processing file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for session in data.get("sessionInfo", []):
                    for entry in session.get("dialog", []):
                        utterance = entry.get("utterance", "")
                        if utterance:
                            try:
                                tts = gTTS(text=utterance, lang='ko')
                                output_path = os.path.join(output_dir, f'sample{file_counter}.mp3')
                                tts.save(output_path)
                                print(f'Saved {output_path}')
                                file_counter += 1
                            except Exception as e:
                                print(f"Error saving {output_path}: {e}")
except Exception as e:
    print(f"Error processing files: {e}")
