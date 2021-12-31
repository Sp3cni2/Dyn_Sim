import numpy as np
from dataclasses import dataclass,field


def engine_init(P_0, k, Mol, T_chamber, P_chamber, Q, ratio=None, Ae=None, Pe=None):

    Rs = 8314.463

    if Pe is None:
        raise ValueError("external pressure can't be None")

    Pt = np.multiply(P_chamber,np.power(1 + np.divide(k-1,2),np.divide(-k,k-1)))
    Tt = np.divide(T_chamber,1 + np.divide(k-1,2))

    At = np.multiply(
                     np.divide(
                               Q,
                               Pt),
                     np.sqrt(
                             np.divide(
                                        np.multiply(Rs,Tt),
                                        np.multiply(Mol,k))))

    if Ae is None:
        if ratio is not None:
            Ae = ratio * At
        else:
            Mach_sq = np.multiply(np.divide(2,k-1),np.power(np.divide(P_chamber,P_0),np.divide(k-1,k))-1)
            Mach = np.sqrt(Mach_sq)
            Ae = np.divide(At,Mach)*np.power(np.divide(1 + np.divide(k-1,2)*Mach_sq ,np.divide(k+1,2)),np.divide(k+1,2*k - 2))

    c = np.multiply(
                    np.multiply(
                                np.divide(
                                            2*k,
                                            k-1),
                                            np.divide(
                                                      np.multiply(
                                                                  Rs,
                                                                  T_chamber),
                                                      Mol)),
                                1 - np.power(
                                             np.divide(
                                                       Pe,
                                                       P_chamber),
                                             np.divide(
                                                       k-1,
                                                       k)))
    Ve = np.sqrt(c)
    return Ve, Ae


def produce_thrust(Ve, Ae, Pe, P_chamber, Q):
    return Ve*Q + Ae*(P_chamber - Pe)
