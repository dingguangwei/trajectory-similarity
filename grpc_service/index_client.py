# coding=utf-8

import grpc
import sys
import pandas as pd

sys.path.append('..')

from grpc_service.index_proto import index_pb2, index_pb2_grpc

_HOST = 'localhost'
_PORT = '8080'


def get_client():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = index_pb2_grpc.TrajectoryIndexStub(channel=conn)
    return client


def get_intersection_trajectory_ids(min_lon, min_lat, max_lon, max_lat):
    client = get_client()
    response = client.get_intersection_trajectory_ids(index_pb2.IntersectionRequest(min_lon=min_lon, min_lat=min_lat, max_lon=max_lon, max_lat=max_lat))
    return response.id_list


def get_trajectory_by_ids(id_list):
    client = get_client()
    response = client.get_trajectory_by_ids(index_pb2.IndexRequest(id_list=id_list))
    trajectory_list = []
    for item in response.trajectory_list:
        data = []
        for point in item.point_list:
            lon = round(float(point.lon), 6)
            lat = round(float(point.lat), 6)
            time_stamp = point.time_stamp
            data.append([lon, lat, time_stamp])
        trajectory = pd.DataFrame(data=data, columns=['lon', 'lat', 'time_stamp'])
        trajectory_list.append(trajectory)
    return trajectory_list

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = index_pb2_grpc.TrajectoryIndexStub(channel=conn)
    # response = client.get_intersection_trajectory_ids(index_pb2.IntersectionRequest(min_lat=30, min_lon=110, max_lat=50, max_lon=120))
    # print("received: len = ", len(response.ids), '  response:', str(response.id_list))
    response = client.get_trajectory_by_ids(index_pb2.IndexRequest(id_list=[20081024020959]))
    print(response.trajectory_list[0].point_list)


if __name__ == '__main__':
    traj = get_trajectory_by_ids(id_list=[20081024020959, 20081023025304])[0]
    print(traj)
