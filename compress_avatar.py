from PIL import Image

# 打开图片
img = Image.open('image/tuanzi.jpg')

# 获取原始大小
original_size = img.size
print(f"原始尺寸: {original_size[0]} x {original_size[1]}")

# 裁剪为正方形（从中心裁剪）
width, height = img.size
if width > height:
    # 横图，裁剪左右
    left = (width - height) // 2
    right = left + height
    img = img.crop((left, 0, right, height))
else:
    # 竖图，裁剪上下
    top = (height - width) // 2
    bottom = top + width
    img = img.crop((0, top, width, bottom))

print(f"裁剪后尺寸: {img.size[0]} x {img.size[1]}")

# 调整大小为200x200
img = img.resize((200, 200), Image.Resampling.LANCZOS)

# 保存压缩
img.save('image/tuanzi_avatar.jpg', 'JPEG', quality=80, optimize=True)

print("✓ 团子头像已压缩并裁剪为正方形 200x200")
