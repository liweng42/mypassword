from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

class MyPasswordForm(FlaskForm):
    """加密自己密码
    """
    secret_key = PasswordField(
        '私密秘钥',
        validators=[
            InputRequired(message='请输入私密秘钥'),
            Length(min=8, max=16, message=u'私密秘钥8到16个字符之间')
        ])
    app_name = StringField(
        '应用名称',
        validators=[
            InputRequired(message='请输入应用名称'),
        ])
