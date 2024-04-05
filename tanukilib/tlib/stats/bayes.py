from typing import Optional


class BayesTheorem:
    """
    Represents Bayes Theorem Formula.
    Also provides calculation of P(A|B) and P(B|A)
    """

    def __init__(
            self,
            P_A_given_B: Optional[float],
            P_B_given_A: Optional[float],
            P_A: float,
            P_B: float):
        self.P_A_given_B = P_A_given_B
        self.P_B_given_A = P_B_given_A
        self.P_A = P_A
        self.P_B = P_B

    def calc_posterior_probablity(self) -> float:
        """Calculate P(A|B). Aka posterior probablity"""
        if self.P_B_given_A is None:
            raise AssertionError("P(B|A) needs to be set")
        print(f"P(A|B) = {self.P_B_given_A}*{self.P_A}/{self.P_B}")
        self.P_A_given_B = (self.P_B_given_A * self.P_A) / self.P_B
        return self.P_A_given_B

    def calc_casuality(self) -> float:
        """Calculate P(B|A). Aka casulality"""
        if self.P_A_given_B is None:
            raise AssertionError("P(A|B) needs to be set")
        print(f"P(B|A) = {self.P_A_given_B}*{self.P_B}/{self.P_A}")
        self.P_B_given_A = (self.P_A_given_B * self.P_B) / self.P_A
        return self.P_B_given_A
