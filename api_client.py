import delta_sharing


class ApiClient:

    def __init__(self, profile_file):
        # print(f'start init api client:{profile_file}, type:{type(profile_file)}')
        self.profile_file: str = profile_file
        try:
            self.sharing_client = delta_sharing.SharingClient(profile_file)
        except Exception as e:
            pass
            # print(f'error in create:{str(e)}-- {e.__class__.__name__}')
        # print('end init api client')

    @property
    def is_reachable(self):
        shares = []
        try:
            shares = self.sharing_client.list_shares()
        except Exception as e:
            # print(f'error in reachable test:{str(e)}')
            pass
        finally:
            return True if len(shares) > 0 else False