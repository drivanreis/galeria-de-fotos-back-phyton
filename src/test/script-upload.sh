#!/bin/bash

# ../backend/src/test/script-upload.sh

#curl -X POST http://189.71.214.150:3001/upload \
#  -F "photo=@./a_lenda_do_tesouro_perdido_1_2004_720p.png"

curl -X POST http://localhost:3001/upload \
  -F "photo=@./a_lenda_do_tesouro_perdido_1_2004_720p.png"
