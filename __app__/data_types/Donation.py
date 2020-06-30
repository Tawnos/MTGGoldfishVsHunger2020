class Donation:
    def __init__(self,
                 donation_id,
                 user_id,
                 organization_id,
                 organization_name,
                 amount,
                 metadata,
                 created_at):
        self.donation_id = donation_id
        self.user_id = user_id
        self.organization_id = organization_id
        self.organization_name = organization_name
        self.amount = amount
        self.metadata = metadata
        self.created_at = created_at
