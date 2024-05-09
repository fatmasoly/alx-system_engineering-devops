Postmortem: Web Stack Outage Incident

Issue Summary:

Duration: May 5, 2024, 14:00 UTC to May 6, 2024, 03:00 UTC
Impact: A complete outage of our e-commerce platform, affecting all users attempting to access the website. Approximately 75% of our users were unable to browse or make purchases during the incident.
Root Cause: An unanticipated surge in traffic overwhelmed our load balancer, causing it to enter a degraded state and reject incoming connections.
Timeline:

May 5, 2024, 14:00 UTC: Issue detected as a sudden spike in error rates on our monitoring dashboard.
14:05 UTC: Engineering team alerted via automated monitoring system.
14:15 UTC: Initial investigation focused on the database layer due to recent schema changes.
15:30 UTC: Database layer deemed healthy; attention shifted to load balancer configuration.
17:00 UTC: Misleading investigation into potential DDoS attack due to unusual traffic patterns.
19:00 UTC: Incident escalated to senior engineering management for additional resources and expertise.
21:30 UTC: Load balancer logs reviewed, revealing excessive connection attempts from legitimate user traffic.
May 6, 2024, 02:00 UTC: Load balancer configuration adjusted to increase connection limit and optimize resource allocation.
03:00 UTC: Service fully restored; traffic normalized.
Root Cause and Resolution:

Root Cause: The load balancer was configured with inadequate connection limits, leading to a bottleneck under heavy load.
Resolution: Load balancer configuration settings were adjusted to accommodate higher traffic volumes. Additionally, monitoring thresholds were refined to provide early warnings of potential capacity issues.
Corrective and Preventative Measures:

Improvements/Fixes:
Implement automated scaling for load balancer resources to handle traffic spikes dynamically.
Enhance DDoS protection mechanisms to differentiate legitimate traffic from malicious attacks more effectively.
Conduct regular load testing to validate system resilience under peak loads.
Tasks to Address the Issue:
Update load balancer configuration to allow for a higher number of concurrent connections.
Deploy automated scaling policies for load balancer resources based on traffic patterns.
Enhance monitoring alerts to detect and mitigate potential DDoS attacks more efficiently.
Schedule regular load tests to simulate peak traffic scenarios and validate system performance.
Conduct a post-mortem review with the engineering team to analyze incident response and identify areas for improvement in the escalation process.
By implementing these corrective measures and addressing the identified tasks, we aim to minimize the risk of similar incidents in the future and ensure the continued reliability and availability of our e-commerce platform for our users.
