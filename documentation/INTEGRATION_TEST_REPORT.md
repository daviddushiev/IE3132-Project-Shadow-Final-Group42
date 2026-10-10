# Project Shadow — Integration Test Report

**Module:** IE3132 — Penetration Testing  
**Project:** Project Shadow: The Vanished Research  
**Group:** Group 42  
**Member:** Aluthpatabendige S K (Senuda)  
**Responsibility:** Integration, Testing and Validation  
**Test Date:** 10 October 2026  
**Test Environment:** Ubuntu Linux, Docker, rCTF

---

## 1. Introduction

Project Shadow is a cybersecurity Capture the Flag (CTF) environment containing seven challenges covering reconnaissance, web security, cryptography, digital forensics, networking, reverse engineering, and Linux security.

Integration testing was performed to verify the availability and connectivity of the main services supporting the CTF environment.

A Python-based Integration Health Checker, `project_shadow_health_check.py`, was used to automate six service connectivity tests.

## 2. Objectives

The objectives of the integration tests were to:

- Verify that the rCTF platform is accessible.
- Confirm that the PS-01 public website and research archive respond correctly.
- Verify the availability of the PS-02 research portal.
- Confirm DNS resolution for the research archive subdomain.
- Check connectivity to the PS-07 SSH service.
- Produce automated PASS/FAIL results for service availability.

## 3. Test Environment

| Component | Configuration |
|---|---|
| Operating system | Ubuntu Linux |
| CTF platform | rCTF |
| Container platform | Docker |
| Automation language | Python 3 |
| HTTP testing | urllib.request |
| DNS testing | dig through subprocess |
| TCP connectivity testing | Python socket |
| Target environment | Local, isolated academic CTF deployment |

## 4. Automated Test Cases

| Test ID | Test Description | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| T01 | Check rCTF platform on port 8080 | HTTP 200 | HTTP 200 | PASS |
| T02 | Check PS-01 public website using `solace.test` | HTTP 200 | HTTP 200 | PASS |
| T03 | Check research archive using `archive.solace.test` | HTTP 200 | HTTP 200 | PASS |
| T04 | Check PS-02 research portal on port 8081 | HTTP 200 | HTTP 200 | PASS |
| T05 | Resolve `archive.solace.test` using DNS port 1053 | IP address `127.0.0.1` | `127.0.0.1` | PASS |
| T06 | Check PS-07 SSH connectivity on port 2227 | TCP connection succeeds | Connection successful | PASS |

## 5. Automation Implementation

The integration health checker uses three Python libraries:

**urllib.request:** Sends HTTP requests to the rCTF platform and web challenge services. The PS-01 tests include HTTP Host headers to access the correct Nginx virtual hosts.

**subprocess:** Executes a DNS lookup using `dig` and verifies that the expected IP address is returned.

**socket:** Establishes a TCP connection to the PS-07 SSH port to verify service reachability without attempting authentication.

Each function returns `True` when its test succeeds and `False` when it fails. The main function counts the results and produces a summary. The script also returns a nonzero exit status when one or more checks fail.

## 6. Test Execution

The script was executed using:

```bash
python3 project_shadow_health_check.py
```

The results were saved using:

```bash
python3 project_shadow_health_check.py | tee health_check_results.txt
```

### Recorded Test Results

```text
PROJECT SHADOW - INTEGRATION HEALTH CHECK
-----------------------------------------
[PASS] T01 - rCTF platform is accessible
[PASS] T02 - PS-01 website is accessible
[PASS] T03 - Research archive is accessible
[PASS] T04 - PS-02 research portal is accessible
[PASS] T05 - DNS resolves archive.solace.test
[PASS] T06 - PS-07 SSH port 2227 is reachable

========== TEST SUMMARY ==========
Total Tests : 6
Passed      : 6
Failed      : 0
Overall     : ALL TESTS PASSED
```

## 7. Test Summary

| Metric | Result |
|---|---|
| Total automated tests | 6 |
| Passed | 6 |
| Failed | 0 |
| Pass rate | 100% |

All six automated connectivity tests passed during the recorded execution.

## 8. Scope and Limitations

The health checker performs read-only service connectivity checks.

It does not modify Docker containers, challenge source code, rCTF accounts, competition scores, or database records.

The automated tests do not independently verify:

- Complete functionality of all seven challenges.
- Valid or invalid flag submission behavior.
- Security vulnerabilities or exploitation results.
- Correctness of cryptographic or forensic solutions.
- SSH authentication or privilege escalation.
- Integration of the hint portal with rCTF scoring.

Separate manual evidence was collected for challenge registration, hint display, positive and negative flag validation, and scoreboard behavior.

## 9. Conclusion

The Project Shadow Integration Health Checker successfully verified six essential service connectivity requirements.

The results confirm that the tested rCTF, website, DNS, and SSH endpoints were accessible at the time of execution.

The automated checks complement the manual challenge-validation screenshots and provide a repeatable method for identifying service availability issues.

## 10. Supporting Evidence

- `project_shadow_health_check.py` — Python integration-testing source code.
- `health_check_results.txt` — Recorded automated test output.
- `01-senuda-seven-challenges.png` — Challenge registration.
- `02-senuda-docker-services.png` — Docker service status.
- `03-senuda-service-connectivity.png` — Manual connectivity tests.
- `04-senuda-hint-system.png` — Hint interface validation.
- `05-senuda-valid-flag-accepted.png` — Valid flag evidence.
- `06-senuda-invalid-flag-rejected.png` — Invalid flag rejection.
- `07-senuda-scoreboard-validation.png` — Scoreboard verification.
- `08-senuda-automation-code-part1.png` to `part4.png` — Automation code.
- `09-senuda-automation-test-results.png` — Automated execution results.

---

**End of Integration Test Report**
