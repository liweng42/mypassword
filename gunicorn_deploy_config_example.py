# gunicron 部署配置

# 绑定的ip及端口号
bind = '127.0.0.1:8001'
# 进程数
"""
# (2 Workers * CPU Cores) + 1
# ---------------------------
# For 1 core  -> (2*1)+1 = 3
# For 2 cores -> (2*2)+1 = 5
# For 4 cores -> (2*4)+1 = 9
"""
workers = 2
# 监听队列
backlog = 2048
# 使用gevent模式，还可以使用sync 模式，默认的是sync模式
worker_class = "gevent"
debug = True
# 你项目的根目录, app 启动的文件所在目录
chdir = '/var/www/mypasword'
# 进程名称
proc_name = 'gunicorn.pid'
