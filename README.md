# 项目说明

这是一个用于农业数据控制系统的项目，包含以下模块：

- **Backend**: 主程序入口和调度器。
- **Sensors**: 传感器模块，包括温湿度、土壤湿度和气压传感器。
- **Devices**: 控制设备模块，包括继电器、LED和蜂鸣器。
- **Network**: 网络通信模块，支持MQTT和HTTP。
- **Control**: 控制逻辑模块，实现自动灌溉。
- **Database**: 数据库模块，使用SQLite存储数据。
- **AI**: AI分析模块，提供数据预测功能。
- **Web**: 基于Flask的Web界面。

## 快速开始

1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 运行Web服务器：
   ```bash
   python web/app.py
   ```

3. 查看系统设计文档：
   [docs/system_design.md](docs/system_design.md)

## 目录结构

```
backend
sensors
devices
network
control
database
ai
web
docs
requirements.txt
README.md
```