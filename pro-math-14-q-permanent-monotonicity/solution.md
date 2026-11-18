# ChatGPT Pro 答复

**命题成立。** 对每个非对角的实对称正定 $`4\times4`$ 矩阵 $`A`$，$`P_A(q)`$ 在 $`[-1,1]`$ 上严格递增。

下面给出一份**显式平方和证明**：把 $`P'_A(q)`$ 在两个半区间上的 Bernstein 系数，全部写成非负整数加权的平方和。所列恒等式可以直接展开核验；文末附有仅用 Python 标准库、整数和有理数运算的完整校验程序。

先说明题源核对结果。da Fonseca–Goyal 的论文中，四阶反例发生在 $`q=44,45`$，作者明确说明其构造不解决 $`[-1,1]`$ 上的实对称情形。Mitchell 的论文证明了秩一和三阶情形，并指出四阶情形仍有困难。以下给出本次构造的独立代数证书。[arxiv.org+1](https://arxiv.org/abs/2611.14694)

## 1. 归一化与完整的四阶展开

令

``` math

D=\operatorname{diag}(\sqrt{a_{11}},\ldots,\sqrt{a_{44}}),
\qquad R=D^{-1}AD^{-1}.
```

每个排列项都获得相同的正因子，因此

``` math

P_A(q)=\left(\prod_{i=1}^4a_{ii}\right)P_R(q).
```

故只需考虑对角元全为 $`1`$ 的情形。以下仍把归一化后的矩阵记为 $`A`$，写成

``` math

A=
\begin{pmatrix}
1&a&b&c\\
a&1&d&e\\
b&d&1&f\\
c&e&f&1
\end{pmatrix}.
```

令

``` math

P_A(q)=\sum_{r=0}^{6}p_rq^r.
```

直接枚举 $`S_4`$ 的 $`24`$ 个排列，得到：

<div>

<div>

<div>

| $`r`$ | $`p_r`$                 |
|-------|-------------------------|
| $`0`$ | $`1`$                   |
| $`1`$ | $`a^2+d^2+f^2`$         |
| $`2`$ | $`a^2f^2+2abd+2def`$    |
| $`3`$ | $`b^2+e^2+2abef+2acdf`$ |
| $`4`$ | $`b^2e^2+2ace+2bcf`$    |
| $`5`$ | $`c^2+2bcde`$           |
| $`6`$ | $`c^2d^2`$              |

</div>

</div>

<div>

</div>

</div>

我们的目标是证明

``` math

P'_A(q)\geq 0\qquad(-1\leq q\leq1),
```

然后单独处理严格性。

## 2. 把问题化为十二个 Bernstein 系数的非负性

对 $`\varepsilon\in\{-1,+1\}`$，在 $`0\leq t\leq1`$ 上写

``` math

P'_A(\varepsilon t)
=
\sum_{k=0}^{5}\binom5k B_k^\varepsilon
t^k(1-t)^{5-k}.
\tag{1}
```

这里始终是**先对 $`q`$ 求导，再代入 $`q=\varepsilon t`$**。

普通幂基与 Bernstein 基之间的转换给出

``` math

B_k^\varepsilon
=
\sum_{j=0}^{k}
\frac{\binom kj}{\binom5j}
\,\varepsilon^j(j+1)p_{j+1}.
\tag{2}
```

特别地，

``` math

B_0^-=B_0^+=a^2+d^2+f^2\geq0.
\tag{3}
```

下面将剩余十个系数 $`B_k^\varepsilon`$，$`1\leq k\leq5`$，全部写成平方和。由于式 (1) 中的所有基函数都非负，这便足以证明导数非负。

## 3. 平方和所用的辅助矩阵

由 $`A\succeq0`$ 及其单位对角，可取实单位向量

``` math

v_1,v_2,v_3,v_4\in\mathbb R^4,
\qquad a_{ij}=\langle v_i,v_j\rangle.
```

定义六个秩至多为一的矩阵：

``` math

\begin{aligned}
T_a&=a\,v_3v_4^{\mathsf T},
&
T_b&=b\,v_2v_4^{\mathsf T},
&
T_c&=c\,v_2v_3^{\mathsf T},\\
T_d&=d\,v_1v_4^{\mathsf T},
&
T_e&=e\,v_1v_3^{\mathsf T},
&
T_f&=f\,v_1v_2^{\mathsf T}.
\end{aligned}
\tag{4}
```

对 $`g\in\{a,b,c,d,e,f\}`$，令

``` math

S_g=\frac{T_g+T_g^{\mathsf T}}{\sqrt2},
\qquad
W_g=\frac{T_g-T_g^{\mathsf T}}{\sqrt2}.
\tag{5}
```

为缩短证书，以下用直立字母 $`\mathsf A,\ldots,\mathsf L`$ 表示辅助矩阵；它们与原矩阵 $`A`$ 区分开：

<div>

<div>

<div>

| 对称辅助矩阵  | 定义        | 反对称辅助矩阵 | 定义        |
|---------------|-------------|----------------|-------------|
| $`\mathsf A`$ | $`S_a+S_f`$ | $`\mathsf G`$  | $`W_a+W_f`$ |
| $`\mathsf B`$ | $`S_b+S_e`$ | $`\mathsf H`$  | $`W_b+W_e`$ |
| $`\mathsf C`$ | $`S_c`$     | $`\mathsf I`$  | $`W_c`$     |
| $`\mathsf D`$ | $`S_d`$     | $`\mathsf J`$  | $`W_d`$     |
| $`\mathsf E`$ | $`S_a-S_f`$ | $`\mathsf K`$  | $`W_a-W_f`$ |
| $`\mathsf F`$ | $`S_b-S_e`$ | $`\mathsf L`$  | $`W_b-W_e`$ |

</div>

</div>

<div>

</div>

</div>

另设三个实数

``` math

X=af,\qquad Y=be,\qquad Z=cd.
\tag{6}
```

**方括号统一表示平方：**

``` math

[U]=\|U\|_F^2
```

当 $`U`$ 是矩阵时取 Frobenius 范数平方；当 $`U`$ 是实数时，$`[U]=U^2`$。因此下面每一个方括号项都非负。

## 4. 完整的平方和证书

设

``` math

\mathcal R_k^\varepsilon=20B_k^\varepsilon.
```

### 4.1 负半区间 $`q=-t`$

五个系数满足：

``` math

\boxed{
\begin{aligned}
\mathcal R_1^-={}&
10[\mathsf D]+8[\mathsf E]+2[\mathsf J]
+8[\mathsf G-\mathsf J]+2[\mathsf G]+2[\mathsf K].
\end{aligned}}
\tag{7}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_2^-={}&
3[\mathsf B-\mathsf D]+5[\mathsf A-\mathsf D]
+4[\mathsf J]+8[\mathsf G-\mathsf J]\\
&+3[\mathsf L]+7[\mathsf K]+4[X-Z].
\end{aligned}}
\tag{8}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_3^-={}&
4[\mathsf D]+4[\mathsf A-\mathsf B]
+5[\mathsf H-\mathsf J]+3[\mathsf H]\\
&+11[\mathsf G-\mathsf J]+[\mathsf G]
+2[\mathsf L]+4[\mathsf K-\mathsf L]+12[Y-Z].
\end{aligned}}
\tag{9}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_4^-={}&
2[\mathsf C+\mathsf D]
+8[\mathsf B-\mathsf C-\mathsf D]
+2[\mathsf A-\mathsf B]\\
&+4[\mathsf J]+4[\mathsf I]
+6[\mathsf H-\mathsf I-\mathsf J]\\
&+4[\mathsf L]+16[\mathsf K-\mathsf L]+2[\mathsf K].
\end{aligned}}
\tag{10}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_5^-={}&
10[\mathsf F]+10[\mathsf H-2\mathsf I]
+20[\mathsf H-\mathsf I-\mathsf J]\\
&+10[\mathsf G-\mathsf H+2\mathsf I]
+10[\mathsf K-\mathsf L].
\end{aligned}}
\tag{11}
```

其中式 (11) 尤其给出了端点 $`q=-1`$ 的五项平方和：

``` math

\begin{aligned}
P'_A(-1)={}&
\tfrac12[\mathsf F]+\tfrac12[\mathsf H-2\mathsf I]
+[\mathsf H-\mathsf I-\mathsf J]\\
&+\tfrac12[\mathsf G-\mathsf H+2\mathsf I]
+\tfrac12[\mathsf K-\mathsf L].
\end{aligned}
\tag{12}
```

### 4.2 正半区间 $`q=t`$

五个系数满足：

``` math

\boxed{
\begin{aligned}
\mathcal R_1^+={}&
5[\mathsf D]+5[\mathsf A+\mathsf D]
+7[\mathsf E]+7[\mathsf J]\\
&+2[\mathsf G]+3[\mathsf G+\mathsf J]+3[\mathsf K].
\end{aligned}}
\tag{13}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_2^+={}&
[\mathsf D]+[\mathsf B]+[\mathsf B+\mathsf D]
+8[\mathsf A+\mathsf D]+6[\mathsf E]\\
&+5[\mathsf J]+[\mathsf H]+[\mathsf H+\mathsf J]
+4[\mathsf G+\mathsf J]\\
&+[\mathsf G+\mathsf H]+[\mathsf K+\mathsf L]+4[Y].
\end{aligned}}
\tag{14}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_3^+={}&
2[\mathsf D]+[\mathsf B+\mathsf D]
+5[\mathsf A+\mathsf D]+6[\mathsf A+\mathsf B]\\
&+2[\mathsf E]+2[\mathsf E+\mathsf F]
+6[\mathsf J]+5[\mathsf H+\mathsf J]\\
&+[\mathsf G+\mathsf J]+4[\mathsf K+\mathsf L]
+4[Y]+4[Y+Z]+4[X].
\end{aligned}}
\tag{15}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_4^+={}&
8[\mathsf D]+2[\mathsf B+\mathsf D]
+5[\mathsf A+\mathsf B]
+2[\mathsf A+\mathsf B+\mathsf D]\\
&+6[\mathsf A+\mathsf B+\mathsf C]
+8[\mathsf F]+2[\mathsf J]+14[\mathsf I]\\
&+6[\mathsf H+\mathsf J]+7[\mathsf K+\mathsf L]
+8[Y]+4[Y+Z]+20[X].
\end{aligned}}
\tag{16}
```
``` math

\boxed{
\begin{aligned}
\mathcal R_5^+={}&
52[\mathsf C]+4[\mathsf B+\mathsf D]
+20[\mathsf B+\mathsf C]+7[\mathsf B+\mathsf C+\mathsf D]\\
&+12[\mathsf A+\mathsf B+\mathsf C]
+9[\mathsf H+\mathsf I+\mathsf J]
+8[\mathsf K+\mathsf L]\\
&+32[Z]+4[Y-Z]+20[Y]+4[X-Y]+28[X].
\end{aligned}}
\tag{17}
```

这十个恒等式的右端均为非负整数加权的平方和，故

``` math

B_k^\varepsilon\geq0
\quad
(\varepsilon=\pm1,\;0\leq k\leq5).
```

代回式 (1)，立即得到

``` math

\boxed{P'_A(q)\geq0\qquad\text{对所有 }q\in[-1,1].}
\tag{18}
```

## 5. 为什么这些恒等式可独立核验

这里的非平凡步骤已经完整地列为有限个代数恒等式，没有使用数值近似来判定正负。

展开它们只需一个基本公式。若

``` math

T_g=g\,v_kv_l^{\mathsf T},
\qquad
T_h=h\,v_mv_n^{\mathsf T},
```

则由式 (5)：

``` math

\begin{aligned}
\langle S_g,S_h\rangle_F
&=gh\bigl(a_{km}a_{ln}+a_{kn}a_{lm}\bigr),\\
\langle W_g,W_h\rangle_F
&=gh\bigl(a_{km}a_{ln}-a_{kn}a_{lm}\bigr).
\end{aligned}
\tag{19}
```

这里 $`a_{ii}=1`$。

因此，核验式 (7)–(17) 的方法是：

1.  用式 (19) 展开右端各个范数平方。
2.  用第 1 节的 $`p_r`$ 和式 (2) 展开左端 $`20B_k^\varepsilon`$。
3.  比较 $`a,b,c,d,e,f`$ 的单项式系数。

例如，

``` math

B_1^-
=
a^2+d^2+f^2
-\frac25\bigl(a^2f^2+2abd+2def\bigr),
```

式 (7) 展开后恰好等于其 $`20`$ 倍。其余九式按完全相同的规则核验。

附件程序做了这一有限核验，并且从原始的 **24 个排列项**重新生成左端，未把上面的系数表当作输入。我还用保留全部十个独立对称矩阵元的另一套张量收缩计算，独立核对了所有恒等式，包括：

- 对称与反对称张量的符号；
- 因子 $`20`$；
- Bernstein 基中的 $`\binom5k`$；
- 负半区间中的 $`\varepsilon^j`$。

所有比较均为精确代数比较。

## 6. 从导数非负得到严格递增

还需排除 $`P_A`$ 为常数。由第 1 节的展开即可完成，无需假设导数在每一点都严格为正。

- 如果 $`a,d,f`$ 中至少一个非零，则

  ``` math

  P'_A(0)=a^2+d^2+f^2>0.
  ```

- 如果 $`a=d=f=0`$，而 $`b,e`$ 中至少一个非零，则 $`P_A(q)-1`$ 的最低次非零项为

  ``` math

  (b^2+e^2)q^3.
  ```

- 如果 $`a=d=f=b=e=0`$，由非对角性可知 $`c\ne0`$，此时

  ``` math

  P_A(q)=1+c^2q^5.
  ```

故对每个非对角矩阵，$`P'_A`$ 都是**非零多项式**。

现在任取 $`-1\leq u<v\leq1`$。由式 (18)，

``` math

P_A(v)-P_A(u)=\int_u^v P'_A(q)\,dq\geq0.
```

若此积分为零，连续非负函数 $`P'_A`$ 必在整个 $`[u,v]`$ 上恒为零，进而作为多项式恒等于零，矛盾。因此

``` math

\boxed{
P_A(u)<P_A(v)
\qquad(-1\leq u<v\leq1).
}
```

恢复第 1 节的正比例因子后，结论对原来的任意非对角实对称正定 $`4\times4`$ 矩阵成立。证毕。

------------------------------------------------------------------------

### 精确复核程序

[q_permanent4_sos_certificate.py](attachments/q_permanent4_sos_certificate.py)

运行：

<div>

<div>

<div>

<div>

Bash

</div>

<div>

<div>

</div>

</div>

</div>

<div>

`python q_permanent4_sos_certificate.py`

</div>

</div>

</div>

程序不需要第三方依赖，内含完整平方和证书。输出为：

<div>

<div>

<div>

<div>

Plain text

</div>

<div>

<div>

</div>

</div>

</div>

<div>

`PASS: all 42 square forms have nonnegative integer weights. PASS: all 12 normalized degree-5 Bernstein identities hold exactly. PASS: the defining polynomial was expanded directly over all 24 permutations. Arithmetic: Python integers and fractions.Fraction; no floating point.`

</div>

</div>

</div>
