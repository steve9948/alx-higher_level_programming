#!/bin/bash
# sends a POST request to the URL, and set 2 variables and displays the body of the response
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
