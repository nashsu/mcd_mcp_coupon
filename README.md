# About

本程序是基于麦当劳官方MCP协议，使用 OpenCode 基于 Sonnet4.5 全自动开发，目的是测试 OpenCode、Sonnet4.5 以及 vibe coding 的能力。

使用的 vibe coding 指令是：

``` https://open.mcd.cn/mcp/doc 这个是麦当劳MCP服务的说明文档，仔细阅读文档内容，基于文档内容编写一个python程序，通过MCP协议帮我自动领取优惠券，我会提供token进行身份验证。文档如果不能正常获取，请不要开始编程。 ```


# 麦当劳优惠券自动领取工具

基于麦当劳MCP协议的Python自动领券工具，帮助您快速领取麦当劳优惠券。

## 功能特性

- ✅ 查看可领取的优惠券列表
- ✅ 一键领取所有可用优惠券
- ✅ 查看已领取的优惠券
- ✅ 查看麦当劳活动日历
- ✅ 获取当前时间信息

## 准备工作

### 1. 申请 MCP Token

访问麦当劳MCP平台：https://open.mcd.cn/mcp/doc

按照以下步骤申请Token：
1. 点击右上角【登录】按钮
2. 使用手机号验证登录
3. 登录成功后点击【控制台】
4. 点击【激活】按钮申请MCP Token
5. 同意服务协议
6. 复制生成的MCP Token

### 2. 安装依赖

确保已安装Python 3.6+，然后安装依赖：

```bash
pip install requests
```

## 使用方法

### 方式一：交互式使用（推荐）

直接运行程序，按提示操作：

```bash
python mcd_coupon_auto.py
```

程序会提示您输入MCP Token，然后显示菜单供您选择操作：

```
请选择操作：
1. 查看可领取的优惠券
2. 一键领取所有优惠券
3. 查看我的优惠券
4. 查看活动日历
5. 获取当前时间
0. 退出
```

### 方式二：作为Python模块使用

```python
from mcd_coupon_auto import McDonaldsMCPClient

# 初始化客户端
client = McDonaldsMCPClient(token="YOUR_MCP_TOKEN")

# 查看可领取的优惠券
available = client.get_available_coupons()
print(available)

# 一键领取所有优惠券
result = client.auto_bind_coupons()
print(result)

# 查看我的优惠券
my_coupons = client.get_my_coupons()
print(my_coupons)

# 查看活动日历
calendar = client.get_campaign_calendar()
print(calendar)
```

## MCP 工具说明

本工具基于麦当劳MCP协议实现，支持以下工具：

| 工具名称 | 功能说明 |
|---------|---------|
| `available-coupons` | 查询用户当前可领取的麦麦省优惠券列表 |
| `auto-bind-coupons` | 自动领取麦麦省所有当前可用的优惠券 |
| `my-coupons` | 查询用户已领取的优惠券 |
| `campaign-calendar` | 查询麦当劳当月营销活动日历 |
| `now-time-info` | 获取当前时间信息 |

## 注意事项

1. **Token安全**：请妥善保管您的MCP Token，不要泄露给他人
2. **请求限制**：每个Token每分钟最多600次请求，请合理控制使用频率
3. **协议支持**：本工具使用Streamable HTTP协议
4. **版本要求**：支持MCP Version 2025-06-18及之前版本

## 技术规格

- **接入地址**: https://mcp.mcd.cn/mcp-servers/mcd-mcp
- **传输协议**: Streamable HTTP
- **认证方式**: Bearer Token (在Authorization请求头中)
- **请求格式**: JSON
- **速率限制**: 600次/分钟

## 常见问题

### Q: Token无效怎么办？
A: 请检查Token是否正确复制，是否已激活，或者重新申请Token。

### Q: 提示请求失败？
A: 检查网络连接，确认是否超过请求频率限制（600次/分钟）。

### Q: 领券失败？
A: 可能原因：
- 优惠券已被领取
- 优惠券数量已达上限
- 不满足领取条件

## 相关链接

- [麦当劳MCP文档](https://open.mcd.cn/mcp/doc)
- [MCP协议官方文档](https://modelcontextprotocol.io/)

## 免责声明

本工具仅供学习交流使用，请遵守麦当劳相关服务条款。使用本工具产生的任何后果由使用者自行承担。

## License

MIT License
