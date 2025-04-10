"""
python ./icon_android.py ./aaa.{png, jpg, svg, ...}

=>

- mipmap-hdpi
    - ic_launcher_foreground.png : (162 x 162)
    - ic_launcher_round.png : (49 x 49)
    - ic_launcher.png : (49 x 49)
- mipmap-mdpi
    - ic_launcher_foreground.png : (108 x 108)
    - ic_launcher_round.png : (48 x 48)
    - ic_launcher.png : (48 x 48)
- mipmap-xhdpi
    - ic_launcher_foreground.png : (216 x 216)
    - ic_launcher_round.png : (96 x 96)
    - ic_launcher.png : (96 x 96)
- mipmap-xxhdpi
    - ic_launcher_foreground.png : (324 x 324)
    - ic_launcher_round.png : (144 x 144)
    - ic_launcher.png : (144 x 144)
- mipmap-xxxhdpi
    - ic_launcher_foreground.png : (432 x 432)
    - ic_launcher_round.png : (192 x 192)
    - ic_launcher.png : (192 x 192)

and {img name}.zip
"""

"""
{
    "mipmap-hdpi": {
        "ic_launcher_foreground.png": (162, 162),
        "ic_launcher_round.png": (49, 49),
        "ic_launcher.png": (49, 49)
    },
    "mipmap-mdpi": {
        "ic_launcher_foreground.png": (108, 108),
        "ic_launcher_round.png": (48, 48),
        "ic_launcher.png": (48, 48)
    },
    "mipmap-xhdpi": {
        "ic_launcher_foreground.png": (216, 216),
        "ic_launcher_round.png": (96, 96),
        "ic_launcher.png": (96, 96)
    },
    "mipmap-xxhdpi": {
        "ic_launcher_foreground.png": (324, 324),
        "ic_launcher_round.png": (144, 144),
        "ic_launcher.png": (144, 144)
    },
    "mipmap-xxxhdpi": {
        "ic_launcher_foreground.png": (432, 432),
        "ic_launcher_round.png": (192, 192),
        "ic_launcher.png": (192, 192)
    }
}
"""
import os
import cairosvg
from pathlib import Path
from PIL import Image
import zipfile
resolutions = {
    "mipmap-hdpi": {
        "ic_launcher_foreground.png": (162, 162),
        "ic_launcher_round.png": (49, 49),
        "ic_launcher.png": (49, 49)
    },
    "mipmap-mdpi": {
        "ic_launcher_foreground.png": (108, 108),
        "ic_launcher_round.png": (48, 48),
        "ic_launcher.png": (48, 48)
    },
    "mipmap-xhdpi": {
        "ic_launcher_foreground.png": (216, 216),
        "ic_launcher_round.png": (96, 96),
        "ic_launcher.png": (96, 96)
    },
    "mipmap-xxhdpi": {
        "ic_launcher_foreground.png": (324, 324),
        "ic_launcher_round.png": (144, 144),
        "ic_launcher.png": (144, 144)
    },
    "mipmap-xxxhdpi": {
        "ic_launcher_foreground.png": (432, 432),
        "ic_launcher_round.png": (192, 192),
        "ic_launcher.png": (192, 192)
    }
}

def generate_images(input_image_path, output_dir):
    # 定义不同分辨率
    
    
    # 检查文件类型
    if input_image_path.lower().endswith('.svg'):
        # 将SVG转换为PNG
        png_path = os.path.splitext(input_image_path)[0] + '.png'
        cairosvg.svg2png(url=input_image_path, write_to=png_path)
        input_image_path = png_path
    
    # 打开输入图片
    with Image.open(input_image_path) as img:
        for folder_name, file_sizes in resolutions.items():
            # 创建文件夹
            folder_path = os.path.join(output_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            for file_name, size in file_sizes.items():
                # 生成不同分辨率的图片
                resized_img = img.resize(size, Image.LANCZOS)
                
                # 保存图片到文件夹
                resized_img.save(os.path.join(folder_path, file_name))

def create_zip(output_dir: str, zip_name: Path):
    # 创建压缩包
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(output_dir):
            rel_root = os.path.relpath(root, output_dir)
            # 只打包 mipmap-* 文件夹中的文件
            if rel_root not in resolutions:
                continue
            for file in files:
                file_path = os.path.join(root, file)
                # 避免打包压缩包自身
                if Path(file_path).resolve() == zip_name.resolve():
                    continue
                arcname = os.path.relpath(file_path, output_dir)
                zipf.write(file_path, arcname)

def create_icon(input_file: str, output_dir: str, is_zip: bool) -> None:
    generate_images(input_file, output_dir)
    if is_zip:
        output_dir_path = Path(output_dir)
        output_dir_zip_path = output_dir_path / "zip_a"
        create_zip(output_dir, output_dir_zip_path.with_suffix(".zip"))
