# coding=utf-8

import matplotlib.pyplot as plt
fig = plt.figure() #figsize=(10,6)
ax= fig.add_subplot(111)
ax.set_xlim([1, 6]);
ax.set_ylim([1, 9]);
ax.text(2, 8,  r"$ \mu \alpha \tau \pi \lambda \omega \tau \
    lambda \iota \beta $",color='r',fontsize=20);
ax.text(2, 6, r"$ \lim_{x \rightarrow 0} \frac{1}{x} $",fontsize=20);
ax.text(2, 4, r"$ a \ \leq \ b \ \leq \ c \ \Rightarrow \ a \
    \leq \ c$",fontsize=20);
#
ax.text(2, 2, r"$ \sum_{i=1}^{\infty}\ x_i^2$",fontsize=20)
ax.text(5, 5, r'$ 1/10^{200}$')
ax.text(1, 5, r'$ 1/10_{200}$')

ax.text(4, 8, r"$ \sin(0) = \cos(\frac{\pi}{2})$",fontsize=20);
ax.text(4, 6, r"$ \sqrt[3]{x} = \sqrt{y}$",fontsize=20);
ax.text(4, 4, r"$ \neg (a \wedge b) \Leftrightarrow \neg a \
    \vee \neg b$");
ax.text(4, 2, r"$ \int_a^b f(x)dx$",fontsize=20);
plt.show()
