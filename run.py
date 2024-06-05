import os
import PIL
from PIL import Image

while True:
    folder_path = input('輸入資料夾路徑: ')

    if not os.path.exists(folder_path):
        print('請輸入有效路徑。')
    else:
        break

index = 1
total = len(os.listdir(folder_path))

for image in os.listdir(folder_path):
    try:
        print(f'({index} / {total}) ', end='')

        image_path = os.path.join(folder_path, image)
        if not os.path.isfile(image_path): raise TypeError

        basename, ext = os.path.splitext(image)

        if not ext.lower().endswith('.webp'): raise NameError
        im = Image.open(image_path).convert('RGBA')
        im.save(os.path.join(folder_path, f'{basename}.png'), 'png')

        os.remove(image_path)

        print(f'成功更改 {image_path}。')
    except NameError:
        print(f'{image_path} 並非 .webp 檔案。')
    except TypeError:
        print(f'{image_path} 並非一個檔案。')
    except PIL.UnidentifiedImageError:
        print(f'{image_path} 並非一張圖片。')
    except Exception as e:
        print(f'未知錯誤 - ({e})')

    index += 1