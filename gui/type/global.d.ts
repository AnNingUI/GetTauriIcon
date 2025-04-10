/**
 * @author AnNingUI
 */
// window 全局类型添加
declare interface Window {
  pywebview: PyWebView
}

declare type Cross<T extends any[]> = T extends [infer H, ...infer R] ? H & Cross<R> : {}

type PyWebViewApi = Cross<[_PyWebViewSystem, _PyWebViewStorage, _PyWebViewTauriIcon]>

interface PyWebView {
  api: PyWebViewApi
}

/**
Cross<[
  _PyWebViewSystem,
  _PyWebViewStorage
]>
==
_PyWebViewSystem & _PyWebViewStorage
 */
interface _CheckInfo {
  code: 0 | -1 | 1
  msg: string
  htmlUrl?: string
  assets?: string
  body?: string
}

interface FileInfo {
  filename: string
  ext: string
  dir: string
  path: string
}
interface _PyWebViewSystem {
  /**
   * 调用js中挂载到window的函数
   * @inpy api/system.py
   * @param func js中挂载的函数名
   * @param info 传递给js的参数
   * @returns
   */
  system_py2js: <T>(func: string, info: string) => Promise<T>
  /**
   * 程序基础配置信息 { 应用名称, 版本号 }
   * @inpy api/system.py
   * @returns
   */
  system_getAppInfo: () => Promise<{
    appName: string
    appVersion: string
  }>
  /**
   * 检查更新 0=>有新版本; -1=>联网失败; 1=>已经是最新版本
   * @inpy api/system.py
   * @returns
   */
  system_checkNewVersion: () => Promise<_CheckInfo>
  /**
   * 下载新版本 0=>下载程序包成功; -1=>联网失败; -2=>下载程序包失败; 1=>已经是最新版本
   * @inpy api/system.py
   * @returns
   */
  system_downloadNewVersion: () => Promise<
    | {
        code: 0 | -1 | -2 | 1
        msg: string
        downloadPath?: string
      }
    | _CheckInfo
  >
  /**
   * 取消下载新版本
   * @inpy api/system.py
   * @returns
   */
  system_cancelDownloadNewVersion: () => Promise<void>
  /**
   * 获取用户名称
   * @inpy api/system.py
   * @returns
   */
  system_getOwner: () => Promise<string>
  /**
   * 用电脑默认软件打开本地文件
   * @inpy api/system.py
   * @param path
   * @returns
   */
  system_pyOpenFile: (path: string) => Promise<void>
  /**
   * 文件选择对话框
   * @inpy api/system.py
   * @param fileTypes 文件类型 描述+后缀，例如["这是xxx文本类型,后缀在括号里面 (\*.py;\*.txt)", "这是全部类型 (\*.\*)"]
   * @param directory 文件路径
   * @returns
   */
  system_pyCreateFileDialog: (fileTypes: string[], directory: string) => Promise<FileInfo[]>
  /**
   * 选择文件夹对话框
   * @inpy api/system.py
   * @param directory
   * @returns
   */
  system_pySelectDirDialog: (directory: string) => Promise<string>
}

interface _PyWebViewStorage {
  /**
   *
   * @inpy api/storage.py
   * @param key
   * @returns
   */
  storage_get: (key: string) => Promise<string>
  /**
   *
   * @inpy api/storage.py
   * @param key
   * @param value
   * @returns
   */
  storage_set: (key: string, value: string) => Promise<void>
}

enum IconOSType {
  Computer = 0,
  Android = 1,
  IOS = 2
}
interface _PyWebViewTauriIcon {
  /**
   * 生成tauri图标文件夹 及 压缩包
   * @param osType 系统类型
   * @param inputFile 源文件路径
   * @param outputDir 生成目录
   * @param isZip 是否生成压缩包
   * @returns
   */
  tauri_icon_create_icon: (osType: IconOSType, inputFile: string, outputDir: string, isZip: boolean) => Promise<void | string>
}
