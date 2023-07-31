#### Make sure python version 3.6+
python3/python --version

#### Make sure pip or pip3 available in the env
pip3/pip --version

#### Install python dependencies
pip3/pip install grpcio grpcio-tools delta-sharing pyinstaller

#### If needed Generate GRPC from proto 
python3 -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. .\publisher.proto

## Create executables (Linux and Mac)
- pyinstaller PluginDeltaSharing.spec
- Copy all files from dist/PluginDeltaSharing to make the zip

## Create executables (Windows)
- pyinstaller .\PluginDeltaSharing-Windows.spec
- cd PluginRunner
- dotnet publish -c Release -r win-x64
- Copy all files from dist\PluginDeltaSharing and PluginRunner\bin\Release\net6.0\win-x64\publish to make the zip
