from typing import Any, Dict, Optional


class ResponseWrapper:
    """统一的HTTP响应封装类"""
    
    @staticmethod
    def success(data: Any = None, message: str = "success") -> Dict:
        """成功响应
        
        Args:
            data: 响应数据
            message: 响应消息
            
        Returns:
            Dict: 统一格式的响应字典
        """
        return {
            "code": 200,
            "message": message,
            "data": data
        }
    
    @staticmethod
    def error(code: int = 500, message: str = "error", data: Optional[Any] = None) -> Dict:
        """错误响应
        
        Args:
            code: 错误码
            message: 错误消息
            data: 错误详细信息
            
        Returns:
            Dict: 统一格式的响应字典
        """
        return {
            "code": code,
            "message": message,
            "data": data
        }