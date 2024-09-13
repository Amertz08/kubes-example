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
    - Sidecar Containers
    - Ephemeral Containers
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
