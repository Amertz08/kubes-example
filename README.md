# Kubes Example

Project to learn Kubernetes

- Workloads
  - Pods
    - Lifecycle
      - Container states
        - has hook API to trigger events to run at certain points in the container's lifecycle
      - Restart policy
        - used to deal with container failures
        - side car containers ignore pod level policy
      - Pod Readiness
        - Can specify extra conditions to evaluate Pod for readiness
        - Only ready when all containers in Pod are ready and all conditions in `readinessGates` are `True`
      - Container Probe
        - Diagnostic performed periodically on the container
        - types
          - livenessProbe: whether the container is running
          - readinessProbe: whether the container is ready to respond to requests
          - startupProbe: whether the application within the container is started
    - Init Container
      - run prior to app container
      - always run to completion
      - must complete successfully before next one starts
      - If they fail the whole Pod fails
      - Can run less secure code/tools instead of being ran in the app container
      - Should be idempotent
    - Sidecar Containers
      - ran prior to the app container
      - will remain running when app container starts
      - defined in `initContainers` but with `restartPolicy: Always`
      - have own lifecycle independent of app containers
        - can be started, stopped and restarted independently of app containers
        - can be updated or scaled independently of app containers
      - can interact with app container given they share the same network
    - Ephemeral Containers
      - Used to debug or inspect a hard to reproduce issue
      - has no lifecycle guarantees
      - started via a specific 
    - Disruptions
    - Pod Quality of Service Classes
    - User Namespaces
    - Downward API
  - Workload Management
  - Autoscaling Workloads
  - Managing Workloads
- Services, Load Balancing and Networking
  - Service
  - Ingress
  - Ingress Controllers
  - Gateway API
  - Endpoint Slices
  - Network Policies
  - DNS for Services and Pods
  - IPv4/IPv6 dual-stack
  - Topology Aware Routing
  - Service ClusterIP allocation
  - Service Internal Traffic Policy


## questions
- labels use cases?


## general todos
- Kube
  - DNS service
  - dashboard UI
  - parallel jobs
  - deployment/service with a message queue
- FastAPI
  - deployments
  - https
- Diagramming
- Locust load testing in Kube
