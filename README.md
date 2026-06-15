**Note:** We're more interested in how you approach the problem and implement your solution than in you finding a “correct” answer to the question.

## The task - Deploying & migrating a workload

Your challenge is to build the cloud infrastructure and execute a two-stage application deployment migration strategy for a web workload. 

Initially, you will configure the host machine to serve the application natively. Following that baseline, you are required to transition the application away from the host OS layers by authoring a custom container packaging layout.

You can use whichever cloud service you feel appropriate to host it. Our cloud platform is Huawei, so that would be a preference, but AWS or Azure is fine. The web app has been provided. See build instructions below.

### Requirements:
* **Stage 1 (Native Baseline):** Provision your cloud Virtual Server within a private environment with explicit ingress and egress control. Configure the runtime environment manually and run the provided application natively on the host instance.
* **Stage 2 (Container Migration):** Note that all container files have been stripped from this repository. You must write an optimized multi-stage `Dockerfile` from scratch, package the application, and re-deploy it to your host environment as a containerized workload.
* Create a readable and maintainable solution that is easy to understand by an audience of your peers.
* **Stage 3** Add object storage to the infra and configure it with the application.
* **Stage 4** Discover docker-compose and try to implement it with an appropriate approach to handel environment variables during the build phase of your container.

If you have time, consider implementing these features:
* A load balancing solution
* Automating the deployment

We appreciate that some of these requirements are open to interpretation. Feel free to implement the requirements how you think is best. 

If you have any questions then please don’t hesitate in reaching out to the team at Qantara.

Good luck!


## Build instructions
We have provided a React app that represents a production ready containerised workload. It gets some data from an API (not a live call) and presents the data to a web page.


### Working with the repository locally

| Command | Outcome |
|:---|:---|
| `npm install` | Setup the initial dependencies - run once |
| `npm start` | Start the code locally in debug build |
| `npm run build` | If you want to create a production build |