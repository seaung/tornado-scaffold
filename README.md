# Tornado-Scaffold

一个基于Tornado框架的RESTful API脚手架项目，提供了一套完整的项目结构和常用功能组件，帮助开发者快速构建高质量的Web API服务。

## 特性

- 📦 **模块化的项目结构**：清晰的目录组织，便于代码管理和扩展
- 🛡 **中间件系统**：灵活的中间件机制，支持请求前处理和响应后处理
  - CORS中间件：处理跨域请求
  - Token认证中间件：实现API接口的认证授权
- 🔧 **统一的响应格式**：标准化的API响应结构
- ✨ **数据验证**：请求参数验证机制
- 📊 **数据库支持**：集成数据库操作支持
- 🚀 **快速开发**：提供常用工具类和辅助函数

## 项目结构

```
├── app/                    # 应用主目录
│   ├── api/               # API接口模块
│   │   └── v1/           # API版本
│   ├── configs/          # 配置文件
│   ├── libs/             # 公共库
│   │   ├── database/     # 数据库相关
│   │   ├── middleware/   # 中间件
│   │   ├── utils/        # 工具类
│   │   └── validator/    # 数据验证
│   └── models/           # 数据模型
├── manage.py             # 项目管理脚本
└── requirements.txt      # 项目依赖
```

## 快速开始

### 安装

1. 克隆项目
```bash
git clone https://github.com/seaung/tornado-scaffold.git
cd tornado-scaffold
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

### 运行

```bash
python manage.py
```

## 使用示例

### 创建API接口

```python
from tornado.web import RequestHandler
from app.libs.middleware import MiddlewareManager
from app.libs.utils.response import ResponseWrapper

class UserRequestHandler(RequestHandler):
    @MiddlewareManager.apply_middleware
    async def get(self):
        return self.finish(ResponseWrapper.success(data={'msg': 'ok'}))
```

### 添加中间件

```python
from app.libs.middleware import BaseMiddleware

class CustomMiddleware(BaseMiddleware):
    async def process_request(self):
        # 请求处理前的逻辑
        pass

    async def process_response(self):
        # 响应处理前的逻辑
        pass
```

## 贡献

欢迎提交问题和改进建议！

## 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件
