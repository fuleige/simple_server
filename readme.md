# 环境变量

```bash
# 系统需要配置变量而不是硬编码来保证数据安全

# Mysql的密码
export MYSQL_CONFIG_PWD=xxxxxx
# 服务器的token
export SERVER_AUTH_TOKEN=xxxxxx
```

# ubuntu 配置 Mysql 服务

```bash
# 安装
sudo apt install mysql-server -y

# 默认root没有密码, 直接执行
sudo mysql

# -- 在 Mysql Shell中
CREATE DATABASE config_database;

# 提前将密码保存到环境变量中 MYSQL_CONFIG_PWD
CREATE USER 'configurator'@'localhost' IDENTIFIED WITH mysql_native_password BY $MYSQL_CONFIG_PWD;

GRANT ALL PRIVILEGES ON mydatabase.* TO 'configurator'@'localhost';

FLUSH PRIVILEGES;
```

# 生成私钥证书以启动tls加密

```bash
# 将这些文件保存在tls目录下
mdir -p tls
cd tls

# 生成私钥
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048

# 创建证书
openssl req -new -key private_key.pem -out csr.pem
openssl x509 -req -days 3650 -in csr.pem -signkey private_key.pem -out cert.pem
```

# 开启服务

```bash

# 安装相关的库
pip3 install flask mysql

```