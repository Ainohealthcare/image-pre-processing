import os
import shutil
from PIL import Image

def convert_and_move_images_to_jpg(input_folder, output_folder):
    # output 폴더가 없다면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 폴더 내의 모든 파일 및 하위 폴더를 순회
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):  # PNG 파일인 경우
            # 파일 경로 완성
            file_path = os.path.join(input_folder, filename)
            # 이미지 파일 열기
            img = Image.open(file_path)
            # RGB 모드로 변환 (알파 채널 제거)
            rgb_img = img.convert('RGB')
            # 저장할 새 파일명 (JPG 확장자 사용)
            new_file_path = os.path.join(output_folder, filename[:-4] + '.jpg')
            # 이미지 저장
            rgb_img.save(new_file_path, "JPEG")
            print(f"Converted and moved {filename} to {new_file_path}")

# 사용 예:
convert_and_move_images_to_jpg("input", "output")
