git clone git@github.com:Aninhas190/udacity-devops-CI-CD.git
cd udacity-devops-CI-CD
git pull
make all
az webapp up -n udacity-project-2
# in the end you should see the following website deployed https://udacity-project-2.azurewebsites.net