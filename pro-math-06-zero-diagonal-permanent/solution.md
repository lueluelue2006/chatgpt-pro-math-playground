# ChatGPT Pro 答复

**是。五阶情形成立，而且可以得到一个带显式余量的更强结论：**

``` math

\boxed{\displaystyle
\operatorname{per}(A)\ge
\frac{11}{256}
+\frac1{6400}\left\|A-\frac{J-I}{4}\right\|_F^2 .
}
```

因此，$`\operatorname{per}(A)=11/256`$ **当且仅当**

``` math

A=\frac{J-I}{4}.
```

我构造了一个 **$`26\times26`$ 的有理平方和证书**，并完成了精确整数核验，包括多项式恒等式和正定性。下面给出这一计算机辅助证明的数学论证、证书定义及独立验证方法。

**完整证明、全部整数系数和核验程序：**

[c44_n5_exact_proof.zip](attachments/c44_n5_exact_proof.zip)

文件包包含中文证明、完整证书、两个核验实现、实际验证输出，以及证书搜索与有理化脚本。

## 一、原题与文献核对

你给出的 C44 页面确实陈述了这一猜想，并明确给出五阶候选值 $`11/256`$。本次核对时，该页面仍将一般猜想列为开放，五阶部分列出的是局部结果和有限网格检验。[Yair Lavi](https://yair-lavi.com/mincs-list/conjecture-44/index.html)

London–Minc 的 1989 年论文证明的范围是 $`n\le 4`$；Burghduff 的 1995 年论文证明了均匀非对角矩阵在各阶都是严格局部极小点。[Israel Institute of Technology+1](https://cris.technion.ac.il/en/publications/on-the-permanent-of-doubly-stochastic-matrices-with-zero-diagonal/)

以下是本次构造并核验的**五阶全局证书**。证明实际使用的是明确给出的整数矩阵、多项式恒等式和对称矩阵正定性判据。

## 二、先消去行列和：只剩 11 个变量

令

``` math

B=J-I,\qquad U=\frac B4,\qquad H=4A-B=4(A-U).
```

于是

``` math

h_{ii}=0,\qquad
\sum_j h_{ij}=0,\qquad
\sum_i h_{ij}=0,
```

并且

``` math

1+h_{ij}=4a_{ij}\ge0\qquad(i\ne j).
\tag{1}
```

记满足前三组线性等式的实向量空间为 $`V`$。它有 11 个自由变量。一个显式坐标选择是

``` math

x=(h_{24},h_{25},h_{32},h_{34},h_{35},
h_{42},h_{43},h_{45},h_{52},h_{53},h_{54}).
```

写 $`s=x_1+\cdots+x_{11}`$，则整个矩阵由下式唯一确定：

``` math

H(x)=
\begin{pmatrix}
0&-x_3-x_6-x_9&s-x_7-x_{10}&-x_1-x_4-x_{11}&-x_2-x_5-x_8\\
s-x_1-x_2&0&-s&x_1&x_2\\
-x_3-x_4-x_5&x_3&0&x_4&x_5\\
-x_6-x_7-x_8&x_6&x_7&0&x_8\\
-x_9-x_{10}-x_{11}&x_9&x_{10}&x_{11}&0
\end{pmatrix}.
\tag{2}
```

任意 $`x\in\mathbb R^{11}`$ 都给出 $`V`$ 中的一个矩阵，反之亦然。

五个元素的错排数为

``` math

!5=44.
```

因此定义

``` math

F(H)=\operatorname{per}(B+H)-44.
\tag{3}
```

代入式 (2) 后，$`F`$ 是一个总次数至多为 5 的 11 元多项式。它的常数项为零；每个非对角位置出现在恰好 11 个错排中，所以一次项为

``` math

11\sum_{i\ne j}h_{ij}=0.
```

## 三、精确证书

### 1. 使用的对称群

令

``` math

G=S_5\times\{0,1\},\qquad |G|=240.
```

对 $`g=(p,\varepsilon)`$，定义

``` math

(gH)_{ij}=
\begin{cases}
H_{p(i),p(j)},&\varepsilon=0,\\
H_{p(j),p(i)},&\varepsilon=1.
\end{cases}
\tag{4}
```

也就是同时置换行列，并允许再转置。这个群保持 $`V`$、$`F(H)`$、Frobenius 范数以及约束 (1)。

### 2. 只需要 26 个单项式

定义以下列向量；**排列顺序是证书的一部分**：

``` math

\begin{aligned}
z(H)=\big(&
h_{25},h_{32},h_{35},h_{42},h_{45},h_{52},h_{53},h_{54},\\
&
h_{12}^{2},h_{12}h_{42},h_{12}h_{32},h_{12}h_{13},
h_{13}^{2},h_{14}h_{15},\\
&
h_{32}^{2},h_{24}h_{51},h_{25}h_{41},h_{53}^{2},
h_{12}h_{45},h_{12}h_{54},\\
&
h_{45}^{2},h_{15}h_{42},h_{14}h_{52},h_{12}h_{51},
h_{21}h_{53},h_{21}h_{34}
\big)^{\mathsf T}.
\end{aligned}
\tag{5}
```

它包含 8 个一次单项式和 18 个二次单项式。

### 3. 有理 Gram 矩阵

证书给出一个整数对称矩阵 $`N\in\mathbb Z^{26\times26}`$。令

``` math

d=1\,644\,261\,835\,572\,000,
\qquad Q=\frac Nd.
\tag{6}
```

文件包中的 certificate.json 完整存储了 $`N`$ 的全部 351 个上三角整数，依次为

``` math

N_{11},N_{12},\ldots,N_{1,26},
N_{22},\ldots,N_{2,26},\ldots,N_{26,26}.
```

下三角由对称性确定。

证书文件的 SHA-256 为：

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

`f5af5642870922ec3f79e3845483d7cbe290b6f483cdc095624e5097cbc5ad76`

</div>

</div>

</div>

对这些固定整数，已经精确验证了以下两个事实：

``` math

\boxed{Q\succ0}
\tag{7}
```

以及对**每一个 $`H\in V`$** 成立的恒等式

``` math

\boxed{\displaystyle
F(H)=
\frac{\|H\|_F^2}{100}
+
\frac1{240}
\sum_{g\in G}
\bigl(1+(gH)_{12}\bigr)\,
z(gH)^{\mathsf T}Qz(gH).
}
\tag{8}
```

式 (8) 就是关键证书。它是整个线性空间 $`V`$ 上的多项式恒等式。

为便于独立实现，清除全部分母后的形式是

``` math

\boxed{\displaystyle
100\sum_{g\in G}
\bigl(1+(gH)_{12}\bigr)\,
z(gH)^{\mathsf T}Nz(gH)
=
240d\bigl(100F(H)-\|H\|_F^2\bigr).
}
\tag{9}
```

这是一条整数多项式恒等式。下一节先说明它如何立即解决原题，再说明如何严格核验证书。

## 四、由证书推出全局不等式和唯一等号

取原题中的任意可行矩阵 $`A`$，令 $`H=4A-B`$。

由非负性，对每个 $`g\in G`$，都有

``` math

1+(gH)_{12}\ge0.
```

由 $`Q\succ0`$，又有

``` math

z(gH)^{\mathsf T}Qz(gH)\ge0.
```

所以式 (8) 的求和部分非负，从而

``` math

\operatorname{per}(B+H)-44
\ge \frac{\|H\|_F^2}{100}.
\tag{10}
```

现在使用

``` math

B+H=4A,\qquad
\operatorname{per}(4A)=4^5\operatorname{per}(A),
\qquad H=4(A-U),
```

得到

``` math

\begin{aligned}
\operatorname{per}(A)-\frac{44}{1024}
&\ge
\frac{\|H\|_F^2}{100\cdot1024}\\
&=
\frac{16\|A-U\|_F^2}{100\cdot1024}\\
&=
\frac{\|A-U\|_F^2}{6400}.
\end{aligned}
```

也就是

``` math

\boxed{\displaystyle
\operatorname{per}(A)\ge
\frac{11}{256}+
\frac1{6400}\|A-U\|_F^2.
}
```

若 $`\operatorname{per}(A)=11/256`$，上式迫使

``` math

\|A-U\|_F^2=0,
```

故 $`A=U`$。

反过来，$`U`$ 的 44 个错排乘积全部等于 $`4^{-5}`$，因此

``` math

\operatorname{per}(U)=44\cdot4^{-5}=\frac{11}{256}.
```

这同时证明了所求下界与等号唯一性。

## 五、恒等式如何被完整、精确地核验

这里需要说明为什么有限计算足以验证式 (9)。

### 1. 4,368 个点具有唯一插值性

将式 (9) 左右两边相减，再代入式 (2)，得到

``` math

R(x_1,\ldots,x_{11}).
```

因为权重 $`1+(gH)_{12}`$ 的次数至多为 1，而 $`z`$ 的分量次数至多为 2，所以

``` math

\deg R\le5.
```

取

``` math

\Lambda=
\left\{
\alpha\in\mathbb Z_{\ge0}^{11}:
\alpha_1+\cdots+\alpha_{11}\le5
\right\}.
```

其大小为

``` math

|\Lambda|=\binom{11+5}{5}=4368.
```

**一个总次数至多为 5 的 11 元多项式，由它在这 4,368 个点上的取值唯一确定。**

证明可以直接使用多元 Newton 基底：

``` math

b_\beta(x)=
\prod_{i=1}^{11}\binom{x_i}{\beta_i},
\qquad |\beta|\le5.
```

这些多项式构成该多项式空间的一组基。把 $`\alpha,\beta`$ 按总次数排序，则取值矩阵

``` math

\bigl(b_\beta(\alpha)\bigr)_{\alpha,\beta\in\Lambda}
```

为下三角矩阵，对角线全部为 1：

- 若 $`|\alpha|<|\beta|`$，必有某个 $`\alpha_i<\beta_i`$，所以取值为零。
- 若 $`|\alpha|=|\beta|`$ 且 $`\alpha\ne\beta`$，同样必有这样的坐标。
- 若 $`\alpha=\beta`$，取值为 1。

因此取值映射可逆。精确检查

``` math

R(\alpha)=0\qquad(\alpha\in\Lambda)
```

就严格推出

``` math

R\equiv0.
```

**这 4,368 项检查已经全部通过。**

### 2. 运算是精确整数运算

在上述插值点上，由式 (2) 可知

``` math

|h_{ij}|\le5.
```

因此

``` math

|1+h_{ij}|\le6,\qquad |z_i(H)|\le25.
```

群求和所形成的 Gram 矩阵，其每个元素的绝对值至多为

``` math

240\cdot6\cdot25^2=900000.
```

这部分可以安全地用整数数组计算。随后与证书整数矩阵 $`N`$ 相乘，以及式 (9) 的最终比较，都使用 Python 任意精度整数。

这就给出了式 (8) 的一套完整核验，且不需要依赖数值误差阈值。

## 六、正定性如何精确核验

因为 $`d>0`$，所以 $`Q\succ0`$ 等价于 $`N\succ0`$。

核验程序对整数对称矩阵 $`N`$ 使用无分数 Bareiss 消元，计算全部 26 个顺序主子式。每一步都检查：

1.  递推中的除法整除，余数为零；
2.  得到的顺序主子式严格为正。

具体递推是：初始 $`M=N`$、$`p_{\mathrm{old}}=1`$。第 $`k`$ 步令 $`p=M_{kk}`$，并对 $`i,j>k`$ 更新

``` math

M_{ij}\leftarrow
\frac{pM_{ij}-M_{ik}M_{kj}}{p_{\mathrm{old}}},
\qquad p_{\mathrm{old}}\leftarrow p.
```

在已有各步主子式非零的条件下，每一步的 $`p`$ 正是对应的顺序主子式。全部 26 个均已精确验证为正，所以由 Sylvester 判据，

``` math

N\succ0.
```

## 七、对称性还把默认核验缩减为 34 项

文件中的默认核验程序只依赖 Python 标准库。它使用另外一套完整验证方法，利用 $`G`$ 的对称性。

$`V`$ 上各次齐次 $`G`$ 不变多项式空间的维数为：

<div>

<div>

<div>

| 次数 | 0   | 1   | 2   | 3   | 4   | 5   |
|------|-----|-----|-----|-----|-----|-----|
| 维数 | 1   | 0   | 2   | 3   | 11  | 18  |

</div>

</div>

<div>

</div>

</div>

这些维数由程序从整数群表示直接计算。若 $`R_g`$ 是群元素在 $`V`$ 上的表示，令

``` math

\chi_j=\operatorname{tr}(R_g^j),
```

则各次对称幂的迹满足 Newton 递推

``` math

h_0=1,\qquad
k h_k=\sum_{j=1}^k\chi_jh_{k-j}.
```

再在 240 个群元素上平均即可得到不变子空间维数，因为群平均算子是投影，其迹就是像空间维数。

程序另外选择固定整数矩阵 $`H_1,\ldots,H_{18}`$，并用

``` math

K^{(k)}_{ij}
=
\sum_{g\in G}
\langle H_i,gH_j\rangle_F^k
```

验证相应取值点确实能确定整个不变多项式空间。各矩阵的行列式模 $`1000003`$ 分别为：

<div>

<div>

<div>

| 次数 $`k`$ | 所需取值数 | 行列式余数 |
|------------|------------|------------|
| 2          | 2          | 402097     |
| 3          | 3          | 484704     |
| 4          | 11         | 707220     |
| 5          | 18         | 208969     |

</div>

</div>

<div>

</div>

</div>

余数全部非零，所以这些取值映射具有满秩。于是共计

``` math

2+3+11+18=34
```

项精确检查，就足以证明所有齐次部分的恒等式。

这套检查使用的取值点独立于构造证书时的线性方程。它与前面的 4,368 点全插值核验都已实际运行通过。

## 八、复跑方法和实际输出

解压文件包，进入 c44_n5_proof 目录。

默认验证只需要 Python 标准库：

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

`python verify.py certificate.json`

</div>

</div>

</div>

完整的 4,368 点插值验证需要 NumPy：

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

`python verify.py --full certificate.json`

</div>

</div>

</div>

第二个核验实现：

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

`python verify_independent.py certificate.json`

</div>

</div>

</div>

对交付证书实际执行完整验证，得到：

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

`SHA256 f5af5642870922ec3f79e3845483d7cbe290b6f483cdc095624e5097cbc5ad76 Invariant dimensions, degrees zero through five: 1 0 2 3 11 18 Orbit-kernel determinants modulo 1000003: 402097 484704 707220 208969 Verified independent polynomial identity checks: 34 Positive leading principal minors of the Gram numerator: 26 Verified all simplex-lattice identity checks: 4368 Exact certificate verified.`

</div>

</div>

</div>

整个证明所需的关键事实——**式 (8) 的全局恒等式和 $`Q`$ 的正定性**——均由包内完整给出的有限整数数据和上述核验程序确定。五阶结论及唯一等号情形随式 (10) 得证。
