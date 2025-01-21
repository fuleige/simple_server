from flask import Flask, request, jsonify
import json
from enum import Enum
from functools import wraps

# 注意只有从项目根目录才不会报错
from dao.config_data_dao import ConfigDao

database_config_dao = ConfigDao()


# --------------- 一些重要实体 --------------------

class ErrorCode(Enum):
    OK = 0
    TOKEN_FAIL = 1


code_message_map = {
    ErrorCode.OK: "ok",
    ErrorCode.TOKEN_FAIL: "token auth fail"
}


class Status:

    def __init__(self, code=ErrorCode.OK, message=None):
        self._data_dict = {}
        self.reset_code_message(code, message)

    def reset_code_message(self, code, message=None):
        self._data_dict["code"] = code.value
        if message is None:
            if code in code_message_map:
                message = code_message_map[code]
            else:
                message = f"error code {code}"
        self._data_dict["message"] = message

    def add_extrac_data(self, data_key, data_val):
        self._data_dict[data_key] = data_val

    def to_response_json_httpcode(self, code=200):
        return jsonify(self._data_dict), code


# --------------- 外部访问接口 --------------------
app = Flask(__name__)


def config_url(name: str) -> str:
    return f"/qetqDemoZelda411Yxlm/config/{name}"


# def token_auth_require(func):
#     """
#     用于token鉴权的辅助函数
#     """
#     @wraps(func)
#     def token_warpper_func(*args, **kwags):
#         token_data = request.args.get("token")
#         if token_data is None or token_data != config.auth_token:
#             return Status(ErrorCode.TOKEN_FAIL).to_response_json_httpcode(403)
#         return func(*args, **kwags)
#     return token_warpper_func


@app.route(config_url("GetHttpsProxyServerConfig"), methods=['GET'])
def get_method():
    status = Status()
    status.add_extrac_data("config", json.loads(
        database_config_dao.get_https_proxy_config()))
    return status.to_response_json_httpcode()


@app.route(config_url("PutHttpsProxyServerConfig"), methods=['POST'])
def post_method():
    return Status().to_response_json_httpcode()


def main():
    ssl_context = ('tls/cert.pem', 'tls/private_key.pem')
    app.run(debug=False, port='18801', host='0.0.0.0', ssl_context=ssl_context)


if __name__ == '__main__':
    main()
