from typing import Any, Optional
from tortoise import fields
from tortoise.models import Model
from datetime import datetime


class DBBaseModel(Model):
    """数据库模型基类

    提供通用字段和方法的基类，所有模型类都应该继承这个类。
    包含了创建时间、更新时间、软删除等通用功能。
    """
    id = fields.IntField(pk=True, description='主键ID')
    created_at = fields.DatetimeField(auto_now_add=True, description='创建时间')
    updated_at = fields.DatetimeField(auto_now=True, description='更新时间')
    is_deleted = fields.BooleanField(default=False, description='是否已删除')

    class Meta:
        abstract = True  # 标记为抽象基类，这样不会创建实际的数据库表

    def __str__(self) -> str:
        """返回模型的字符串表示"""
        return f'{self.__class__.__name__}(id={self.id})'

    async def soft_delete(self) -> None:
        """软删除记录"""
        self.is_deleted = True
        self.updated_at = datetime.now()
        await self.save()

    @classmethod
    async def get_by_id(cls, id: int) -> Optional['DBBaseModel']:
        """根据ID获取记录

        Args:
            id: 记录ID

        Returns:
            Optional[DBBaseModel]: 如果找到记录则返回实例，否则返回None
        """
        return await cls.get_or_none(id=id, is_deleted=False)

    async def update_fields(self, **kwargs: Any) -> None:
        """更新指定字段

        Args:
            **kwargs: 需要更新的字段和值
        """
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.updated_at = datetime.now()
        await self.save()