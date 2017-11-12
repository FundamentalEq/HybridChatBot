#!/bin/bash

echo "Parsing Data"
python parser.py

echo "Creating Index"
python index.py

echo "Calculating Tf-idfs vectors"
python cal_tf-idf.py
