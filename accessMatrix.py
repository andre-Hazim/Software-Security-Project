class AccessControlMatrix:
    def __init__(self):
        # Initialize an empty matrix
        self.matrix = {}

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

    def display_matrix(self):
        # Display the access control matrix
        header = ["Roles/Resources"] + list(self.matrix[list(self.matrix.keys())[0]].keys())
        rows = [header]

        for role, resource_access in self.matrix.items():
            row = [role] + [access for access in resource_access.values()]
            rows.append(row)

        for row in rows:
            print("|".join(row))


# Example Usage:

# Create an instance of the AccessControlMatrix
acm = AccessControlMatrix()

# Add roles to the matrix
roles = ["Client", "Premium Client", "Financial Planner", "Financial Advisor",
         "Investment Analyst", "Technical Support", "Teller", "Compliance Officer"]

for role in roles:
    acm.add_role(role)

# Add resources and access rights to each role
resources = ["AB", "CI", "RAC", "IP", "FAD", "IAD", "PCI", "MMI", "DT, IT", "System"]

access_rights = [
    ["R-", "---", "---", "R-", "R-", "---", "---", "---", "---", "---"],
    ["R-", "---", "---", "RW", "R-", "R-", "---", "---", "---", "---"],
    ["R-", "---", "---", "RW", "---", "---", "R-", "R-", "---", "---"],
    ["R-", "---", "---", "RW", "RW", "---", "R-", "---", "---", "---"],
    ["R-", "---", "---", "RW", "---", "RW", "R-", "R-", "R-", "---"],
    ["---", "R--", "--X", "---", "---", "---", "---", "---", "---", "---"],
    ["R-", "---", "---", "R-", "---", "---", "---", "---", "---", "R-X"],
    ["R-", "---", "---", "R-", "---", "---", "---", "---", "---", "---"]
]

for role, access in zip(roles, access_rights):
    for resource, rights in zip(resources, access):
        acm.add_resource(role, resource, rights)

# Display the access control matrix
acm.display_matrix()
print(acm.get_access("Client","AB"))