class HealthCheckAction:
    def execute(self, system_id):
        print(f'Checking system {system_id}...')
        return 'OK'
