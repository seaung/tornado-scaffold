import os
import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

from app import create_app

# 定义命令行参数
define("port", default=9527, help="运行端口", type=int)
define("debug", default=False, help="是否开启调试模式", type=bool)


def main():
    # 解析命令行参数
    parse_command_line()

    try:
        # 创建应用实例
        app = create_app()

        # 配置应用
        app.listen(options.port)
        print(f'[+] 服务器启动成功! 监听端口: {options.port}')
        print('[+] 调试模式:', '开启' if options.debug else '关闭')

        # 启动事件循环
        tornado.ioloop.IOLoop.current().start()

    except KeyboardInterrupt:
        print('\n[-] 正在关闭服务器...')
        tornado.ioloop.IOLoop.current().stop()
        print('[-] 服务器已关闭')
    except Exception as e:
        print(f'[-] 服务器启动失败: {str(e)}')
        raise


if __name__ == '__main__':
    main()
