# coding=utf-8

import grpc
import time
from concurrent import futures
import sys
import index.trajectory_index

sys.path.append("..")
# sys.path

from grpc_service.index_proto import index_pb2, index_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = "localhost"
_PORT = "8080"


class TrajectoryIndex(index_pb2_grpc.TrajectoryIndexServicer):
    def __init__(self):
        self.trajectory_index = index.trajectory_index.TrajectoryIndex()

    def get_intersection_trajectory_ids(self, request, context):
        mbr = (request.min_lon, request.min_lat, request.max_lon, request.max_lat)
        id_list = self.trajectory_index.get_intersection_trajectory_ids(
            min_lon=request.min_lon,
            min_lat=request.min_lat,
            max_lon=request.max_lon,
            max_lat=request.max_lat,
        )
        print("\n[IntersectionRequest] mbr = ", mbr)
        print("[IntersectionResponse] id_list = ", id_list)
        return index_pb2.IntersectionResponse(ids=id_list)

    def get_trajectory_by_ids(self, request, context):
        id_list = request.id_list
        trajectory_list = self.trajectory_index.get_trajectory_by_ids(id_list=id_list)
        trajectory_list_response = []
        for i in range(len(trajectory_list)):
            point_list = []
            for j in range(len(trajectory_list[i])):
                # Todo: 后续需要加上滞留时间
                lon = str(trajectory_list[i].at[j, "lon"])
                lat = str(trajectory_list[i].at[j, "lat"])
                time_stamp = str(trajectory_list[i].at[j, "time_stamp"])
                point = index_pb2.Point(lon=lon, lat=lat, time_stamp=time_stamp)
                point_list.append(point)
            trajectory_list_response.append(
                index_pb2.Trajectory(id=id_list[i], point_list=point_list)
            )
        print("\n[IndexRequest] ids = ", id_list)
        print("[IndexResponse] len = ", len(trajectory_list_response))
        return index_pb2.IndexResponse(trajectory_list=trajectory_list_response)


def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    index_pb2_grpc.add_TrajectoryIndexServicer_to_server(TrajectoryIndex(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ":" + _PORT)
    grpcServer.start()
    print("\ngrpc Server start:", _HOST + ":" + _PORT)
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


if __name__ == "__main__":
    serve()
