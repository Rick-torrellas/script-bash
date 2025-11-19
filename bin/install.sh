#!/bin/bash
apt-get update && \
    apt-get install -y bash git procps && \
    rm -rf /var/lib/apt/lists/*