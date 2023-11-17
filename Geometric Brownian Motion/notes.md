# Geometric Brownian Motion (GBM)

A **Geometric Brownian Motion (GBM)**, also known as exponential Brownian motion, is a continuous-time stochastic process. In this process, the logarithm of a randomly varying quantity follows a Brownian motion, also known as a Wiener process, with drift. GBM is a crucial example of stochastic processes that satisfy a stochastic differential equation (SDE), notably used in mathematical finance to model stock prices in the Black–Scholes model.

## Technical Definition: The SDE

A stochastic process $S_{t}$ is said to follow a GBM if it satisfies the following stochastic differential equation (SDE):

$$
dS_{t} = \mu S_{t} dt + \sigma S_{t} dW_{t}
$$

where $W_{t}$ is a Wiener process or Brownian motion, and $\mu$ (the percentage drift) and $\sigma$ (the percentage volatility) are constants. The drift models deterministic trends, while the volatility models unpredictable events during the motion.

## Solving the SDE

For an arbitrary initial value $S_{0}$, the SDE has the analytic solution (under Itô's interpretation):

$$
S_{t} = S_{0} \exp\left(\left(\mu - \frac{\sigma^{2}}{2}\right)t + \sigma W_{t}\right)
$$

The derivation requires the use of Itô calculus. Applying Itô's formula to $f(S) = \ln(S)$ gives:

$$
\begin{aligned}
d\ln(S) &= f'(S) dS + \frac{1}{2}f''(S)S^{2}\sigma^{2} dt\\
&= \frac{1}{S}(\sigma S dW_{t} + \mu S dt) - \frac{1}{2}\sigma^{2} dt\\
&= \sigma dW_{t} + (\mu - \frac{\sigma^{2}}{2}) dt.
\end{aligned}
$$

It follows that $E(\ln(S_{t})) = \ln(S_{0}) + (\mu - \frac{\sigma^{2}}{2})t$.

## Arithmetic Brownian Motion

The process $X_{t} = \ln\left(\frac{S_{t}}{S_{0}}\right)$, satisfying the SDE

$$
dX_{t} = \left(\mu - \frac{\sigma^{2}}{2}\right)dt + \sigma dW_{t}
$$

is known as Arithmetic Brownian Motion (ABM). This model was postulated by Louis Bachelier in 1900 for stock prices, representing the first attempt to model Brownian motion, now known as the Bachelier model. The ABM SDE can be obtained through the logarithm of a GBM via Itô's formula.

## Properties of GBM

The solution $S_{t}$ is a log-normally distributed random variable. The expected value and variance are given by:

$$
E(S_{t}) = S_{0}e^{\mu t},
$$

$$
\text{Var}(S_{t}) = S_{0}^{2}e^{2\mu t}\left(e^{\sigma^{2}t} - 1\right).
$$

These properties can be derived using the fact that $Z_{t} = \exp\left(\sigma W_{t} - \frac{1}{2}\sigma^{2}t\right)$ is a martingale.

## Code Outputs

### Simulated Paths
![Simulated paths for X(t) and S(t)](https://github.com/espinetandreu/Financial-Mathematics/blob/main/Geometric%20Brownian%20Motion/ABMvsGBM.png)

### Distribution at final time
![Distribution at final time](https://github.com/espinetandreu/Financial-Mathematics/blob/main/Geometric%20Brownian%20Motion/PDFABMvsGBM.png)

