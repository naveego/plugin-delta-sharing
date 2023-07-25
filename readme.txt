# Generate .py file from proto file - skip this step as grpc tools will generate the .py
protoc --proto_path=. --python_out=. .\publisher.proto

#install grpcio grpcio-tools
pip3 install grpcio
pip3 install grpcio-tools

# Generate grpc and proto
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. .\publisher.proto


# Make sure python version 3.6+
python --version
# or
python3 --version

# Make sure pip or pip3 available in the env
pip --version
pip3 --version

# Install python dependencies
# If pip is available
pip install grpcio grpcio-tools delta-sharing pyinstaller

# If pip3 is available
pip3 install grpcio grpcio-tools delta-sharing pyinstaller



# Create executables
pyinstaller .\PluginDeltaSharing.spec
