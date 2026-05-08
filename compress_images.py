from PIL import Image
import os

# 图片目录
image_dir = 'image'

# 获取所有jpg文件
jpg_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

print(f"找到 {len(jpg_files)} 张图片，开始压缩...")

for filename in jpg_files:
    filepath = os.path.join(image_dir, filename)
    
    try:
        # 打开图片
        img = Image.open(filepath)
        
        # 获取原始大小
        original_size = os.path.getsize(filepath) / 1024  # KB
        
        # 调整尺寸（如果太大）
        max_width = 1200
        if img.width > max_width:
            ratio = max_width / img.width
            new_height = int(img.height * ratio)
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        
        # 保存压缩后的图片（质量75%）
        img.save(filepath, 'JPEG', quality=75, optimize=True)
        
        # 获取压缩后大小
        new_size = os.path.getsize(filepath) / 1024  # KB
        
        print(f"✓ {filename}: {original_size:.1f}KB → {new_size:.1f}KB (减少 {(1 - new_size/original_size)*100:.1f}%)")
        
    except Exception as e:
        print(f"✗ {filename}: 压缩失败 - {e}")

print("\n压缩完成！")
