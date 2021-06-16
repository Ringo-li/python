# logging用来记录软件运行时的日志信息
import logging

# 设置loggin日志的配置
# level：显示的级别
# %(asctime)s：当前时间
# %(filename)s：当前程序文件名
# %(lineno)d：行号
# %(levelname)s：日志级别
# %(message)：日志信息
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(filename)s[lineno:%(lineno)d]-%(levelname)s-%(message)s",
                    filename="longging.log",
                    filemode="w")

logging.debug("这是一条debug级别的日志信息")
logging.info("这是一条info级别的日志信息")
logging.warning("这是一条warning级别的日志信息")
logging.error("这是一条error级别的日志信息")
logging.critical("这是一条critical级别的日志信息")