import requests
import urllib3

# 禁用 SSL 警告
urllib3.disable_warnings()

# 服务器地址
SERVER_URL = "http://47.103.61.134:4060/message"

# 要发送的消息
message = "hello, i am julyfun"

# 准备请求数据
data = {
    "content": message
}

try:
    # 添加超时设置和更多调试信息
    print(f"正在连接服务器: {SERVER_URL}")
    response = requests.post(
        SERVER_URL, 
        json=data,
        timeout=10,  # 10秒超时
        verify=False  # 忽略 SSL 验证
    )
    
    # 检查响应
    if response.status_code == 200:
        print("消息发送成功！")
        print("服务器响应:", response.json())
    else:
        print(f"发送失败，状态码: {response.status_code}")
        print("错误信息:", response.text)
        print("响应头:", response.headers)
        
except requests.exceptions.Timeout:
    print("请求超时，服务器没有及时响应")
except requests.exceptions.ConnectionError:
    print("连接错误，无法连接到服务器")
except requests.exceptions.RequestException as e:
    print(f"发送请求时出错: {e}")
