"""
┌-----------------------------------┐
| name                  | size      |
|-----------------------|-----------|
| 32x32.png             | 32 * 32   |
| 128x128.png           | 128 * 128 |
| 128x128@2.png         | 256 * 256 |
| icon.icns             | 512 * 512 |
| icon.ico              | 16 * 16   |
| icon.png              | 512 * 512 |
| Square30x30Logo.png   | 30 * 30   |
| Square44x44Logo.png   | 44 * 44   |
| Square71x71Logo.png   | 71 * 71   |
| Square89x89Logo.png   | 89 * 89   |
| Square107x107Logo.png | 107 * 107 |
| Square142x142Logo.png | 142 * 142 |
| Square150x150Logo.png | 150 * 150 |
| Square284x284Logo.png | 284 * 284 |
| Square310x310Logo.png | 310 * 310 |
| StoreLogo.png         | 50 * 20   |
└-----------------------------------┘

Quality is paramount
./get_icon.py name.{png, jpg, svg}... => {32x32.png...}.zip
"""

import sys
import zipfile
from pathlib import Path
from PIL import Image
import cairosvg

def convert_svg_to_png(svg_path: str, png_path: str, scale: float = 1.0) -> None:
    """Convert SVG to PNG using CairoSVG."""
    cairosvg.svg2png(url=svg_path, write_to=png_path, scale=scale)

def resize_and_export(
    image: Image.Image, 
    sizes: dict[str, tuple[int, int]], 
    output_dir: Path
) -> None:
    """Resize image to different sizes and save."""
    for filename, (width, height) in sizes.items():
        resized_img = image.resize((width, height), Image.LANCZOS)
        output_path = output_dir / filename
        resized_img.save(output_path, "PNG")

def process_image(
    input_path: Path, 
    output_dir: Path, 
    output_zip: Path = None
) -> None:
    """Main function to generate icons."""
    input_path = Path(input_path)
    temp_png = None

    if input_path.suffix.lower() == ".svg":
        temp_png = input_path.with_suffix(".png")
        convert_svg_to_png(str(input_path), str(temp_png))
        input_path = temp_png

    image = Image.open(input_path).convert("RGBA")

    sizes = {
        "32x32.png": (32, 32),
        "128x128.png": (128, 128),
        "128x128@2.png": (256, 256),
        "icon.icns": (512, 512),
        "icon.png": (512, 512),
        "Square30x30Logo.png": (30, 30),
        "Square44x44Logo.png": (44, 44),
        "Square71x71Logo.png": (71, 71),
        "Square89x89Logo.png": (89, 89),
        "Square107x107Logo.png": (107, 107),
        "Square142x142Logo.png": (142, 142),
        "Square150x150Logo.png": (150, 150),
        "Square284x284Logo.png": (284, 284),
        "Square310x310Logo.png": (310, 310),
        "StoreLogo.png": (50, 50)
    }

    # 生成普通 PNG 图标
    resize_and_export(image, sizes, output_dir)

    # 生成多尺寸 ICO 图标
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    icon_path = output_dir / "icon.ico"
    icon_images = Image.open(output_dir / "icon.png")
    icon_images.save(icon_path, format="ICO", sizes=icon_sizes)

    # 压缩文件
    if not output_zip is None:
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in output_dir.iterdir():
                zipf.write(file, file.name)

        print(f"Icons saved to {output_zip}")

    if temp_png:
        temp_png.unlink()  # 删除临时 PNG 文件


def get_icon(input_file: str, output_dir: Path, is_zip: bool) -> None:

    output_zip = Path(output_dir).with_suffix(".zip") if is_zip else None
    process_image(input_file, output_dir, output_zip)

