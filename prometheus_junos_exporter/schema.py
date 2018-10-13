from voluptuous import Schema, Required, Any

import yaml


class Configuration(object):
    def __init__(self):
        self.schema = Schema({
            Required(str): {
                Required('device'): Any('junos', 'arubaos', 'ios'),
                Required('auth'): {
                    Required('method'): Any('password', 'ssh_key'),
                    'username': str,
                    Any('password', 'ssh_key', 'proxy'): str,
                    'port': int,
                    Any('http_secure', 'verify'): bool
                },
                Required('metrics'): [
                    # Junos Metrics
                    'ospf',
                    'optics',
                    'interface',
                    'interface_specifics',
                    'igmp',
                    'environment',
                    'bgp',
                    # ArubaOS Metrics
                    'clients',
                    'cpu',
                    'memory',
                    'system information',
                    'access point statistics',
                    'access point state']
            }
        })

    def validate(self, config):
        try:
            self.schema(config)
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    config = Configuration()
    with open('prometheus_junos_exporter/config/config.yml', 'r') as file:
        data = yaml.load(file.read())
    config.validate(data)