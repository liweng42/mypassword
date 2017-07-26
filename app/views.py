from flask import render_template, flash
from app.init_app import app
from app.forms import MyPasswordForm
import hashlib


# home page
@app.route('/', methods=['GET', 'POST'])
def home_page():
    """home page
    """
    form = MyPasswordForm()
    pwd = ''
    if form.validate_on_submit():
        secret_key = form.secret_key.data
        app_name = form.app_name.data
        pwd = md5(secret_key+app_name)
        pwd = strong_pwd(pwd[:16])
        # flash(u'密码为：'+pwd, 'info')
    return render_template('index.html', form=form, password_result=pwd)


# Sample HTTP error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()


def strong_pwd(str):
    """
    根据传入的字符串，将碰到的第1、3、5个数字转换为特殊字符，碰到的第2、4、6个字母转换为大写字母
    """
    s_dict = {
        1: '!',
        2: '@',
        3: '#',
        4: '$',
        5: '%',
        6: '^',
        7: '&',
        8: '*',
        9: '(',
        0: ')'
    }
    if len(str) < 16:
        raise "字符串小于16位！"
    digit_num = 0
    alpha_num = 0
    result = ''
    for i in range(len(str)):
        if str[i].isdigit():
            digit_num += 1
            if digit_num == 1 or digit_num == 3 or digit_num == 5 or digit_num == 7:
                index = int(str[i])
                result += s_dict[index]
            else:
                result += str[i]
        elif str[i].islower():
            alpha_num += 1
            if alpha_num == 2 or alpha_num == 4 or alpha_num == 6 or alpha_num == 8:
                result += str[i].upper()
            else:
                result += str[i]
        else:
            result += str[i]

    return result
