# ChatGPT Pro 答复

**答案是肯定的：存在这样的整数 $`N`$。** 而且可以证明更精确的结论：

``` math
\boxed{\displaystyle
\lim_{n\to\infty}n^{3/2}
\log\frac{p(n)^2}{p(n-1)p(n+1)}
=\frac{\pi}{2\sqrt2}>0.}
\tag{1}
```

下面给出完整证明。核心是两件事：构造一个使砖多重集可以铺满两行矩形的充分条件，证明这个条件失败的概率指数小；再用傅里叶反演直接估计相邻三项的差，避免对未经控制的渐近余项作差分。

本题的计数与 Gajdzica、Visser、Zakarczemny 的论文 *Rectangle Partitions Generalizing Integer Partitions* 中的 $`p(2,n)`$ 一致，该文也提出了研究这一序列对数凹性的问题。以下把需要的组合估计和解析估计都展开。[Springer Nature Link+1](https://link.springer.com/article/10.1007/s00026-026-00826-w)

## 一、先只按砖种和总面积计数

能出现在高度为 $`2`$ 的矩形中的砖，只有以下两类：

``` math
1\times k\quad(k\ge1),\qquad
2\times k\quad(k\ge2).
```

第二类从 $`k=2`$ 开始，正是为了让 $`1\times2`$ 与 $`2\times1`$ 这同一种砖只计一次。

暂时去掉“能铺满”的条件，令 $`A_m`$ 为这些砖种中总面积为 $`m`$ 的多重集数量。其生成函数为

``` math
\begin{aligned}
G(q)
&=\sum_{m\ge0}A_mq^m\\
&=\prod_{k\ge1}\frac1{1-q^k}
  \prod_{k\ge2}\frac1{1-q^{2k}}
=\prod_{j\ge1}(1-q^j)^{-b_j},
\end{aligned}
\tag{2}
```

其中

``` math
b_j=
\begin{cases}
2,&j\ge4\text{ 且 }j\text{ 为偶数},\\
1,&\text{其他情形}.
\end{cases}
\tag{3}
```

这里 $`A_m`$ 只要求总面积正确，所以允许某些实际上放不进外框的多重集。显然

``` math
p(n)\le A_{2n}.
```

对任意 $`t>0`$，给砖多重集赋予如下概率：每一种面积为 $`a`$ 的砖，其出现次数独立服从

``` math
\Pr_t(X=r)=(1-e^{-ta})e^{-tar},
\qquad r=0,1,2,\ldots.
\tag{4}
```

于是，一个总面积为 $`m`$ 的指定多重集的概率恰好是

``` math
\frac{e^{-tm}}{G(e^{-t})}.
```

记随机总面积为 $`S`$，就有

``` math
\Pr_t(S=m)=\frac{A_me^{-tm}}{G(e^{-t})}.
\tag{5}
```

这个随机多重集几乎必然有限，因为 $`S`$ 的期望有限。

## 二、关键组合引理：不能铺满的概率指数小

我们先证明：

> **引理 1。** 存在常数 $`c,C>0`$，使充分小的 $`t>0`$ 满足
>
> ``` math
> \Pr_t\!\left(
> S\text{ 为偶数，且所选多重集不能铺满 }2\times(S/2)
> \right)
> \le Ce^{-c/t}.
> \tag{6}
> ```

证明只需要一个关于子多重集和的简单观察。

### 1. 连续子集和区间的扩张

设一个整数多重集的总和为 $`T`$，它的子多重集和包含整个整数区间

``` math
[u,T-u],
```

其宽度为 $`W=T-2u`$。

加入一个整数 $`d`$ 后，新子集和同时包含

``` math
[u,T-u]
\quad\text{和}\quad
[u+d,T-u+d].
```

如果 $`d\le W+1`$，这两个整数区间相接或重叠，故其并包含

``` math
[u,T+d-u].
\tag{7}
```

这个新区间仍然以新总和的一半为中心，宽度增加了 $`d`$。

### 2. 用相邻长度的砖建立初始区间

把 $`1\times k`$、$`k\ne2`$ 的砖称为薄砖。记长度为 $`k`$ 的薄砖数量为 $`C_k`$。由随机模型，

``` math
\Pr_t(C_k\ge1)=e^{-tk},
```

且不同 $`k`$ 对应的事件独立。

取

``` math
L=8\left\lfloor\frac1{800t}\right\rfloor.
\tag{8}
```

当 $`t\to0`$ 时，$`L\asymp t^{-1}`$，并且 $`tL\le1/100`$。以下只考虑足够小的 $`t`$，从而所有涉及的长度都大于 $`2`$。

对每个

``` math
j=L,L+1,\ldots,2L-1,
```

考察长度对 $`(2j,2j+1)`$。如果两种长度的薄砖都至少出现一块，就称这一对成功。单对失败的概率不超过

``` math
1-e^{-t(4j+1)}
\le t(4j+1)
\le8tL
\le0.08.
```

这 $`L`$ 对使用互不相同的长度，因此相互独立。设成功对数为 $`M`$。用失败集合的并集界，

``` math
\Pr_t(M<L/2)
\le 2^L(0.08)^{L/2}
=(0.32)^{L/2}.
\tag{9}
```

在 $`M\ge L/2`$ 的事件上，从每个成功对中各保留一块长度为 $`2j`$ 和一块长度为 $`2j+1`$ 的砖。

令这些成功对的较小长度之和为 $`B`$。从每一对中选一块，得到的所有可能总长度恰好包含

``` math
B,B+1,\ldots,B+M.
```

保留的这些砖的总长度为 $`2B+M`$，所以我们得到了一个**以总长度的一半为中心、宽度至少为 $`L/2`$ 的连续整数区间**。

### 3. 将区间宽度扩张到 $`L^2/32`$

再考察长度集合

``` math
\left\{\frac L4,\frac L4+1,\ldots,\frac L2-1\right\}.
```

这里有 $`L/4`$ 种长度，每一种缺席的概率至多为

``` math
1-e^{-td}\le td\le \frac{tL}{2}\le0.005.
```

因此，出现的不同长度少于 $`L/8`$ 种的概率至多为

``` math
2^{L/4}(0.005)^{L/8}
=(0.02)^{L/8}.
\tag{10}
```

这些长度与上一步的长度对互不相交。

在至少有 $`L/8`$ 种长度出现时，每种取一块，逐块加入已经保留的砖。它们的长度都不超过 $`L/2`$，因而不超过当前区间宽度。由式 (7)，连续区间始终存在，且最后宽度至少为

``` math
\frac L8\cdot\frac L4=\frac{L^2}{32}.
\tag{11}
```

### 4. 吸收所有剩余薄砖

令 $`R=L^2/32`$。出现长度大于 $`R`$ 的薄砖的概率至多为

``` math
\begin{aligned}
\Pr_t(\exists k>R:C_k\ge1)
&\le\sum_{k>R}e^{-tk}\\
&\le\frac{e^{-tR}}{1-e^{-t}}
=O(e^{-c_1/t})
\end{aligned}
\tag{12}
```

，其中 $`c_1>0`$，因为 $`L\asymp t^{-1}`$。

当这种例外也没有发生时，所有剩余薄砖的长度都不超过现有区间宽度。再次反复使用式 (7)，可以把剩余薄砖全部加入。

最终，若全部薄砖的总长度为 $`H`$，其子多重集和包含一个以 $`H/2`$ 为中心的连续整数区间。

薄砖以外的砖包括所有 $`1\times2`$ 多米诺和所有 $`2\times k`$、$`k\ge2`$ 的砖，它们的面积都是偶数。因此，**当 $`S`$ 为偶数时，$`H`$ 也为偶数**。于是薄砖可以分成总长度均为 $`H/2`$ 的两组，分别铺在两行。

再把所有多米诺竖放，并把所有 $`2\times k`$ 砖并排放在这两行的旁边，就得到一个

``` math
2\times(S/2)
```

矩形。

所以，不可铺满事件必定包含在式 (9)、(10)、(12) 的例外事件之并中。它们的总概率为 $`O(e^{-c/t})`$，引理 1 得证。 $`\square`$

## 三、把随机总面积的均值调到 $`2n`$

总面积的均值和方差分别为

``` math
\mu(t)=\mathbb E_tS
=\sum_{j\ge1}\frac{b_jj}{e^{tj}-1},
\tag{13}
```
``` math
\sigma(t)^2=\operatorname{Var}_tS
=\sum_{j\ge1}\frac{b_jj^2e^{tj}}{(e^{tj}-1)^2}.
\tag{14}
```

我们需要它们的首项：

``` math
\boxed{\displaystyle
\mu(t)\sim\frac{\pi^2}{4t^2},
\qquad
\sigma(t)^2\sim\frac{\pi^2}{2t^3}.}
\tag{15}
```

这里可以直接用黎曼和证明。所需积分为

``` math
\int_0^\infty\frac{x}{e^x-1}\,dx
=\sum_{\ell\ge1}\frac1{\ell^2}
=\frac{\pi^2}{6},
\tag{16}
```
``` math
\int_0^\infty\frac{x^2e^x}{(e^x-1)^2}\,dx
=2\sum_{\ell\ge1}\frac1{\ell^2}
=\frac{\pi^2}{3}.
\tag{17}
```

每个正整数面积都有一个砖种，偶数面积 $`j\ge4`$ 额外有一个砖种。额外部分是步长为 $`2`$ 的黎曼和，贡献前一部分首项的一半。因此，式 (16)、(17) 分别乘以 $`3/2`$，即得式 (15)。

另外，

``` math
\mu'(t)=-\sigma(t)^2<0,
```

且 $`\mu(t)`$ 从 $`t\downarrow0`$ 时的无穷大连续下降到 $`t\to\infty`$ 时的零。

所以，对每个 $`m=2n`$，存在唯一的 $`t=t_n>0`$，使

``` math
\mu(t)=m.
\tag{18}
```

以下始终使用这个 $`t`$。由式 (15)，

``` math
t\sim\frac{\pi}{2\sqrt m},
\qquad
\sigma^2\sim\frac{4m^{3/2}}{\pi}.
\tag{19}
```

## 四、直接估计均值附近的二阶差分

设

``` math
a_h=\Pr_t(S=m+h),
\qquad h\in\mathbb Z.
```

我们将证明三个精确到所需尺度的估计：

``` math
\boxed{
\begin{aligned}
a_0&\sim\frac1{\sqrt{2\pi}\,\sigma},\\
2a_0-a_2-a_{-2}
&\sim\frac4{\sqrt{2\pi}\,\sigma^3},\\
a_2-a_{-2}&=o(\sigma^{-2}).
\end{aligned}}
\tag{20}
```

第二行的正号，是最终严格不等式的来源。

### 1. 中心区域的高斯极限

记中心化特征函数为

``` math
\phi_t(\theta)=\mathbb E_t e^{i\theta(S-m)}.
```

由式 (2) 和 $`\mu(t)=m`$，其对数有绝对收敛表示

``` math
\log\phi_t(\theta)
=
\sum_{j,\ell\ge1}
\frac{b_je^{-tj\ell}}{\ell}
\left(e^{ij\ell\theta}-1-ij\ell\theta\right).
\tag{21}
```

展开到二次项，得到

``` math
\log\phi_t(\theta)
=-\frac{\sigma^2\theta^2}{2}
+O(t^{-4}|\theta|^3).
\tag{22}
```

余项界的理由是

``` math
\begin{aligned}
\sum_{j,\ell\ge1}
b_jj^3\ell^2e^{-tj\ell}
&\le
2\sum_{\ell\ge1}\ell^2
\sum_{j\ge1}j^3e^{-t\ell j}\\
&\le
Ct^{-4}\sum_{\ell\ge1}\ell^{-2}
=O(t^{-4}),
\end{aligned}
```

其中用了对所有 $`u>0`$ 成立的界

``` math
\sum_{j\ge1}j^3e^{-uj}\le Cu^{-4}.
```

由于 $`\sigma\asymp t^{-3/2}`$，对每个固定实数 $`x`$，式 (22) 给出

``` math
\phi_t(x/\sigma)\longrightarrow e^{-x^2/2}.
\tag{23}
```

### 2. 整个积分区间上的统一控制

仅有式 (23) 还不够；必须控制远离中心的贡献。

由式 (21) 的实部以及 $`b_j\ge1`$，

``` math
-\log|\phi_t(\theta)|
\ge\sum_{j\ge1}e^{-tj}(1-\cos j\theta).
\tag{24}
```

令 $`r=e^{-t}`$。右端可以直接求和：

``` math
\sum_{j\ge1}r^j(1-\cos j\theta)
=
\frac{r(1+r)(1-\cos\theta)}
{(1-r)\bigl((1-r)^2+2r(1-\cos\theta)\bigr)}.
\tag{25}
```

在 $`|\theta|\le\pi`$、$`t`$ 充分小时，利用

``` math
1-r\asymp t,
\qquad
1-\cos\theta\asymp\theta^2,
```

可得某个固定 $`c>0`$，使

``` math
-\log|\phi_t(\theta)|
\ge
\frac{c\theta^2}{t(t^2+\theta^2)}.
```

特别地，调整常数 $`c`$ 后，

``` math
|\phi_t(\theta)|
\le
\begin{cases}
\exp(-c\theta^2/t^3),&|\theta|\le t,\\[2mm]
\exp(-c/t),&t\le|\theta|\le\pi.
\end{cases}
\tag{26}
```

这也排除了其他角度产生同量级振荡项的可能。

### 3. 傅里叶反演

因为 $`S`$ 是整数值随机变量，

``` math
a_h=\frac1{2\pi}\int_{-\pi}^{\pi}
e^{-ih\theta}\phi_t(\theta)\,d\theta.
\tag{27}
```

因此

``` math
2a_0-a_2-a_{-2}
=
\frac1{2\pi}\int_{-\pi}^{\pi}
(2-2\cos2\theta)\phi_t(\theta)\,d\theta,
\tag{28}
```
``` math
a_2-a_{-2}
=
\frac1{2\pi}\int_{-\pi}^{\pi}
(-2i\sin2\theta)\phi_t(\theta)\,d\theta.
\tag{29}
```

在中心区间作代换 $`x=\sigma\theta`$。由式 (23)，

``` math
\sigma^2(2-2\cos(2x/\sigma))
\longrightarrow4x^2,
```
``` math
\sigma(-2i\sin(2x/\sigma))
\longrightarrow-4ix.
```

式 (26) 给出高斯型可积控制；同时 $`\sigma t\to\infty`$，所以缩放后的中心区间扩张到整个实轴。区间 $`|\theta|\ge t`$ 的贡献，即使乘以 $`\sigma^3`$，也仍趋于零。

控制收敛定理于是给出

``` math
\begin{aligned}
\sigma a_0
&\longrightarrow
\frac1{2\pi}\int_{\mathbb R}e^{-x^2/2}\,dx
=\frac1{\sqrt{2\pi}},\\[1mm]
\sigma^3(2a_0-a_2-a_{-2})
&\longrightarrow
\frac1{2\pi}\int_{\mathbb R}4x^2e^{-x^2/2}\,dx
=\frac4{\sqrt{2\pi}},\\[1mm]
\sigma^2(a_2-a_{-2})
&\longrightarrow
\frac1{2\pi}\int_{\mathbb R}(-4ix)e^{-x^2/2}\,dx
=0.
\end{aligned}
```

最后一个积分因奇性为零。式 (20) 全部得到证明。

## 五、把估计转回真正的铺砖数

对 $`h=0,\pm2`$，定义

``` math
w_h=
\frac{e^{-t(m+h)}}{G(e^{-t})}
p\!\left(\frac{m+h}{2}\right).
\tag{30}
```

这正是“总面积为 $`m+h`$，且所选砖多重集可以铺满对应两行矩形”的概率。

由引理 1，

``` math
0\le a_h-w_h\le Ce^{-c/t}.
\tag{31}
```

而指数小的量比任意固定次幂都小，特别是

``` math
e^{-c/t}=o(\sigma^{-3}).
```

因此式 (20) 原样传递给 $`w_h`$：

``` math
\begin{aligned}
w_0&\sim\frac1{\sqrt{2\pi}\,\sigma},\\
2w_0-w_2-w_{-2}
&\sim\frac4{\sqrt{2\pi}\,\sigma^3}>0,\\
w_2-w_{-2}&=o(\sigma^{-2}).
\end{aligned}
\tag{32}
```

仅使用第二行，便有充分大的 $`n`$ 满足

``` math
w_0>\frac{w_{-2}+w_2}{2}
\ge\sqrt{w_{-2}w_2}.
```

于是

``` math
w_0^2>w_{-2}w_2.
```

式 (30) 中的权重恰好抵消：

``` math
\frac{w_0^2}{w_{-2}w_2}
=
\frac{p(n)^2}{p(n-1)p(n+1)}.
```

故

``` math
\boxed{p(n)^2>p(n-1)p(n+1)}
```

对一切充分大的 $`n`$ 成立。**题目所问的整数 $`N`$ 因而存在。**

## 六、得到开头所述的精确极限

为完成更强结论 (1)，令

``` math
H=2w_0-w_2-w_{-2},
\qquad
J=w_2-w_{-2}.
```

有恒等式

``` math
\frac{w_2w_{-2}}{w_0^2}
=
\left(1-\frac{H}{2w_0}\right)^2
-
\left(\frac{J}{2w_0}\right)^2.
\tag{33}
```

由式 (32)，

``` math
\frac{H}{w_0}\sim\frac4{\sigma^2},
\qquad
\frac{J}{w_0}=o(\sigma^{-1}).
```

代入式 (33) 得

``` math
\frac{p(n-1)p(n+1)}{p(n)^2}
=
1-\frac{4+o(1)}{\sigma^2}.
```

取对数，并使用式 (19) 中 $`m=2n`$，便得到

``` math
\begin{aligned}
\log\frac{p(n)^2}{p(n-1)p(n+1)}
&\sim\frac4{\sigma^2}\\
&\sim\frac{\pi}{(2n)^{3/2}}
=\frac{\pi}{2\sqrt2\,n^{3/2}}.
\end{aligned}
```

这证明了式 (1)，也严格确定了最终对数凹性差的正首项。 $`\square`$
