# Derivation of the Black-Scholes Model using Itô's Lemma

The Black-Scholes model is derived using Itô's lemma applied to a specific function of the Geometric Brownian Motion (GBM). The main idea is to consider the function representing the option price and then apply Itô's lemma to derive the stochastic differential equation (SDE) governing its dynamics.

## Geometric Brownian Motion (GBM) Dynamics

The underlying asset, $S_t$, follows a Geometric Brownian Motion (GBM) with drift $\mu$ and volatility $\sigma$:

$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

## Option Price Dynamics

The option price, denoted by $C(S, t)$, is a function of the underlying asset price $S$ and time $t$. The Black-Scholes model assumes a risk-free interest rate $r$.

The dynamics of the option price can be represented as the second-order Taylor expansion:

$$
dC = \frac{\partial C}{\partial t} dt + \frac{\partial C}{\partial S} dS + \frac{1}{2} \frac{\partial^2 C}{\partial S^2} (dS)^2
$$

Applying Itô's lemma to the option price function $C(S, t)$, we have $(dW)^2=dt$:

$$
dC = \frac{\partial C}{\partial t} dt + \frac{\partial C}{\partial S} dS + \frac{1}{2} \frac{\partial^2 C}{\partial S^2} \sigma^2 S^2 dt
$$

Now, substitute the GBM dynamics for $dS$:

$$
dC = \left(\frac{\partial C}{\partial t} + \mu S \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}\right) dt + \sigma S \frac{\partial C}{\partial S} dW
$$

## Hedging Portfolio Dynamics

To make the option risk-free, set up a hedging portfolio with the proportion $\Delta$, representing the number of shares of the underlying asset to hold, and $M$, representing the amount invested in the risk-free asset. The dynamics of this portfolio can be given by:

$$
dM =  r M dt = dC - \Delta dS
$$

Substituting the dynamics of $dS$ into $dM$, we get:

$$
r M dt = dC - \Delta (\mu S dt + \sigma S dW)
$$

## Delta Hedging Strategy

Now, equating the two expressions for $dC$, we can determine the hedging strategy $\Delta$. 

$$
\Delta (\mu S dt + \sigma S dW) + r M dt = \left(\frac{\partial C}{\partial t} + \mu S \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}\right) dt + \sigma S \frac{\partial C}{\partial S} dW
$$

We can construct a risk-free portfolio hedging agains uncertainty. Setting coefficients of $dW$ terms equal, we get:

$$
\Delta = \frac{\partial C}{\partial S}
$$

With this $\Delta$ the terms in $dW$ will cancel out:

$$
(\frac{\partial C}{\partial S}\mu S + r M)dt = \left(\frac{\partial C}{\partial t} + \mu S \frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2}\right) dt
$$

If we choose $M = C -\frac{\partial C}{\partial S}S$ from the definition of the hedging portfolio, then the $dS$ terms in $dC$ will cancel out.

Thus, we obtain the Black-Scholes partial differential equation (PDE) for a European call option:

$$
\frac{\partial C}{\partial t} + rS\frac{\partial C}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} - rC = 0
$$

## PDE Solution

This PDE has the well-known closed-form solution for a European call option:

$$
C(S, t) = S_0 N(d_1) - Ke^{-r(T - t)} N(d_2)
$$

where $d_1$ and $d_2$ are derived from the following equations:

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)(T - t)}{\sigma \sqrt{T - t}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T - t}
$$

Here, $N$ is the cumulative distribution function of the standard normal distribution. This is the Black-Scholes formula for a European call option.
