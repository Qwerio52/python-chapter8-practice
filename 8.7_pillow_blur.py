# 8.7 图像模糊效果 Pillow
from PIL import Image, ImageFilter
import os

def blur(img_path, out_path="blur.jpg"):
    if not os.path.exists(img_path):
        print(f"❌ 找不到图片文件：{img_path}")
        return
    img = Image.open(img_path)
    blur_img = img.filter(ImageFilter.BLUR)
    blur_img.save(out_path)
    print(f"✅ 模糊图已保存至 {out_path}")
    blur_img.show()

if __name__ == "__main__":
    blur("test.jpg")