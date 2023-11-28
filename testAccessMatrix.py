import unittest
from accessMatrix import *
class TestAccessControlMatrix(unittest.TestCase):

    def setUp(self):
        self.acm = AccessControlMatrix()

    def test_add_role(self):
        self.assertIn(Roles.CLIENT, self.acm.matrix)

    def test_get_access(self):        
        self.assertEqual(self.acm.get_access(Roles.CLIENT, Resources.AB.value), "R--")

    def test_get_role(self):
        role = self.acm.get_role(Roles.CLIENT)
        print(list(role.values()))
        print(Rights.CLIENT.value)
        self.assertEqual(list(role.values()), Rights.CLIENT.value)  # Include all resources

    


if __name__ == '__main__':
    unittest.main()
