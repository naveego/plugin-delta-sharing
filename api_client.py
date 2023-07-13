import delta_sharing


class ApiClient:

    def __init__(self, profile_file):
        self.profile_file: str = profile_file
        self.sharing_client = delta_sharing.SharingClient(profile_file)

    @property
    def is_reachable(self):
        shares = []
        try:
            shares = self.sharing_client.list_shares()
        except Exception as e:
            pass
        finally:
            return True if len(shares) > 0 else False