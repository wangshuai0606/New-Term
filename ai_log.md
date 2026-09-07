# AI智能体修复记录

- **目标**：当`--name`只含空白字符时，`main()`应以`SystemExit(2)`结束，而非输出`Hello, !`
- **约束**：不改变正常姓名的输出行为；仅修改空白校验逻辑
- **改动**：在`cli.py`中添加`name = a.name.strip()`，空白时打印错误到stderr并`sys.exit(2)`
- **验证**：pytest测试`test_whitespace_name_raises_system_exit`通过，正常姓名测试不受影响
