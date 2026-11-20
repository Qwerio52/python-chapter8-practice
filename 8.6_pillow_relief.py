# 8.6 图像浮雕效果 Pillow
from PIL import Image
import os

def relief(img_path, out_path="relief.jpg"):
    if not os.path.exists(img_path):
        print(f"❌ 找不到图片文件：{img_path}")
        return
    img = Image.open(img_path).convert("L")
    w, h = img.size
    new_img = Image.new("L", (w,h))
    p_old = img.load()
    p_new = new_img.load()

    for y in range(h):
        for x in range(w):
            if x == w-1 or y == h-1:
                p_new[x,y] = 128
            else:
                val = p_old[x,y] - p_old[x+1,y+1] + 128
                val = max(0, min(255, val))
                p_new[x,y] = val
    new_img.save(out_path)
    print(f"✅ 浮雕图已保存至 {out_path}")
    new_img.show()

if __name__ == "__main__":
    relief("test.jpg")