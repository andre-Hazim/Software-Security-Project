from enum import Enum
class Rights(Enum):
    
    CLIENT = ["R--", "---", "---", "R--", "R--", "---", "---", "---", "---", "---"]
    PREMIUM_CLIENT = ["R--", "---", "---", "RW-", "R--", "R--", "---", "---", "---", "---"]
    FINANCIAL_PLANNER =["R--", "---", "---", "RW-", "---", "---", "R--", "R--", "---", "---"]
    FINANCIAL_ADVISOR = ["R--", "---", "---", "RW-", "RW-", "---", "R--", "---", "---", "---"]
    INVESTMENT_ANALYST = ["R--", "---", "---", "RW-", "---", "RW-", "R--", "R--", "R--", "---"]
    TECHNICAL_SUPPORT = ["---", "R--", "--X", "---", "---", "---", "---", "---", "---", "---"]
    TELLER = ["R--", "---", "---", "R--", "---", "---", "---", "---", "---", "R-X"]
    COMPLIANCE_OFFICER = ["R--", "---", "---", "R--", "---", "---", "---", "---", "---", "---"]

class Roles(Enum):
    CLIENT = "Client"
    PREMIUM_CLIENT = "Premium Client"
    FINANCIAL_PLANNER = "Financial Planner"
    FINANCIAL_ADVISOR = "Financial Advisor"
    INVESTMENT_ANALYST = "Investment Analyst"
    TECHNICAL_SUPPORT = "Technical Support"
    TELLER = "Teller"
    COMPLIANCE_OFFICER = "Compliance Officer"

class Resources(Enum):
    AB = "AB"
    CI = "CI"
    RAC = "RAC"
    IP = "IP"
    FAD = "FAD"
    IAD = "IAD"
    PCI = "PCI"
    MMI = "MMI"
    DT_IT = "DT, IT"
    SYSTEM = "System" 



class AccessControlMatrix:
    def __init__(self):
        # Initialize an empty matrix
        self.matrix = {}
        
        for role,rights in zip(Roles,Rights):
            self.add_role(role)
            for resource ,right in zip(Resources, rights.value):
                self.add_resource(role,resource,right)

    def add_role(self, role):
        # Add a new role to the matrix
        self.matrix[role] = {}

    def add_resource(self, role, resource, access):
        # Add a resource with its access rights to a role
        if role not in self.matrix:
            raise ValueError(f"Role '{role}' does not exist in the matrix.")
        
        self.matrix[role][resource] = access

    def get_access(self, role, resource):
        # Get the access rights for a specific role and resource
        if role in self.matrix and resource in self.matrix[role]:
            return self.matrix[role][resource]
        else:
            return None
        
    def get_role(self, rolename):
        if rolename in self.matrix:
            return self.matrix[rolename]
        else:
            return None

    def __str__(self):
        # Display the access control matrix
        header ={ }
        
        
        for roles in self.matrix:
            header[roles] =  self.matrix[roles]

        s="Roles/Resources : {}\n".format([r.value for r in Resources])
        for key, value in self.matrix.items():
            
            s+= "{} : {}\n".format(key.name,list(value.values()))
        
        return s

# Example Usage:

# Create an instance of the AccessControlMatrix
acm = AccessControlMatrix()
print (acm)