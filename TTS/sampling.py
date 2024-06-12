import os
from pydub import AudioSegment

# 디렉토리 설정
input_dir = 'sample'
output_dir = 'test'

# output_dir이 없다면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# sample 폴더의 파일 목록 출력 (디버깅용)
file_list = os.listdir(input_dir)
print(file_list)

# mp3 파일들을 순회하며 wav로 변환
for filename in file_list:
    if filename.endswith('.mp3'):
        mp3_path = os.path.join(input_dir, filename)
        wav_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.wav")

        # 파일이 존재하는지 확인
        if not os.path.isfile(mp3_path):
            print(f"File not found: {mp3_path}")
            continue

        # 파일이 존재하는지 다시 확인
        with open(mp3_path, 'rb') as f:
            f.read()

        # mp3 파일을 로드하여 wav로 변환 및 저장
        audio = AudioSegment.from_mp3(mp3_path)
        audio.export(wav_path, format="wav", parameters=["-ar", "44100", "-ac", "1", "-sample_fmt", "s16"])
        print(f"Converted {mp3_path} to {wav_path}")
