chmod 600 .travis/prod.pem
ssh-add .travis/prod.pem
echo -e "Host ec2-54-88-185-174.compute-1.amazonaws.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
git remote add prod ec2-54-88-185-174.compute-1.amazonaws.com:/home/ubuntu/titlematch_api.git
git push prod master
