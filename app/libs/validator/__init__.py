from typing import Dict, Any, Optional
from wtforms import Form
from wtforms.validators import DataRequired


class BaseValidator:
    """通用的数据验证基类"""

    def __init__(self, data: Dict[str, Any]) -> None:
        self._form: Optional[Form] = None
        self.data = data

    def validate(self) -> bool:
        """验证数据
        
        Returns:
            bool: 验证是否通过
        """
        if not self._form:
            raise ValueError('Form instance is not initialized')
        return self._form.validate()

    @property
    def errors(self) -> Dict[str, list]:
        """获取验证错误信息
        
        Returns:
            Dict[str, list]: 错误信息字典
        """
        if not self._form:
            return {}
        return self._form.errors


class LoginValidator(BaseValidator):
    """登录数据验证器"""

    class LoginForm(Form):
        username = DataRequired(message='用户名不能为空')
        password = DataRequired(message='密码不能为空')

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data)
        self._form = self.LoginForm(data=self.data)


class RegisterValidator(BaseValidator):
    """注册数据验证器"""

    class RegisterForm(Form):
        username = DataRequired(message='用户名不能为空')
        password = DataRequired(message='密码不能为空')
        confirm_password = DataRequired(message='确认密码不能为空')
        email = DataRequired(message='邮箱不能为空')

    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__(data)
        self._form = self.RegisterForm(data=self.data)

    def validate(self) -> bool:
        """验证注册数据，包括密码确认
        
        Returns:
            bool: 验证是否通过
        """
        if not super().validate():
            return False

        if self.data['password'] != self.data['confirm_password']:
            if not self._form.errors.get('confirm_password'):
                self._form.errors['confirm_password'] = []
            self._form.errors['confirm_password'].append('两次输入的密码不一致')
            return False

        return True