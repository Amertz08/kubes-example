# Kubes Example

Project to learn Kubernetes. [Narrative doc](NARRATIVE.md) that outlines some of my thought process. My [notes](NOTES.md)
document is my notes I am taking as I read the Kubernetes documentation.

## general todos
- Kube
  - [ ] DNS service
  - [ ] dashboard UI
  - [ ] parallel jobs
  - [ ] deployment/service with a message queue
  - [ ] do a rolling deployment 
  - Helm
    - [x] basic API chart
    - [ ] cron chart
    - [ ] db chart
    - Should they all be one chart?
    - Should I just use postgres chart?
- FastAPI
  - deployments
  - [ ] https
  - [ ] Can run locally and connect to DB in K8 cluster
  - [ ] Can run in local cluster and connect to DB
- Diagramming
- Locust load testing in Kube
- GHA
  - [ ] build and push image
  - [ ] automated tests
  - tox to define 'future' runtime?
- ETL
  - fake data generator
- RabbitMQ
  - deploy
  - write consuming service
- Terraform
  - [ ] VPC
  - [ ] EKS Cluster
  - [ ] ECR Repo
  - [ ] S3 Bucket
  - [ ] Service Account IAM Role
