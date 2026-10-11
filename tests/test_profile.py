import unittest

from scripts.validate_profile import ROOT, contrast_ratio, validate


class ProfileValidationTest(unittest.TestCase):
    def test_repository_assets_and_links(self):
        self.assertEqual([], validate(ROOT, online=False))

    def test_contrast_calculation(self):
        self.assertGreater(contrast_ratio("#111820", "#F4EEE3"), 7)


if __name__ == "__main__":
    unittest.main()
