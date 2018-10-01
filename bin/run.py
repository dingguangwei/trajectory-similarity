from util.file_reader import file_reader
from similarity_computation.idc_DTW import dtw
from conf.config_reader import get_root_path

if __name__ == '__main__':
    root_path = get_root_path()

    reader = file_reader(root_path=root_path)
    trajectory_list = reader.get_some_trajectory([5, 7])

    result = dtw(trajectory_list[0], trajectory_list[1])
    print('result : ', result)
