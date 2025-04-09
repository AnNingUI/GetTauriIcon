from enum import Enum

class IconOSType(Enum):
    Computer = 0
    Android  = 1
    IOS      = 2

class TauriIcon():
    """ 管理Tauri icon 的生成 """
    def tauri_icon_create_icon(self, os_type: int, input_file: str, output_dir: str, is_zip: bool):
        match os_type:
            case IconOSType.Computer.value:
                from .sendbox.tauri_icon.get_icon import create_icon
                create_icon(input_file, output_dir, is_zip)
            case IconOSType.Android.value:
                from .sendbox.tauri_icon.android.get_icon import create_icon
                create_icon(input_file, output_dir, is_zip)
            case IconOSType.IOS.value:
                pass
            case _:
                return "Error: 未知系统或后续可能计划支持"