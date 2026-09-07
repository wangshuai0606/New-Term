# Q11 协作材料重写

## 重写的Issue

**环境：** Windows 10/11，Python 3.10+，greetlab-25040032035 v0.1.0

**复现命令：**

    sdt-greet --name "   "

**期望结果：** 程序应检测到空白姓名，输出错误信息到stderr，并以退出码2结束。

**实际结果：** 程序仍输出 `Hello, !`，并以退出码0正常结束。

**影响：** 空白姓名被视为合法输入，可能导致下游系统收到无效数据。

---

## 重写的提交信息

**标题：** Reject whitespace-only names in greetlab CLI

**正文：**
- 问题：`--name "   "` 时仍输出问候语，未做空白校验
- 解决：在cli.py中添加name.strip()，空白时sys.exit(2)
- 测试：新增pytest测试验证空白姓名触发SystemExit(2)

---

## 重写的评审意见

**[Blocking]** 当前实现未校验空白姓名，建议修复：
1. 对a.name执行strip()，若结果为空则sys.exit(2)
2. 错误信息输出到stderr
3. 新增pytest测试覆盖空白姓名场景

**[Suggestion]** 考虑在argparse层面添加type=str.strip
