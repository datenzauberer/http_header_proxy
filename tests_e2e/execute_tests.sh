#!/usr/bin/env bash


#################################################################################
# Description
#################################################################################
# http_header_proxy (SystemUnderTest)
# http://127.0.0.1:8100
#########################################
# test_service (TestService)
# http://127.0.0.1:5000/memory/http_header_proxy
#########################################
# TestController : Creates the load

# Start TestService
python service_show_memory.py &
pid_ser=$!
# Start http_header_proxy
pushd ..
cargo run &
pid_sut=$!
popd

# Execute Tests
rm memory_usage.txt
num_of_tests=10000
for ((i = 1; i <= num_of_tests; i++)); do
    echo DATAPOINT: $i
    # this calls the service via proxy (to check if memory is increased)
    http_proxy=http://127.0.0.1:8100 curl -v http://127.0.0.1:5000/large_response
    # thist checks if the memory was increased
    curl http://127.0.0.1:5000/memory/http_header_proxy | grep memory_usage_mb >> memory_usage.txt
done

# Show
cat memory_usage.txt
