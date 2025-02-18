import os
from typing import Optional
from tornado.web import Application
from tornado.options import options

from app.configs.settings import settings


def create_app() -> Application:
    """创建并配置Tornado应用实例

    Returns:
        Application: 配置完成的Tornado应用实例
    """
    # 初始化数据库连接
    from app.libs.database import db
    await db.init()

    # 注册中间件
    from app.libs.middleware import MiddlewareManager
    from app.libs.middleware.cors import CORSMiddleware
    from app.libs.middleware.auth import TokenAuthMiddleware

    # 注册CORS中间件
    MiddlewareManager.register(CORSMiddleware)
    # 注册Token认证中间件
    MiddlewareManager.register(TokenAuthMiddleware)

    # 导入路由配置
    from app.configs.urls import url_patterns

    # 创建应用实例
    app = Application(
        handlers=url_patterns,
        debug=options.debug,
        **settings
    )

    # 设置项目根目录
    app.root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    return app
