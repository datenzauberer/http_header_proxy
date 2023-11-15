
# Description

A TestService shows 
The http_header_proxy (SystemUnderTest) is tested by calling the TestService.

http_header_proxy (SystemUnderTest)
<http://127.0.0.1:8100>

test_service (TestService)
<http://127.0.0.1:5000/memory/http_header_proxy>

# Setup Python venv (for TestService)

```sh
python3 -m venv venv
. venv/bin/activate
pip install Flask psutil
```

# Execute Test

(Be sure that you're in the venv: ~. venv/bin/activate~)

```sh
cd tests_e2e
./execute_tests.sh
```
