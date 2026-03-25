{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "20cc2207",
   "metadata": {},
   "source": [
    "### Experiência 2 - Emulador Industrial"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ecddff4",
   "metadata": {},
   "source": [
    "##### Item 1\n",
    "Utilizando os resultados desenvolvidos na Experiencia 1, explique porque no controle em malha fechada do emulador industrial iremos adotar sempre $G_{pf}(s) = 1$. Já no controle em malha aberta $G_{pf}(s) = k_{pf}s/(1+0,01s)$."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd5624f8",
   "metadata": {},
   "source": [
    "#### Sem perturbação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5258e4e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "706b0f45",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b795ec00",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.24"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "66853839",
   "metadata": {},
   "source": [
    "#### Com perturbação"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5843aeaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.12"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a8b1cd76",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.18"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4ef68f7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "kp = 0.24"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac29b152",
   "metadata": {},
   "source": [
    "*Explique o que ocorre com comportamento do sistema quando o ganho proporcional $k_p$ e progressivamente aumentado, notando de que forma o comportamento regulador do sistema frente ao distúrbio na carga é afetado pelo aumento do ganho de malha produzido por $k_p$.*"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ee964514",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
