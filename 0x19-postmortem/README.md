# Postmortem: Server Outage Due to Misconfigured Firewall Rules

## Issue Summary

**Duration**: March 14, 2024, 14:00 - 17:30 UTC

**Impact**: The entire web application was down, affecting all users. Approximately 100% of the user base experienced complete service unavailability, leading to disruptions in access to the online platform and potential data loss during the outage period.

**Root Cause**: The root cause was a misconfiguration in the firewall rules that inadvertently blocked HTTP and HTTPS traffic to the web servers, rendering the application inaccessible.

## Timeline

- **14:00 UTC** - Issue detected via monitoring alert indicating that all web servers were unreachable.
- **14:05 UTC** - Network engineer noticed the issue and verified it through direct server access attempts.
- **14:10 UTC** - Initial investigation focused on the web server configuration and possible application-level issues.
- **14:30 UTC** - Misleading assumption that the problem was related to recent application updates. Rolled back updates, but the issue persisted.
- **15:00 UTC** - Escalated to the network team after initial debugging yielded no results.
- **15:30 UTC** - Network team started analyzing firewall configurations and network traffic logs.
- **16:00 UTC** - Discovered incorrect firewall rules blocking incoming HTTP and HTTPS traffic.
- **16:15 UTC** - Corrected the firewall rules and initiated testing to confirm resolution.
- **17:00 UTC** - Full functionality of the web application restored.
- **17:30 UTC** - Monitoring confirmed stable service, and the incident was declared resolved.

## Root Cause and Resolution

**Root Cause**:
The issue was caused by a recent update to the firewall rules intended to enhance security by restricting access to non-essential services. However, a misconfiguration in these rules inadvertently blocked HTTP (port 80) and HTTPS (port 443) traffic, making the web application inaccessible to all users.

**Resolution**:
The resolution involved identifying and correcting the misconfigured firewall rules. The network team carefully reviewed the changes made to the firewall and pinpointed the incorrect rules. They then modified the firewall settings to allow traffic on ports 80 and 443, restoring access to the web servers. Following the correction, extensive testing was conducted to ensure no other services were impacted and to confirm the stability of the web application.

## Corrective and Preventative Measures

**Improvements/Fixes**:
1. **Firewall Rule Review Process**:
   - Implement a thorough review process for firewall rule changes, including peer reviews and automated validation checks.

2. **Enhanced Monitoring**:
   - Enhance monitoring to include specific checks for firewall rules and port accessibility to detect similar issues more quickly.

3. **Change Management**:
   - Introduce stricter change management protocols to ensure all network changes are well-documented and reviewed before implementation.

**Tasks to Address the Issue**:
1. **Patch Firewall Configuration**:
   - Correct the misconfigured firewall rules to ensure proper traffic flow on required ports.

2. **Implement Monitoring**:
   - Set up monitoring for HTTP/HTTPS ports to alert on any unintentional blockages or traffic drops.

3. **Review and Document Firewall Changes**:
   - Conduct a full review of recent firewall changes and document all findings and corrective actions.

4. **Develop Automated Tests**:
   - Create automated tests to validate firewall rules before and after changes are applied.

5. **Training**:
   - Provide additional training for network and security teams on the importance of careful firewall rule management and validation.

6. **Post-Incident Review**:
   - Conduct a post-incident review meeting to discuss the outage, gather feedback, and identify further improvements.

By implementing these measures, we aim to prevent similar incidents in the future and ensure a more robust and reliable network infrastructure.
