# encoding = utf-8
import os,sys,yaml


class BaseAnalyze:

    def analyze_data_yml(self, file_name):
        # 本地运行
        # 获取当前项目文件目录
        path = os.getcwd()
        # print(path)
        dirs = path.split("/Demo/")
        # print(dirs)
        path_one = dirs[0]
        # print(path_one)
        # 拼凑文件路径
        file_path = path_one + os.sep + "data" + os.sep + file_name  # 适用于pytest运行

        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.FullLoader)


    def analyze_key(self, func_name, file_name):
        dict = self.analyze_data_yml(file_name)
        dict_key = dict[func_name]
        return dict_key

    def analyze_write_data_into_yml(self, file_name, data):
        # 本地运行
        # 获取当前项目文件目录
        path = os.getcwd()
        # print(path)
        dirs = path.split("/Demo/")
        # print(dirs)
        path_one = dirs[0]
        # print(path_one)
        # 拼凑文件路径
        file_path = path_one + os.sep + "data" + os.sep + file_name  # 适用于pytest运行


        with open(file_path, "a", encoding="utf-8") as f:
            return yaml.dump(data, f)
