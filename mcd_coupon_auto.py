#!/usr/bin/env python3
"""
麦当劳优惠券自动领取工具
基于麦当劳MCP协议实现自动领券功能
"""

import requests
import json
from typing import Dict, List, Optional
from datetime import datetime


class McDonaldsMCPClient:
    """麦当劳MCP客户端"""

    def __init__(self, token: str):
        """
        初始化MCP客户端

        Args:
            token: MCP Token用于身份验证
        """
        self.base_url = "https://mcp.mcd.cn/mcp-servers/mcd-mcp"
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def _call_tool(self, tool_name: str, arguments: Optional[Dict] = None) -> Dict:
        """
        调用MCP工具

        Args:
            tool_name: 工具名称
            arguments: 工具参数

        Returns:
            工具返回结果
        """
        payload = {
            "method": "tools/call",
            "params": {"name": tool_name, "arguments": arguments or {}},
        }

        try:
            response = requests.post(
                self.base_url, headers=self.headers, json=payload, timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"success": False, "error": f"请求失败: {str(e)}"}

    def get_current_time(self) -> Dict:
        """
        获取当前时间信息

        Returns:
            当前时间信息
        """
        return self._call_tool("now-time-info")

    def get_available_coupons(self) -> Dict:
        """
        查询可领取的优惠券列表

        Returns:
            可领取的优惠券列表
        """
        return self._call_tool("available-coupons")

    def auto_bind_coupons(self) -> Dict:
        """
        一键领取所有可用优惠券

        Returns:
            领券结果
        """
        return self._call_tool("auto-bind-coupons")

    def get_my_coupons(self) -> Dict:
        """
        查询我的优惠券

        Returns:
            已领取的优惠券列表
        """
        return self._call_tool("my-coupons")

    def get_campaign_calendar(self, specified_date: Optional[str] = None) -> Dict:
        """
        查询活动日历

        Args:
            specified_date: 指定日期(格式: yyyy-MM-dd)，不传则查询当月活动

        Returns:
            活动日历信息
        """
        arguments = {}
        if specified_date:
            arguments["specifiedDate"] = specified_date
        return self._call_tool("campaign-calendar", arguments)


def print_separator(char: str = "=", length: int = 60):
    """打印分隔线"""
    print(char * length)


def print_result(title: str, result: Dict):
    """
    打印结果

    Args:
        title: 标题
        result: 结果数据
    """
    print_separator()
    print(f"【{title}】")
    print_separator()

    if isinstance(result, dict):
        # 尝试提取content字段（MCP响应格式）
        if "content" in result:
            for item in result["content"]:
                if item.get("type") == "text":
                    print(item.get("text", ""))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result)
    print()


def main():
    """主函数"""
    print_separator("*")
    print("麦当劳优惠券自动领取工具".center(50))
    print_separator("*")
    print()

    # 从配置文件或环境变量读取token
    token = input("请输入您的MCP Token: ").strip()

    if not token:
        print("❌ Token不能为空！")
        return

    # 创建客户端
    client = McDonaldsMCPClient(token)

    # 菜单选项
    while True:
        print_separator("-")
        print("请选择操作：")
        print("1. 查看可领取的优惠券")
        print("2. 一键领取所有优惠券")
        print("3. 查看我的优惠券")
        print("4. 查看活动日历")
        print("5. 获取当前时间")
        print("0. 退出")
        print_separator("-")

        choice = input("请输入选项 (0-5): ").strip()
        print()

        if choice == "1":
            result = client.get_available_coupons()
            print_result("可领取的优惠券列表", result)

        elif choice == "2":
            confirm = input("确认要一键领取所有可用优惠券吗？(y/n): ").strip().lower()
            if confirm == "y":
                result = client.auto_bind_coupons()
                print_result("领券结果", result)
            else:
                print("已取消操作\n")

        elif choice == "3":
            result = client.get_my_coupons()
            print_result("我的优惠券", result)

        elif choice == "4":
            date = input("请输入日期(格式yyyy-MM-dd，留空查询当月): ").strip()
            result = client.get_campaign_calendar(date if date else None)
            print_result("活动日历", result)

        elif choice == "5":
            result = client.get_current_time()
            print_result("当前时间", result)

        elif choice == "0":
            print("感谢使用，再见！")
            break

        else:
            print("❌ 无效选项，请重新选择\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
