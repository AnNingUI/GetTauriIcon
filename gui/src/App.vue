<template>
  <div class="form-container">
    <div class="form-header">
      <div class="icon-circle">
        <i class="icon-file"></i>
      </div>
      <h2>文件处理表单</h2>
    </div>

    <el-form :model="formData" label-position="top" class="custom-form">
      <!-- 目标图片地址输入 -->
      <el-form-item label="目标图片地址" class="form-item">
        <div class="input-group">
          <div class="input-prefix">
            <i class="icon-image"></i>
          </div>
          <el-input v-model="formData.imagePath" placeholder="请输入目标图片地址" class="custom-input" />
          <el-button type="primary" @click="selectFile" class="action-button">
            选择
          </el-button>
        </div>
      </el-form-item>

      <!-- 输出文件夹地址输入 -->
      <el-form-item label="输出文件夹地址" class="form-item">
        <div class="input-group">
          <div class="input-prefix">
            <i class="icon-folder"></i>
          </div>
          <el-input v-model="formData.outputPath" placeholder="请输入输出文件夹地址" class="custom-input" />
          <el-button type="primary" @click="selectFolder" class="action-button">
            选择
          </el-button>
        </div>
      </el-form-item>

      <!-- 系统类型选择 -->
      <el-form-item label="系统类型" class="form-item">
        <div class="checkbox-container">
          <el-checkbox-group v-model="formData.systemTypes">
            <el-checkbox label="电脑" class="custom-checkbox">
              <div class="checkbox-content">
                <i class="icon-desktop"></i>
                <span>电脑</span>
              </div>
            </el-checkbox>
            <el-checkbox label="安卓" class="custom-checkbox">
              <div class="checkbox-content">
                <i class="icon-smartphone"></i>
                <span>安卓</span>
              </div>
            </el-checkbox>
          </el-checkbox-group>
        </div>
      </el-form-item>

      <!-- 是否输出压缩包 -->
      <el-form-item label="是否输出压缩包" class="form-item">
        <div class="switch-container">
          <i class="icon-archive"></i>
          <span class="switch-label">输出压缩包：</span>
          <el-switch v-model="formData.compressOutput" class="custom-switch" />
        </div>
      </el-form-item>

      <div class="spacer"></div>

      <!-- 提交按钮 -->
      <el-form-item class="form-item submit-item">
        <el-button type="success" @click="submitForm" class="submit-button">
          <i class="icon-zap"></i>
          <span>开始生成</span>
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus'
import { reactive } from 'vue'
/** @typedef { "电脑" | "安卓" | "IOS" } OSType */
const formData = reactive({
  imagePath: '',
  outputPath: '',
  /** @type { OSType[] } */
  systemTypes: [],
  compressOutput: false
})

const OSMap = {
  "电脑": 0,
  "安卓": 1,
  "IOS": 2
}

// 选择文件方法
const selectFile = () => {
  ElMessage({
    message: '请选择目标图片文件',
    type: 'info',
    customClass: 'custom-message'
  })
  window.pywebview.api.system_pyCreateFileDialog(["Image (*.svg;*.png;*.jpg;*.jpeg;*.bmp;*.ppm;*.pcx;*.xpm)"], "~").then(res => {
    formData.imagePath = res[0].path
  })
}

// 选择文件夹方法
const selectFolder = () => {
  ElMessage({
    message: '请选择输出文件夹',
    type: 'info',
    customClass: 'custom-message'
  })
  window.pywebview.api.system_pySelectDirDialog("~").then(res => {
    formData.outputPath = res
  })
}

// 提交表单方法
const submitForm = () => {
  // 表单验证
  if (!formData.imagePath) {
    ElMessage({
      message: '请输入目标图片地址',
      type: 'error',
      customClass: 'custom-message'
    })
    return
  }
  if (!formData.outputPath) {
    ElMessage({
      message: '请输入输出文件夹地址',
      type: 'error',
      customClass: 'custom-message'
    })
    return
  }
  if (formData.systemTypes.length === 0) {
    ElMessage({
      message: '请选择至少一种系统类型',
      type: 'error',
      customClass: 'custom-message'
    })
    return
  }

  // 提交表单数据
  ElMessage({
    message: '开始生成处理...',
    type: 'success',
    customClass: 'custom-message'
  })
  formData.systemTypes.forEach(osType => {
    const os = OSMap[osType]
    window.pywebview.api.tauri_icon_create_icon(os, formData.imagePath, formData.outputPath, formData.compressOutput).then(res => {
      ElMessage({
        message: `生成成功`,
        type: 'success',
        customClass: 'custom-message'
      })
    }).catch(err => {
      console.error(err)
      ElMessage({
        message: `生成失败，错误信息：${err}`,
        type: 'error',
        customClass: 'custom-message'
      })
    })
  })
}
</script>

<style scoped>
/* 图标样式 */
.icon-image::before {
  content: '🖼️';
}

.icon-folder::before {
  content: '📁';
}

.icon-folder-open::before {
  content: '📂';
}

.icon-desktop::before {
  content: '💻';
}

.icon-smartphone::before {
  content: '📱';
}

.icon-archive::before {
  content: '🗃️';
}

.icon-zap::before {
  content: '⚡';
}

.icon-file::before {
  content: '📄';
}

.form-container {
  width: 100%;
  height: 100vh;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  background: #ffffff;
  text-align: center;
  overflow: hidden;
}

.form-header {
  text-align: center;
  padding: 1rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #f8f8f8;
  border-bottom: 1px solid #eaeaea;
}

.icon-circle {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: linear-gradient(135deg, #4CAF50, #2E7D32);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 5px rgba(46, 125, 50, 0.3);
  margin-bottom: 0.5rem;
}

.icon-circle i {
  font-size: 1.5rem;
  color: white;
}

h2 {
  margin: 0;
  color: #2E7D32;
  font-size: 1.3rem;
  font-weight: 600;
}

.custom-form {
  flex: 1;
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  padding: 1rem;
  box-sizing: border-box;
}

.form-item {
  margin-bottom: 1rem !important;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.form-item :deep(.el-form-item__label) {
  justify-content: center;
  padding-bottom: 0.3rem;
  line-height: 1.2;
  font-size: 0.95rem;
  color: #333;
  font-style: normal !important;
  /* 确保标签为正体 */
}

.form-item :deep(.el-form-item__content) {
  width: 100%;
  display: flex;
  justify-content: center;
}

/* 统一输入组样式 */
.input-group {
  display: grid;
  grid-template-columns: 35px 1fr auto;
  align-items: center;
  gap: 0;
  border: 1px solid #dcdfe6;
  border-radius: 4px;
  overflow: hidden;
  background-color: #fff;
  width: 100%;
  height: 38px;
}

.input-group:focus-within {
  border-color: #4CAF50;
  box-shadow: 0 0 0 1px rgba(76, 175, 80, 0.2);
}

.input-prefix {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  background-color: #f5f7fa;
  border-right: 1px solid #dcdfe6;
  color: #4CAF50;
  font-size: 1rem;
}

.custom-input {
  width: 100%;
}

.custom-input :deep(.el-input__wrapper) {
  box-shadow: none !important;
  padding: 0 10px;
  height: 38px;
  border: none;
}

.custom-input :deep(.el-input__inner) {
  height: 38px;
  font-size: 0.9rem;
  font-style: normal !important;
  /* 确保输入文本为正体 */
}

.action-button {
  height: 38px;
  margin: 0;
  border-radius: 0;
  background: #4CAF50;
  border-color: #4CAF50;
  padding: 0 12px;
  white-space: nowrap;
  font-size: 0.9rem;
  font-style: normal !important;
  /* 确保按钮文本为正体 */
}

.action-button:hover {
  background: #2E7D32;
  border-color: #2E7D32;
}

/* 复选框容器 */
.checkbox-container {
  padding: 0.5rem 0;
  display: flex;
  justify-content: center;
  width: 100%;
}

.custom-checkbox {
  margin: 0 15px;
  display: inline-flex;
  align-items: center;
  height: 32px;
}

.custom-checkbox :deep(.el-checkbox__input) {
  transform: scale(1);
}

.checkbox-content {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 0.9rem;
  font-style: normal !important;
  /* 确保复选框文本为正体 */
}

.checkbox-content i {
  font-size: 1rem;
  color: #4CAF50;
}

/* 开关容器 */
.switch-container {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0.5rem 0;
  justify-content: center;
  height: 32px;
}

.switch-container i {
  font-size: 1rem;
  color: #4CAF50;
}

.switch-label {
  color: #606266;
  font-size: 0.9rem;
  font-style: normal !important;
  /* 确保开关标签为正体 */
}

.custom-switch :deep(.el-switch__core) {
  height: 22px;
  min-width: 44px;
}

.custom-switch :deep(.el-switch__core .el-switch__action) {
  height: 18px;
  width: 18px;
}

/* 弹性空间 */
.spacer {
  flex: 1;
  min-height: 10px;
}

/* 提交按钮 */
.submit-item {
  margin-top: auto;
  margin-bottom: 1.5rem !important;
}

.submit-button {
  width: 80%;
  height: 42px;
  border-radius: 4px;
  background: #4CAF50;
  border-color: #4CAF50;
  font-size: 1rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  font-style: normal !important;
  /* 确保按钮文本为正体 */
}

.submit-button:hover {
  background: #2E7D32;
  border-color: #2E7D32;
}

.submit-button i {
  font-size: 1rem;
}

/* 确保所有文本都是正体 */
:deep(*) {
  font-style: normal !important;
}

/* 响应式调整 */
@media (max-height: 600px) {
  .form-header {
    padding: 0.5rem 0;
  }

  .icon-circle {
    width: 40px;
    height: 40px;
    margin-bottom: 0.3rem;
  }

  .icon-circle i {
    font-size: 1.2rem;
  }

  h2 {
    font-size: 1.1rem;
  }

  .form-item {
    margin-bottom: 0.7rem !important;
  }

  .custom-form {
    padding: 0.7rem;
  }

  .submit-button {
    height: 38px;
  }
}

@media (max-height: 500px) {
  .form-header {
    padding: 0.3rem 0;
    flex-direction: row;
    justify-content: center;
    gap: 10px;
  }

  .icon-circle {
    width: 30px;
    height: 30px;
    margin-bottom: 0;
  }

  .icon-circle i {
    font-size: 1rem;
  }

  h2 {
    font-size: 1rem;
  }

  .form-item {
    margin-bottom: 0.5rem !important;
  }

  .custom-form {
    padding: 0.5rem;
  }

  .submit-button {
    height: 36px;
  }
}

@media (max-width: 480px) {
  .custom-form {
    padding: 0.5rem;
  }

  .action-button {
    padding: 0 8px;
  }
}
</style>