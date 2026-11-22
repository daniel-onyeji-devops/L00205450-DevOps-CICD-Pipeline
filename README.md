
# DevOps CI/CD Pipeline Project

**Student:** Daniel Onyeji  
**Student ID:** L00205450  
**Course:** Postgraduate Diploma in Computing in DevOps  
**College:** Atlantic Technological University (ATU)

## About This Project

For this assignment, I created a simple Python web application and built a CI/CD pipeline around it.

The aim was to understand how developers can automate testing, security checks and application builds instead of doing everything manually.

I used GitHub to store my code, GitHub Actions to automate the pipeline, Docker to package the application and Kubernetes to run it locally.

I also set up basic monitoring and logging to check how the application was performing.

## Tools I Used

- **Python:** To create the web application.
- **Git and GitHub:** To manage and store my code.
- **GitHub Actions:** To run automated tests, security checks and Docker builds.
- **Bandit:** To check my Python code for security issues.
- **Docker:** To package the application into a container.
- **Minikube:** To run a local Kubernetes cluster.
- **Kubernetes:** To deploy and manage the application.
- **Metrics Server:** To monitor CPU and memory usage.
- **VS Code:** To write and manage the project files.

## How My Application Works

I created a simple Python web application using Python's built-in HTTP server.

When I open the application in a browser, it displays:

**Welcome to my DevOps CI/CD Pipeline!**

The application runs on port 8000.

Although the website is simple, the main focus of this assignment was building the automated pipeline and learning how the different DevOps tools work together.

## My CI/CD Pipeline

I created a GitHub Actions workflow in:

`.github/workflows/ci.yml`

Whenever I push changes to GitHub, the workflow automatically:

1. Downloads the latest project code.
2. Sets up Python.
3. Runs the automated Python tests.
4. Installs and runs Bandit to check for security issues.
5. Builds the Docker image.

If the tests or security scan fail, the workflow stops before completing the Docker build.

This helps identify problems early.

## Automated Testing

I created a test file called `test_app.py`.

The test checks that my application returns a successful HTTP response and displays the expected welcome message.

I tested the application locally before adding the test to GitHub Actions.

To run the tests manually:

```bash
python3 -m unittest discover -v
```

## Security Scanning

I used Bandit to scan my Python code for potential security problems.

During the assignment, Bandit identified an issue because my application was listening on all network interfaces using `0.0.0.0`.

The security scan failed, which showed that the automated check was working.

I corrected the application so it uses `127.0.0.1` by default and allows the host address to be configured when needed.

After making the change, I pushed the code to GitHub again.

The next security scan passed with no issues identified.

This was one of the useful lessons I learned because I could see how a security check can prevent insecure code from progressing through the pipeline.

## Docker Containerisation

I created a Dockerfile to package the Python application.

This allows the application to run inside a container with its own Python environment.

To build the image:

```bash
docker build -t devops-python-app .
```

To run it locally:

```bash
docker run -d --name devops-web -p 8000:8000 devops-python-app
```

The application can then be accessed at:

http://localhost:8000

I also added the Docker build command to GitHub Actions so the image is built automatically after the tests and security scan pass.

## Kubernetes Deployment

After testing the application with Docker, I deployed it to a local Kubernetes cluster using Minikube.

I created the cluster using:

```bash
minikube start --driver=docker
```

I then loaded the Docker image into Minikube:

```bash
minikube image load devops-python-app:latest
```

I created a Kubernetes deployment configuration in:

`k8s/deployment.yaml`

To deploy the application:

```bash
kubectl apply -f k8s/deployment.yaml
```

To check the application:

```bash
kubectl get pods
kubectl get deployments
```

The application successfully ran in Kubernetes with one Pod available.

To access it through Kubernetes:

```bash
kubectl port-forward deployment/devops-web 8081:8000
```

The website can then be opened at:

http://localhost:8081

For this assignment, Kubernetes deployment was carried out locally. The GitHub Actions workflow automates testing, security scanning and building the Docker image, but it does not yet automatically deploy the application to Minikube.

## Monitoring and Logging

I used Kubernetes commands to check the application's status and view its logs.

To view the application logs:

```bash
kubectl logs deployment/devops-web
```

The logs confirmed that the application was running on port 8000.

I also enabled Metrics Server in Minikube:

```bash
minikube addons enable metrics-server
```

To check CPU and memory usage:

```bash
kubectl top pods
```

This allowed me to see how much CPU and memory the application was using.

This provides basic resource monitoring, although I have not implemented a full Prometheus and Grafana monitoring system.

## Challenges I Faced

I encountered a few problems while working on this project.

The first was the Bandit security scan failing because the application was listening on all network interfaces. I fixed this by changing how the application handles its host address.

I also had problems getting Docker recognised in my Mac terminal. Docker was installed, but the terminal could not find the command. I corrected the terminal PATH and was then able to use Docker.

Another issue happened during Kubernetes deployment. The Pod initially showed `ImagePullBackOff` because Kubernetes was trying to download an image instead of using the image already loaded into Minikube. I changed the image pull policy to resolve the problem.

I also had some difficulty saving my Kubernetes YAML file in the correct folder. After correcting the file location and formatting, I successfully applied the configuration.

These challenges helped me understand the importance of checking logs, reading error messages and troubleshooting problems one step at a time.

## What I Learned

This assignment helped me understand how different DevOps tools work together.

Before starting, I had some experience with Git, Docker and Kubernetes, but building the project helped me see how they fit into a CI/CD workflow.

I learned how to automate testing, detect security issues, build Docker images, deploy an application to Kubernetes and check its resource usage.

I also learned that getting a pipeline to work involves troubleshooting and making improvements along the way.

## Future Improvements

If I continued developing this project, I would:

- Automate the Kubernetes deployment as part of the CI/CD process.
- Add more automated tests.
- Use Trivy to scan the Docker image for vulnerabilities.
- Add Prometheus and Grafana for more detailed monitoring.
- Push Docker images to a container registry.
- Improve the security and reliability of the application.

Overall, this project gave me practical experience building and troubleshooting a DevOps CI/CD pipeline.
