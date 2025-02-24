#!/usr/bin/env python3
import os
import yaml


rootDir = 'apis'
for dirName, subdirList, fileList in os.walk(rootDir):
    
    if 'env.yaml' in fileList:
        print(f"Found env.yaml in {dirName}")
        with open(os.path.join(dirName, 'env.yaml'), 'r') as stream:
            try:
                env_yaml = yaml.safe_load(stream)
                print(f"Loaded env.yaml in {dirName}")
            except yaml.YAMLError as exc:
                print(exc)
            
            print(env_yaml)

            try:
                os.system(f"cd {dirName} && rm -rf .env Pipfile")
            except:
                print("Could not remove .env and Pipfile")
            
            packages_to_install = ' '.join(env_yaml['packages']) + ' git+https://github.com/gladiaio/gladia-api-utils.git'
            os.system(f"cd {dirName} && echo Y | pipenv --python {env_yaml['python']['version']}")
            os.system(f"cd {dirName} && pipenv run pip install {packages_to_install}")
