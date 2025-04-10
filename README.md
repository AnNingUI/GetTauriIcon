> 使用模板: [PPX](https://github.com/pangao1990/ppx)
>

## 如何运行或者打包源码
初始化与打包看[这里](https://github.com/pangao1990/PPX/blob/main/README.md)

## 如何使用
1. 打包安卓系列icon
   - 第一栏中选择要修改的目标图片(ep: 除了普通图像文件外还支持.svg)
   - 第二栏中选择要输出的目标文件夹
   - 在系统类型中选择 `安卓`
   - 在生成后打开目标文件夹找到 `mipmap-*dpi` *表示相对应的dpi
   - 将一系列图标覆盖到 `tauri项目根目录\src-tauri\gen\android\app\src\main\res` 下即可完成
2. 打包电脑(win, linux, macos)系列icon
   - 第一栏中选择要修改的目标图片(ep: 除了普通图像文件外还支持.svg)
   - 第二栏中选择要输出的目标文件夹
   - 在系统类型中选择 `电脑`
   - 在生成后打开目标文件夹找到 `icons` 文件夹
   - 将 `icons` 文件夹移动覆盖到 `tauri项目根目录\src-tauri` 下即可完成

另外是否获取压缩包是可选项

## 作者将要去做的事
- [] 因为作者没有macos系统，所以暂时无法编写输出ios图像格式的脚本，如果有人可以提供脚本，请提交PR