from typing import Optional
from tortoise import Tortoise
from app.configs.settings import config


class DatabaseManager:
    """数据库管理器，负责处理数据库连接和初始化"""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    async def init(self, db_url: Optional[str] = None) -> None:
        """初始化数据库连接

        Args:
            db_url: 数据库连接URL，如果未提供则使用配置中的URL
        """
        if self._initialized:
            return

        db_url = db_url or config.DATABASE_URI
        if not db_url:
            raise ValueError('数据库连接URL未配置')

        # 初始化Tortoise-ORM
        await Tortoise.init(
            db_url=db_url,
            modules={'models': ['app.models']}
        )

        # 生成数据库schema
        await Tortoise.generate_schemas()

        self._initialized = True

    async def close(self) -> None:
        """关闭数据库连接"""
        if self._initialized:
            await Tortoise.close_connections()
            self._initialized = False


# 创建单例实例
db = DatabaseManager()