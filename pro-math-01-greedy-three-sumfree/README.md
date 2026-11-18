# 贪心三项避和数列的周期

我随手把这道题丢给了网页版 ChatGPT Pro。这里是保存下来的答复和核验材料。

## 题目

对每个整数 d≥3，以 1,d−1,2d−1 为前三项。下一项取严格大于末项、且不能写成任意三个互不相同的已有项之和的最小整数。证明该数列的相邻项差值最终周期，或给出严谨反例。这是 van Berkel 与 Bosma《On t-sumfree sequences》（arXiv:2609.16843v2）的 Conjecture 4。

## 答复结果

贪心差值最终周期。答复给出 $`d\ge6`$ 时的周期修正。

以下结论来自所保存的 ChatGPT Pro 答复，证明与原创性待独立复核。

[题源与相关文献](https://arxiv.org/abs/2609.16843v2) · [保存的答复](solution.md)

## 已保存附件

- [sumfree_conjecture4_verify.py](attachments/sumfree_conjecture4_verify.py)
