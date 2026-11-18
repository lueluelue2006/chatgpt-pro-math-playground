# 315 方格七块蒙德里安拼图的最小面积差

我随手把这道题丢给了网页版 ChatGPT Pro。这里是保存下来的答复和核验材料。

## 题目

把 $`315\times315`$ 的正方形恰好分成七个轴平行矩形。每块边长都是正整数，七块恰好铺满，内部互不重叠。任意两块在允许旋转九十度时仍不全等。求最大块面积与最小块面积之差的精确最小值。

## 答复结果

最小面积差为 **150**。达到该值的坐标和排除 149 的结果均已复核。

已用独立 C++ 实现复跑。阈值 149 为零解，阈值 150 有解。

[题源与相关文献](https://arxiv.org/abs/2610.19193) · [保存的答复](solution.md)

## 已保存附件

- [mondrian_315_7.png](attachments/mondrian_315_7.png)
- [mondrian_315_7_verify.py](attachments/mondrian_315_7_verify.py)

## 精确最优值的复核

- [GPT Pro 的验证器](verify_315.cpp)
- [独立验证器](independent_verify.cpp)
- [下界与复跑说明](optimality.md)
