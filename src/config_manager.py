import os
import yaml
import sys
import argparse

class ConfigManager:
    def __init__(self, yaml_file=None):
        self.config = {}
        if yaml_file:
            self.load_yaml(yaml_file)
        self.load_env_vars()
        self.load_cli_args()

    def load_yaml(self, yaml_file):
        with open(yaml_file, 'r') as file:
            self.config.update(yaml.safe_load(file))

    def load_env_vars(self):
        for key in os.environ:
            self.config[key] = os.environ[key]

    def load_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--config', help='Path to the configuration YAML file')
        args = parser.parse_args()
        if args.config:
            self.load_yaml(args.config)

    def get(self, key, default=None):
        return self.config.get(key, default)