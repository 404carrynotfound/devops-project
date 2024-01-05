# Dev Ops Project

## Used technologies

- Python
- pytest
- Flask
- Flack8
- MyPy
- SonarCloud
- Snyk
- Docker
- Trivy
- Git leaks
- GitHub Actions
- Minikube

## Project Structure

### Main Pipeline

Runs on every push or pull request against the master branch

![image](https://github.com/404carrynotfound/devops-project/assets/37977687/215d965f-3b14-440a-999e-3e54928836b8)

#### Jobs

- Static code analysis
- Test execution
- Building and pushing Docker image (Steps from here are skipped if it's a Pull request)
- Scanning the image
- Deploying to minikube

### Test Pipeline
Runs only in pull requests

![image](https://github.com/404carrynotfound/devops-project/assets/37977687/59b62a59-0b59-4e5c-9791-9ae5534c190e)

#### Jobs
- Test execution

### Git leaks Pipeline
This pipeline runs after pushing against master, on a pull request, and is scheduled every Mon-Fri

![image](https://github.com/404carrynotfound/devops-project/assets/37977687/4416342c-28ec-440a-9e42-e94bac0643a7)

#### Jobs
- Checks for exposed secrets

## Local deployment

### Requirements

- Docker
- Minikube
- Published Docker Image

### How to run

### Start Minikube

```
minikube start
```

### Apply k8s file

```
kubectl apply -f k8s
```

### Verify that configuration is applied

#### Check pods

```
kubectl get pods --all-namespaces
```

### Check node port

```
kubectl get services api-port
```

### Expose the app
```
minikube service api-port
```
