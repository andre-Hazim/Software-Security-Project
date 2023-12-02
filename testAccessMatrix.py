import unittest
from accessMatrix import *
class TestAccessControlMatrix(unittest.TestCase):

    def setUp(self):
        self.acm = AccessControlMatrix()

    def test_add_role(self):
        self.assertIn(Roles.CLIENT, self.acm.matrix)

    def generic_access_test(self, role_enum, resource_enum, expected_access):
        access = self.acm.get_access(role_enum, resource_enum.value)
        self.assertEqual(access, expected_access)

    def test_get_access_client(self):
        expected_rights = Rights.CLIENT.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.CLIENT, resource_enum, expected_rights.pop(0))

    def test_get_access_premium_client(self):
        expected_rights = Rights.PREMIUM_CLIENT.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.PREMIUM_CLIENT, resource_enum, expected_rights.pop(0))

    def test_get_access_financial_planner(self):
        expected_rights = Rights.FINANCIAL_PLANNER.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.FINANCIAL_PLANNER, resource_enum, expected_rights.pop(0))

    def test_get_access_financial_advisor(self):
        expected_rights = Rights.FINANCIAL_ADVISOR.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.FINANCIAL_ADVISOR, resource_enum, expected_rights.pop(0))

    def test_get_access_investment_analyst(self):
        expected_rights = Rights.INVESTMENT_ANALYST.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.INVESTMENT_ANALYST, resource_enum, expected_rights.pop(0))

    def test_get_access_technical_support(self):
        expected_rights = Rights.TECHNICAL_SUPPORT.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.TECHNICAL_SUPPORT, resource_enum, expected_rights.pop(0))

    def test_get_access_teller(self):
        expected_rights = Rights.TELLER.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.TELLER, resource_enum, expected_rights.pop(0))

    def test_get_access_compliance_officer(self):
        expected_rights = Rights.COMPLIANCE_OFFICER.value
        for resource_enum in Resources:
            self.generic_access_test(Roles.COMPLIANCE_OFFICER, resource_enum, expected_rights.pop(0))


    def generic_role_test(self, role_enum, expected_rights):
        role = self.acm.get_role(role_enum)
        self.assertEqual(list(role.values()), expected_rights.value)

    def test_get_role_client(self):
        self.generic_role_test(Roles.CLIENT, Rights.CLIENT)

    def test_get_role_premium_client(self):
        self.generic_role_test(Roles.PREMIUM_CLIENT, Rights.PREMIUM_CLIENT)

    def test_get_role_financial_planner(self):
        self.generic_role_test(Roles.FINANCIAL_PLANNER, Rights.FINANCIAL_PLANNER)

    def test_get_role_financial_advisor(self):
        self.generic_role_test(Roles.FINANCIAL_ADVISOR, Rights.FINANCIAL_ADVISOR)

    def test_get_role_investment_analyst(self):
        self.generic_role_test(Roles.INVESTMENT_ANALYST, Rights.INVESTMENT_ANALYST)

    def test_get_role_technical_support(self):
        self.generic_role_test(Roles.TECHNICAL_SUPPORT, Rights.TECHNICAL_SUPPORT)

    def test_get_role_teller(self):
        self.generic_role_test(Roles.TELLER, Rights.TELLER)

    def test_get_role_compliance_officer(self):
        self.generic_role_test(Roles.COMPLIANCE_OFFICER, Rights.COMPLIANCE_OFFICER)

    


if __name__ == '__main__':
    unittest.main()
