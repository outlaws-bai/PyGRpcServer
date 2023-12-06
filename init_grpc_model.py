# coding: utf-8
# @author: outlaws-bai
# @date: 2023/12/06 20:43:20
# @description:
import os
from pathlib import Path

filename = "Counter.proto"
source_filepath = (
    Path(__file__).parent.parent.parent.parent.parent.parent.parent / "proto" / filename
)
dest_filepath = Path(__file__).parent / "proto" / filename

# read proto file into .
with open(source_filepath, "r", encoding="utf-8") as f_source, open(
    dest_filepath, "w", encoding="utf-8"
) as f_dest:
    f_dest.write(f_source.read())

# init proto model
# cmd: python -m grpc_tools.protoc -I./proto --python_out=grpc_models --grpc_python_out=grpc_models proto/Counter.proto

os.system(
    "python -m grpc_tools.protoc -I./proto --python_out=grpc_models --grpc_python_out=grpc_models proto/Counter.proto"
)
