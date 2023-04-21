# -*- coding: utf-8 -*-
# @Author : John
# @Time : 2023/04/19
# @File : test_redis.py

import redis

conn = redis.Redis(host='127.0.0.1', port=6379, password='qwe123', encoding='utf-8')

# 短信验证码
# conn.set('15131255089', 9999, ex=10)
# value = conn.get('15131255089')
# print(value)

# ******************************* #

# 放值
# conn.lpush('my_queue', "root")
# conn.lpush('my_queue', "good")

# 取值
# v1 = conn.brpop("my_queue", timeout=5)
# print(v1)