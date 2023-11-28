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
    CLIENT = "basic client"
    PREMIUM_CLIENT = "premium client"
    FINANCIAL_PLANNER = "financial planner"
    FINANCIAL_ADVISOR = "financial advisor"
    INVESTMENT_ANALYST = "investment analyst"
    TECHNICAL_SUPPORT = "technical support"
    TELLER = "teller"
    COMPLIANCE_OFFICER = "compliance officer"

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
            self._add_role(role)
            for resource ,right in zip(Resources, rights.value):
                self._add_resource(role,resource.name,right)

    def _add_role(self, role):
        # Add a new role to the matrix
        self.matrix[role] = {}

    def _add_resource(self, role, resource:Resources, access):
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
acm = AccessControlMatrix()
#print(acm.get_role(Roles.CLIENT))
