# Latency-Gesture-Control-System-for-Robotic-Arms
**本科实习项目 | 基于低延迟手势识别的机械臂控制系统**

---

## 项目概述
本项目研发了一套基于 **OpenCV、YOLOv8、TensorRT** 的高精度低延迟手势识别系统，可实现对机械臂的**实时无线控制**。
系统通过计算机视觉技术完成用户手势检测与分类，并将识别结果转换为机械臂运动指令，实现高效、稳定、低延迟的人机交互。

### 核心指标
- 手势识别准确率：**≥ 98%**
- 系统端到端延迟：**＜ 33ms**
- 复杂环境误检率：**＜ 2%**
- 机械臂定位精度：**±0.5mm**

---

## 技术架构
本项目采用视觉感知 + 深度学习推理 + 机器人控制的完整架构：

- **OpenCV**：图像处理、视频流捕获、实时画面渲染
- **YOLOv8**：手势目标检测与分类
- **TensorRT**：NVIDIA 模型推理加速引擎，大幅提升检测速度
- **ROS**：机器人操作系统，负责机械臂轨迹规划、运动控制与节点通信

---

## 主要功能
- 实时摄像头手势检测与识别
- 复杂光照/背景环境下的鲁棒定位
- 手眼标定与空间坐标映射
- 机械臂运动轨迹规划与执行
- 实时识别结果可视化界面
- 低延迟人机交互控制

---

## 系统性能
| 指标 | 数值 |
|------|------|
| 手势识别准确率 | ≥ 98% |
| 推理 + 控制总延迟 | ＜ 33ms |
| 复杂环境误检率 | ＜ 2% |
| 机械臂末端定位精度 | ±0.5mm |

---

## 环境要求
- Ubuntu 20.04 / 22.04 LTS
- Python 3.8+
- CUDA 11.6+
- cuDNN 8.4+
- NVIDIA GPU（RTX 30 系列及以上）

---

## 安装与部署

### 1. 安装系统依赖
```bash
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip cmake libopencv-dev
```

### 2. 安装 Python 依赖
```bash
pip install -r requirements.txt
```

### 3. 下载模型文件
```bash
wget https://example.com/gesture_model.trt -O models/gesture_model.trt
```

### 4. 配置文件
```bash
cp config/calibration_template.yaml config/calibration.yaml
```

---

## 运行方式

### 启动手势识别模块
```bash
python src/gesture_recognition.py --model models/gesture_model.trt
```

### 启动机械臂控制（ROS）
```bash
roslaunch arm_control arm_control.launch
```

---

## 项目说明
本项目为本科实习成果，主要研究方向：
- 计算机视觉手势识别
- 深度学习模型部署与优化
- 机器人实时控制
- 低延迟人机交互系统
```
