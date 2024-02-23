from unittest import TestCase, main
from tlib.core.cfg import Cfg


class CfgTest(TestCase):

    def test_cfgload(self):
        cfg = Cfg('local_ut')
        self.assertEqual(cfg.get_conf_value_as_str(
            'test_cfg_strattrib'), 'test')
        self.assertEqual(cfg.get_conf_value_as_int('test_cfg_intattrib'), 10)
        self.assertEqual(len(cfg.get_api_conf_value('WEATHER', 'APIKEY')), 30)


if __name__ == "__main__":
    main()
