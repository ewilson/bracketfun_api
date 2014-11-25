#!/usr/bin/env sh
chmod 600 .travis/prod.pem
ssh-add .travis/prod.pem
echo "\nHost production\n\tHostName ec2-54-88-185-174.compute-1.amazonaws.com\n\tStrictHostKeyChecking no\n\tUser ubuntu\n\tIdentityFile .travis/prod.pem\n" >> ~/.ssh/config
cat ~/.ssh/config
git remote add prod production:/home/ubuntu/titlematch_api.git
git push prod master
exit

