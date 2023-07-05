import random
import string

def generate_password(length):
    # 所有可能的字符集合
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # 使用random.choices随机选择字符
    password = ''.join(random.choices(all_chars, k=length))
    return password

# 要生成的密码长度
length = 12
password = generate_password(length)

print('生成的密码是:', password)
