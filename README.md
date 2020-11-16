# blockchain_data_conversion_eventlog

1. set up the farbric test-network based on the instructions on https://hyperledger-fabric.readthedocs.io/en/release-2.2/test_network.html:

    1.1 Navigate to the test network directory by using the following command: cd fabric-samples/test-network
    1.2 From the directory bring up the network by using the command: ./network.sh up
    1.3 create a channel: ./network.sh createChannel
    1.4 replace the /fabric-samples/chaincode/fabcar/javascript/lib/fabcar.js with the fabcar.js found in the chaincode folder of this repository
    1.5 deploy the chaincode using: ./network.sh deployCC -l javascript
    1.6 run the following commands to set the configs:
        export PATH=${PWD}/../bin:$PATH
        export FABRIC_CFG_PATH=$PWD/../config/
        # Environment variables for Org1

        export CORE_PEER_TLS_ENABLED=true
        export CORE_PEER_LOCALMSPID="Org1MSP"
        export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
        export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
        export CORE_PEER_ADDRESS=localhost:7051

2. Now network is ready for sending transactinos, run the "generate_data.sh" script from the scripts/fabric folder
3. run the command: "peer channel getinfo -c mychannel", to get the total number of blocks 
4. in the scripts write_block.sh , and convert_json.sh change number_blocks to the blockchain height, given from the last command
5. in the convert_json.sh script, give the directory in which you want to save the block data, after the --output flag, as in:
  --output /Users/myuser/Desktop/data/
6. run  write_block.sh
7. run convert_json.sh
8. in the convert.ipnypb jupyter notebook, set the addresses: set "csv_path" for the address of the output file, set "file_dir" as the directory in which you used      to save the block files in convert_json.sh
9. use the csv file obtained from the script in Prom.
