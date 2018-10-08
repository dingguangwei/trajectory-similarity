该项目是对轨迹相似度算法DTW改进算法的实现，暂时取名为IDC-DTW(Improved distance calculation DTW)
其中，
similarity_computation中是改进算法的相关实现
util中是一些画图和读数据之类的工具api的实现

编译proto使用命令：
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./grpc_service/index_proto/index.proto

