import numpy as np

from ode_functions.gating import f, m_inf


def sodium_current(v, m, parameters, h=1, hs=1):
    """
    Model sodium current

    :param v: Membrane potential
    :param m: m gating variable
    :param parameters: Model parameters
    :param h: Optional h gating variable
    :param hs: Optional hs gating variable
    :return: Sodium current
    """

    g_na = parameters['g_na']
    e_na = parameters['e_na']
    return g_na * (v - e_na) * (m ** 3) * h * hs


def total_current(v, h, parameters, hs=1):
    """
    Model total current

    :param v: Membrane potential
    :param h: Optional h gating variable
    :param parameters: Model parameters
    :param hs: Optional hs gating variable
    :return: Sodium current
    """

    g_na = parameters['g_na']
    g_k = parameters['g_k']
    g_l = parameters['g_l']
    e_na = parameters['e_na']
    e_k = parameters['e_k']
    e_l = parameters['e_l']

    return - (g_l * (v - e_l)) - (g_na * (m_inf(v) ** 3) * h * hs * (v - e_na)) - (
            g_k * (f(h[-1]) ** 3) * (v - e_k))  # todo: integrate with sodium_current()


def nmda_current(v, g_syn, e_syn, mg=1.4):
    """
    Current from an nmda synapse
    :param v: Membrane potential
    :param g_syn: Synaptic conductance
    :param e_syn: Reversal potential of synapse
    :param mg: Model mg parameter: todo: check paper for what this is
    :return: nmda current
    """

    return (g_syn * (v - e_syn)) / (1 + (mg / 3.57) * np.exp(0.062 * v))


def ampa_current(v, g_syn, e_syn):
    """
    Current from an ampa synapse
    :param v: Membrane potential
    :param g_syn: Synaptic conductance
    :param e_syn: Reversal potential of synapse
    :return: ampa current
    """

    return g_syn * (v - e_syn)
