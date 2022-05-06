# Overview

This is the second project for Udacity DevOps. The goal is to run Continuous Integration and Continuous Development in Azure and Azure Pipelines.
This repo contains the files for Udacity Azure Cloud DevOps Nanodegree Program. 
Project "Building a CI/CD Pipeline".

## Project Plan
The project plan can be found in the sheets folder in docs google and the trello board created for this.

* https://trello.com/b/X9Wfqrcz/udacity-course
* https://docs.google.com/spreadsheets/d/1vmCY1sG8x81wtb36xSQL2vj8_DPgoONN09IhrmFtAnI/edit?usp=sharing

## Instructions

<img width="438" alt="image" src="https://user-images.githubusercontent.com/57501664/166905527-99cf0260-1907-43de-ae4a-a752318335a7.png">

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service
   After connecting your Azure App Service with your Azure Pipelines you should be able to see in the deployment Center of Azure Portal the following:
  *  <img width="815" alt="image" src="https://user-images.githubusercontent.com/57501664/166949888-febc49c7-4247-4377-ad13-4cecf5045a08.png">


* Project cloned into Azure Cloud Shell
  * Open Azure Cloud Shell
  * <img width="154" alt="image" src="https://user-images.githubusercontent.com/57501664/166905682-74cc8a43-964c-4b96-8b96-84c976854428.png">
  * Generate a ssh keygen and connect to your github ssh keys
  * run in your terminal ```ssh-keygen``` press enter
  * <img width="362" alt="image" src="https://user-images.githubusercontent.com/57501664/166905963-b71e1471-aacc-4a0d-9a45-6b5d31d9428f.png">
  * run in your terminal ```cat $path to where your public key is save ends in /id_rsa.pub.
  * copy result, go to your github settings -> SSH and GPG keys -> click New SSH Key  paste and give title to key
  * git clone the project in your <img width="347" alt="image" src="https://user-images.githubusercontent.com/57501664/166906384-26b930a1-65ef-4a7c-bd64-a08c5ba6569f.png">
  * cd to your project and create virtual environment:
    run ```python3 -m venv ~/.yourRepo```
    run ```source ~/.your-repo/bin/activate```
    
* Passing tests that are displayed after running the `make all` command from the `Makefile` && output of a test run
  ![tests-passing-make-all](https://user-images.githubusercontent.com/57501664/166949552-bd46698c-0c9e-44cc-ac9e-cf1a52b06099.png)
  
* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).


* Running Azure App Service from Azure Pipelines automatic deployment
  <img width="946" alt="image" src="https://user-images.githubusercontent.com/57501664/166953281-f042a19d-2c9e-4eba-94df-10523232bc66.png">  

* Successful prediction from deployed flask app in Azure Cloud Shell. 
  * run ```chmod 744 ./make_predic_azure_app.sh``` to add permissions to your Cloud shell
  * run ```./make_predict_azure_app.sh``` and you should see the following:

   ```bash
   ana@Azure:~/udacity-devops-CI-CD$ ./make_predict_azure_app.sh 
   Port: 443
   {"prediction":[20.35373177134412]}
   ```

* Output of streamed log files from deployed application
   Go to https://<your-app-name>.scm.azurewebsites.net/api/logs/docker which for me was https://udacity-project-2.scm.azurewebsites.net/api/logs/docker to see the streamed log files

   > ```[{"machineName":"pl0sdlwk0007KP_default","lastUpdated":"2022-05-05T14:50:41.8337636Z","size":747158,"href":"https://udacity-project-2.scm.azurewebsites.net/api/vfs/LogFiles/2022_05_05_pl0sdlwk0007KP_default_docker.log","path":"/home/LogFiles/2022_05_05_pl0sdlwk0007KP_default_docker.log"},{"machineName":"pl0sdlwk0007KP","lastUpdated":"2022-05-05T14:50:41.8337636Z","size":127138,"href":"https://udacity-project-2.scm.azurewebsites.net/api/vfs/LogFiles/2022_05_05_pl0sdlwk0007KP_docker.log","path":"/home/LogFiles/2022_05_05_pl0sdlwk0007KP_docker.log"}]```

## Ehancements

Add more features to predict more prices of houses in Boston given different filter options.

## Demo 

<TODO: Add link Screencast on YouTube>



# Screenshot passing GitHub Actions

![image](https://user-images.githubusercontent.com/57501664/166148782-a0994ae2-6357-4f79-b936-108ab00d3df3.png)

