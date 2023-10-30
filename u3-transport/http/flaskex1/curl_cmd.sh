#!/bin/sh
curl -d"score=70" -X POST http://localhost:5000/scores
curl http://localhost:5000/lookup?index=0
curl http://localhost:5000/avg/

# On cmdline (not powershell)
# curl -X POST -H "Content-Type: application/json" -d " { ""score"" : ""73"" }" http://localhost:5000/scores
# curl -X POST  -d "score=70" http://localhost:5000/scores
#curl -L   -H "Accept: application/vnd.github+json" https://api.github.com/repos/usc-ee250-fall2023/lectures/activity?activity_type=push