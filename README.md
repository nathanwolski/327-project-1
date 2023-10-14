# 327-project-1
#To run this project you will need docker installed as well as the latest version of python
#To start you need to navigate to the project directory and cd into each image folder and build the respective image with commands:

#cd broadcast-receiver

#docker build -t broadcast-receiver-image .

#cd broadcast-sender

#docker build -t broadcast-sender-image .

#cd multicast-receiver

#docker build -t multicast-receiver-image .

#cd multicast-receiver

#docker build -t multicast-receiver-image .

#Then after biuilding the images, you will be able to run the composition file with the command:

#docker-compose up

#Our logging function for the required output kept running into bugs, but the network deploys just fine, our python logging function executes but it not able to get any statistics
#To quit, Either crtl C in the terminal where your running the code or click the stop button in docker desktop
