# Generate .py file from proto file - skip this step as grpc tools will generate the .py
protoc --proto_path=. --python_out=. .\publisher.proto

#install grpcio grpcio-tools
pip3 install grpcio
pip3 install grpcio-tools

# Generate grpc and proto
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. .\publisher.proto


# Make sure python version 3.6+
python3/python --version

# Make sure pip or pip3 available in the env
pip3/pip --version

# Install python dependencies
pip3/pip install grpcio grpcio-tools delta-sharing pyinstaller

# Create executables
pyinstaller .\PluginDeltaSharing.spec
