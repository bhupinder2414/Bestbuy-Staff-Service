# BestBuy Staff-Service Microservice

## Overview
The **staff-service** microservice is designed to manage staff information within Best Buy's internal system. This service provides CRUD operations (Create, Read, Update, Delete) for managing staff data, including fields such as ID, name, position, department, email, and phone number. The service is implemented using REST APIs and adheres to the 12-factor application principles to ensure scalability and maintainability in a cloud-native environment.

## Features
- **Create**: Add new staff records.
- **Read**: Retrieve staff details by ID or list all staff members.
- **Update**: Modify existing staff records.
- **Delete**: Remove staff records by ID.

## Technologies Used
- Programming Language: **[Your Chosen Language]** (e.g., Node.js, Java, Python)
- Framework: **[Your Chosen Framework]** (e.g., Express.js, Flask, Spring Boot)
- In-memory data store (No database)
- Docker for containerization
- Azure Kubernetes Service (AKS) for deployment

## Endpoints
- `POST /staff`: Create a new staff record.
- `GET /staff`: Retrieve all staff records.
- `GET /staff/{id}`: Retrieve a staff record by ID.
- `PUT /staff/{id}`: Update a staff record by ID.
- `DELETE /staff/{id}`: Delete a staff record by ID.

## Setup Instructions

### Prerequisites:
1. Install Docker and Docker Compose.
2. Azure account with Kubernetes setup or access to Azure Kubernetes Service (AKS).
3. GitHub account with repository access for CI/CD setup.

### Running the Service Locally:
1. Clone the repository:
    ```bash
    git clone https://github.com/bhupinder2414/Bestbuy-Staff-Service
    cd Bestbuy-Staff-Service
    ```

2. Run the service:
    - Install dependencies:
        ```bash
        [install command depending on language, e.g.for python pip install -r requirements.txt]
        ```
    - Start the service:
        ```bash
        [command to start service, e.g., python app.py]
        ```
    The service will be available at `http://l27.0.0.1:5000`.

### Docker Setup:
1. Build Docker image:
    ```bash
    docker build -t bestbuystaffservice .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 bhup0006/bestbuystaffservice:Latest
    ```

3. Push the Docker image to Docker Hub:
    ```bash
    docker tag bestbuystaffservice:Latest bhup0006/bestbuystaffservice:Latest
    docker push  bhup0006/bestbuystaffservice:Latest
    ```

### Deploying to Azure Kubernetes Service (AKS):
1. Create AKS cluster using Azure Portal or CLI.
2. Use the `staff-service.yaml` to deploy the service to the AKS cluster:
    ```bash
    kubectl apply -f staff-service.yaml
    ```

### CI/CD Setup:
1. Add a `.github/workflows/ci_cd.yaml` file for the pipeline.
2. The pipeline will:
    - Build the service.
    - Run unit tests.
    - Deploy the service to AKS upon successful tests.

## Completed Tasks
- Developed the **staff-service** microservice with CRUD operations.
- Containerized the service using **Docker**.
- Deployed the service to **Azure Kubernetes Service (AKS)**.
- Configured and tested the **CI/CD pipeline** using **GitHub Actions**.

## Issues Encountered
- Encountered a few configuration issues while setting up the CI/CD pipeline due to network access restrictions in Azure.
- Resolved by reviewing and modifying the Kubernetes deployment YAML file for proper network configurations.

## Repository Information
- **GitHub Repo**: [GitHub Repo URL](https://github.com/bhupinder2414/Bestbuy-Staff-Service)
- **Docker Image**: [Link to Docker Image on Docker Hub](https://hub.docker.com/repository/docker/bhup0006/bestbuystaffservice/general)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
