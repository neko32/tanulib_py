from unittest import TestCase, main
from tlib.stats import BayesTheorem
from tlib.datautil import round_floor


class BayesTest(TestCase):

    def test_bayes_formula(self):
        male_diabetic = 0.18
        male_overweight = 0.33
        overweighted_male_become_diabetes = 0.10

        b = BayesTheorem(
            P_A_given_B=None,
            P_B_given_A=overweighted_male_become_diabetes,
            P_A=male_overweight,
            P_B=male_diabetic
        )
        self.assertEqual(round_floor(b.calc_posterior_probablity(), 2), 0.10)
        self.assertEqual(b.calc_casuality(), overweighted_male_become_diabetes)


if __name__ == "__main__":
    main()
