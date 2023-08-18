import yaml
import os
import json


def read_yaml(path_to_yaml: str) -> dict:
    """
    Reads a yaml file
    :param path_to_yaml: [str] [path to yaml file]
    :return: [dict]
    """
    with open(path_to_yaml, mode='r') as yaml_file:
        content = yaml.safe_load(yaml_file)
        
    return content


def create_directory(dirs: list):
    """
    Creates directories if not exists
    :param dirs: [list] [list of directories or folders to be created]
    :return: None
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok = True)
        print(f"directory is created at {dir_path}")


def save_local_df(data, data_path, index_status = False):
    data.to_csv(data_path, index = index_status)
    print(f"data is saved at {data_path}")


def save_reports(report: dict, report_path: str, indentation = 4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent = indentation)
    
    print(f"reports are saved at {report_path}")