# Overview

This repo utilizes the Instagram tech stack in order to create a webpage (locally hosted) that a user can upload images to. Those images are stored using PostgreSQL which can be accessed at a later time. Since this repo follows Instagram's tech stack, it is separated into two sections: production and development which each have their own Dockerfiles to run. This distinction allows us to troubleshoot more easily in the development phase and to ensure our production phase goes well.

![Example GIF](flask_on_docker.gif)

# Build Instructions
We will separate the build instructions into two phases.

**Phase 1**

To begin to use this service, we must enable portforwarding.

We can bring down any open containers to ensure there are no issues with pre-existing containers. To do so, we can run the following line:

```
$ docker compose down -v
```

The `-v` brings down associated volumes.

Then, we can run the lines:

```
$ docker compose -f docker-compose.prod.yml up -d --build
$ docker compose -f docker-compose.prod.yml exec web python manage.py create_db
```
This first line starts up the service so that we can begin using it. Note, that the `-d` stands for "daemon" which runs the service in the background. 

The second line creates the table to store images for the service.

To ensure everything is working, you can try running `docker ps -a` to see if there are processes, otherwise, proceed with the next step!

**Phase 2**

Now that the service is up and running, load up a web browser page, Firefox is recommended. Then search: "localhost:YOURPORT/upload" where "YOURPORT" is the port you used for portforwarding.

From here, press "Browse" and upload your image of choice, then press "Upload". Then, to view your image, head over to "localhost:YOURPORT/media/YOURFILENAME" where "YOURPORT" is the port you used for portforwarding and "YOURFILENAME" is the name of your file.

You should now see your image! If you do not, ensure that you are correctly portforwarding and using the correct file name (potentially including the file extension!)
