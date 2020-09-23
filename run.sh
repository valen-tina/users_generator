 #!/bin/bash
 docker build -t generate_advocates .
 # docker run --rm -it --entrypoint=sh generate_advocates
 docker run --rm -it -v ${PWD}/:/output/ generate_advocates