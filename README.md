# PROJECT SHADOW — THE VANISHED RESEARCH

### IE3132 – Penetration Testing | Group 42

**Project Type:** Multi-Stage Capture the Flag (CTF) Security Challenge  
**Platform:** Ubuntu Linux, Docker, rCTF  
**Repository:** IE3132-Project-Shadow-Final-Group42  
**Challenge Count:** 7 interconnected challenges  
**Flag Format:** `SHADOW{lowercase_words_with_underscores}`

---

## 1. Project Overview

**Project Shadow: The Vanished Research** is an educational Capture the Flag (CTF) environment developed for the IE3132 Penetration Testing module.

The project simulates a fictional cybersecurity investigation into the disappearance of confidential research belonging to Solace Dynamics. Participants act as security investigators, examining a series of interconnected digital clues to uncover what happened to the missing research.

The challenge environment combines seven practical cybersecurity disciplines, including reconnaissance, web application security, cryptography, digital forensics, network traffic analysis, reverse engineering, and Linux privilege escalation.

The challenges are connected through a common storyline, where information discovered in one stage assists participants in progressing through subsequent stages.

The CTF is designed to provide hands-on experience in security analysis, vulnerability identification, evidence examination, and problem-solving within an isolated academic environment.

## 2. Project Objectives

The main objectives of Project Shadow are:

- Design and implement seven interconnected cybersecurity challenges.
- Demonstrate practical penetration testing and digital forensic techniques.
- Build and configure an isolated Linux-based CTF environment.
- Integrate challenge delivery and scoring using rCTF.
- Provide a structured participant experience through hints and supporting materials.
- Implement and test challenge services using Docker, Linux services, and supporting scripts.
- Demonstrate individual development contributions through GitHub branches, commits, screenshots, scripts, and technical documentation.

## 3. Challenge Overview

| Stage | Challenge | Security Domain | Main Objective |
|---|---|---|---|
| PS-01 | The Forgotten Website | OSINT / Reconnaissance | Discover hidden web resources and investigate document metadata |
| PS-02 | The Research Portal | Web Application Security | Identify and exploit an intentionally vulnerable authentication mechanism |
| PS-03 | The Attacker's Message | Cryptography | Identify and decrypt a classical cipher |
| PS-04 | The Deleted Evidence | Digital Forensics | Recover deleted evidence from a filesystem image |
| PS-05 | The Hidden Communication | Network Forensics | Examine a packet capture to identify suspicious communication |
| PS-06 | The Encoded Research | Reverse Engineering | Analyze an executable and recover information from encrypted data |
| PS-07 | The Final Access | Linux Privilege Escalation | Identify an insecure Linux privilege configuration and retrieve the final flag |

Each challenge contains an individual flag following the Project Shadow flag format.

### PS-01 — The Forgotten Website

**Category:** OSINT and Web Reconnaissance

Participants investigate a fictional organization's website to identify previously overlooked web resources.

The stage incorporates local DNS resolution, virtual hosts, a hidden archive, and a research memo containing relevant metadata.

**Skills assessed:**
- DNS enumeration
- Web reconnaissance
- Subdomain discovery
- Document metadata analysis

**Implementation:** Docker, Nginx, dnsmasq, Python, HTML

### PS-02 — The Research Portal

**Category:** Web Application Security

Participants investigate a research portal containing an intentionally vulnerable authentication mechanism.

The challenge demonstrates how unsafe SQL query construction can lead to authentication bypass.

**Skills assessed:**
- Web application testing
- SQL injection identification
- Authentication security
- Secure coding awareness

**Implementation:** Node.js, Express, SQLite, Docker

**Security note:** The vulnerable implementation is intentional and must only run in an authorized, isolated training environment.

### PS-03 — The Attacker's Message

**Category:** Cryptography

Participants encounter an encrypted message that contains an important clue related to the investigation.

They must identify the cipher, determine the appropriate key, and recover the plaintext.

**Skills assessed:**
- Classical cipher identification
- Vigenère cipher analysis
- Key identification
- Decryption and verification

**Implementation:** Python, text-based challenge artifacts, local web hosting

### PS-04 — The Deleted Evidence

**Category:** Digital Forensics

Participants receive a forensic disk image containing evidence associated with the fictional security incident.

They investigate the filesystem and recover information that is no longer accessible through normal file browsing.

**Skills assessed:**
- Filesystem analysis
- Deleted-file recovery
- Disk image examination
- Digital evidence interpretation

**Implementation:** Linux filesystem image, Sleuth Kit, forensic utilities

**Primary artifact:** `ps04/public/evidence.dd`

### PS-05 — The Hidden Communication

**Category:** Network Forensics

Participants analyze a packet capture containing network activity associated with suspicious communication.

They must identify relevant traffic, investigate transferred objects, and reconstruct information from network evidence.

**Skills assessed:**
- Packet capture analysis
- Wireshark filtering
- HTTP traffic examination
- Network artifact recovery
- Suspicious communication identification

**Implementation:** Python, C, network traffic generation tools, Wireshark-compatible PCAP

**Primary artifact:** `ps05/public/shadow_breach_capture.pcap`

### PS-06 — The Encoded Research

**Category:** Reverse Engineering

Participants examine an executable obtained through the investigation and analyze its relationship to encrypted research data.

The challenge requires understanding program behavior and recovering information needed to interpret the encrypted artifact.

**Skills assessed:**
- Executable analysis
- Static reverse engineering
- Identification of embedded keys
- Understanding encryption routines
- Data recovery

**Implementation:** C, Python, Linux ELF executable, Ghidra

### PS-07 — The Final Access

**Category:** Linux Privilege Escalation

The final stage provides an isolated Linux environment containing an intentionally insecure privilege configuration.

Participants investigate the available permissions and demonstrate their understanding of privilege escalation.

**Skills assessed:**
- Linux enumeration
- File permissions
- Sudo configuration analysis
- Privilege escalation
- Secure Linux administration

**Implementation:** Docker, Linux, SSH, sudo configuration

**Security note:** This challenge intentionally contains a privilege escalation weakness. It must not be deployed on a production server.

---

## 4. System Architecture

Project Shadow uses a modular architecture in which individual challenge services operate alongside a centralized CTF platform.

The principal components are:

1. **Ubuntu Host:** Provides the underlying Linux environment.
2. **Docker Engine:** Runs containerized challenge services and supporting components.
3. **rCTF:** Provides player accounts, challenge registration, flag submission, and score tracking.
4. **Local DNS Service:** Supports reconnaissance activities in PS-01.
5. **Challenge Web Services:** Deliver challenge pages, instructions, and downloadable artifacts.
6. **Linux Services:** Host selected challenge pages through systemd-managed processes.
7. **SSH Challenge Container:** Provides an isolated environment for PS-07.
8. **Hint Portal:** Displays participant hints through a separate web interface.

Docker is used to improve repeatability and separate selected vulnerable applications from the Ubuntu host.

The system was developed and tested for an academic laboratory environment. Production deployment is outside its intended scope.

## 5. Technologies Used

| Technology | Purpose |
|---|---|
| Ubuntu Linux | CTF development and hosting |
| Docker / Docker Compose | Containerized challenge deployment |
| rCTF | Challenge management and scoreboard |
| Nginx | Web hosting and virtual host configuration |
| dnsmasq | Local DNS challenge service |
| Node.js / Express | Web application challenge |
| SQLite | PS-02 challenge database |
| Python | Challenge generation, utilities, encryption and validation |
| C | Executable and challenge artifact development |
| systemd | Management of selected challenge web services |
| HTML / JavaScript | Challenge pages and hint interface |
| Wireshark | Network traffic investigation |
| Sleuth Kit | Filesystem forensic analysis |
| Ghidra | Reverse engineering analysis |
| Git / GitHub | Version control, collaboration, and contribution tracking |

## 6. Repository Structure

```text
IE3132-Project-Shadow-Final-Group42/
│
├── challenges/
│   ├── ps01/                 # OSINT website and local DNS
│   └── ps02/                 # Vulnerable web portal
│
├── ps03/                    # Cryptography challenge
├── ps04/                    # Digital forensics challenge
├── ps05/                    # Network forensics challenge
├── ps06/                    # Reverse engineering challenge
├── ps07/                    # Linux privilege escalation
│
├── hint-portal/             # Browser-based hint interface
│
├── contribution-evidence/
│   ├── Dushiev_D_C/
│   ├── Bandara_A_H_M_O_K/
│   ├── Jeramy_S_R/
│   └── Aluthpatabendige_S_K/
│
├── .gitignore
├── .gitattributes
└── README.md
```

The `contribution-evidence` directory contains individual supporting material for the group members' work.

The runnable challenge source is maintained separately from individual contribution evidence to keep the overall project organized.

## 7. Setup and Execution

### 7.1 Prerequisites

The development environment requires:

- Ubuntu Linux
- Git
- Docker Engine
- Docker Compose plugin
- Python 3
- Node.js and npm where required
- An operational rCTF deployment
- systemd for the Linux-hosted challenge services
- Suitable forensic and analysis tools for challenge testing

Some challenges also require local DNS configuration or an SSH client.

### 7.2 Clone the Repository

```bash
git clone https://github.com/daviddushiev/IE3132-Project-Shadow-Final-Group42.git

cd IE3132-Project-Shadow-Final-Group42
```

Because the repository is private, access must be granted by the repository owner.

### 7.3 Start the Containerized Challenges

PS-01 and PS-02 include Docker Compose configuration files.

From the project root:

```bash
docker compose -f challenges/ps01/compose.yml up -d --build
```

```bash
docker compose -f challenges/ps02/compose.yml up -d --build
```

Verify their status:

```bash
docker ps
```

The containers should be started only within the authorized test environment.

### 7.4 PS-01 Local DNS

PS-01 uses a local DNS service to support fictional domain discovery.

The project includes:

- `challenges/ps01/dns/dnsmasq.conf`
- `challenges/ps01/dns/Dockerfile`
- `challenges/ps01/nginx.conf`

On the original Ubuntu laboratory environment, DNS queries were tested against the local DNS service using port `1053`.

Example:

```bash
dig @127.0.0.1 -p 1053 archive.solace.test
```

The participant's DNS configuration and virtual host access must be correctly configured for the reconnaissance challenge to function as intended.

### 7.5 PS-03 to PS-06 Web Delivery

The project includes challenge pages and downloadable evidence inside the corresponding `public/` directories.

In the original laboratory environment, selected challenge pages were delivered using systemd-managed web services.

A separate deployment step is required to reproduce those services on another machine.

The relevant service configurations, working directories, ports, and startup commands must be checked against the actual Ubuntu deployment before use.

### 7.6 PS-07 Environment

PS-07 contains a Docker-based Linux challenge environment.

Relevant files include:

```text
ps07/docker/Dockerfile
ps07/reset-ps07.sh
```

The provided reset script is intended for managing the local challenge environment.

Before executing it on another system, review its container names, network settings, port mappings, and permissions.

The original environment exposed an isolated SSH challenge service for participant access.

### 7.7 rCTF Configuration

rCTF is used for:

- Participant registration and login
- Challenge presentation
- Flag validation
- Challenge scoring
- Scoreboard management

The challenge source repository does not automatically provision the entire rCTF installation.

The rCTF deployment, database, Redis service, administrative settings, challenge entries, flags, and scoring must be configured separately according to the controlled laboratory setup.

Do not commit real administrator credentials or production secrets to this repository.

### 7.8 Hint Portal

The hint interface is available in:

```text
hint-portal/index.html
```

The portal provides supporting hints for participants.

Its browser-based state is separate from the rCTF scoring database. Any displayed hint-related penalty or progress indication should not be treated as an automatic rCTF score update unless corresponding server-side integration is implemented.

## 8. Testing and Validation

Testing was performed throughout development to check challenge accessibility, correct flag submission behavior, supporting service operation, and challenge progression.

Testing activities included:

- Verifying Docker container status.
- Confirming HTTP challenge page accessibility.
- Testing local DNS queries.
- Checking access to the Linux SSH challenge environment.
- Downloading and examining challenge artifacts.
- Verifying intended solutions in the laboratory.
- Testing valid and invalid flag submissions.
- Confirming scoreboard activity.
- Recording supporting screenshots and test results.

Automated health-check scripts and integration evidence are included in the individual contribution evidence where applicable.

Testing evidence demonstrates the behavior observed in the development environment; successful deployment on a separate machine must be validated independently.

## 9. Group Members and Individual Contributions

### Dushiev D.C — Platform Architecture and Deployment

**Primary responsibility:** CTF platform setup, environment configuration, deployment, and supporting security controls.

Contribution areas include:

- Ubuntu CTF hosting environment
- Docker and supporting service configuration
- rCTF deployment and integration
- Local network and service accessibility
- Challenge environment isolation
- Supporting platform and configuration evidence

**Evidence directory:** `contribution-evidence/Dushiev_D_C/`

### Bandara A.H.M.O.K — Challenge Development

**Primary responsibility:** Development and testing activities for assigned challenges.

Assigned challenge areas:

- PS-02 — Web Application Security
- PS-04 — Digital Forensics
- PS-07 — Linux Privilege Escalation

Supporting source-code copies and screenshots are maintained under:

`contribution-evidence/Bandara_A_H_M_O_K/`

### Jeramy S.R — Challenge Development

**Primary responsibility:** Development and testing activities for assigned challenges.

Assigned challenge areas:

- PS-01 — OSINT and Reconnaissance
- PS-03 — Cryptography
- PS-05 — Network Forensics
- PS-06 — Reverse Engineering

Supporting source-code copies and screenshots are maintained under:

`contribution-evidence/Jeramy_S_R/`

### Aluthpatabendige S.K — Integration and Testing

**Primary responsibility:** Integration testing, service verification, supporting scripts, and technical documentation.

Contribution areas include:

- Cross-challenge integration checks
- Challenge service availability verification
- Automated testing support
- Test result recording
- Documentation and integration evidence

**Evidence directory:** `contribution-evidence/Aluthpatabendige_S_K/`

Individual contributions are also represented through separate Git branches, commit histories, and merged Pull Requests.

## 10. GitHub Collaboration and Version Control

The project uses Git and GitHub to maintain source code and support group collaboration.

Development evidence was organized through individual branches:

| Branch | Responsibility |
|---|---|
| `final-runnable-project` | Runnable CTF implementation |
| `dushiev-platform` | Platform and deployment evidence |
| `bandara-challenges` | Bandara's assigned challenges |
| `jeramy-challenges` | Jeramy's assigned challenges |
| `aluthpatabendige-integration` | Integration and testing evidence |

All five branches were integrated through reviewed Pull Requests into the `main` branch.

The repository preserves the group members' contribution commits, and the main branch contains the combined submission.

## 11. Security and Ethical Considerations

Project Shadow contains deliberately vulnerable applications and simulated attack scenarios for educational use.

The following restrictions apply:

- Run challenges only in an authorized and isolated laboratory environment.
- Do not expose intentionally vulnerable services directly to the public internet.
- Use fictional users, passwords, research data, and organization details.
- Do not reuse challenge credentials for real systems.
- Restrict administrative access to Docker, rCTF, and the Ubuntu host.
- Keep challenge flags and intended solutions private during assessments.
- Do not use the supplied exploitation techniques against systems without authorization.

The project's vulnerabilities are intentionally included for cybersecurity education and must not be interpreted as recommended application design practices.

## 12. Known Deployment Limitations

The repository includes the primary challenge source files, web resources, and selected forensic artifacts.

However, a complete installation on a clean Ubuntu machine additionally requires configuration of the surrounding environment, including:

- rCTF deployment and challenge registration
- Selected systemd service definitions
- Host-level networking and firewall settings
- Appropriate Docker networking and port mappings
- Local DNS access
- Host-specific paths and permissions

These elements must be reconciled with the original laboratory environment to produce a fully automated, reproducible deployment.

The current repository should therefore be treated as the primary source and evidence collection for the completed CTF, rather than a verified one-command installation.

## 13. Conclusion

Project Shadow demonstrates the integration of multiple penetration testing and cybersecurity techniques within a unified Capture the Flag environment.

The project combines web security, reconnaissance, cryptography, digital forensics, network analysis, reverse engineering, and Linux security into a single investigation-based learning experience.

Through Docker deployment, rCTF integration, custom challenge development, supporting scripts, and collaborative version control, the group developed a practical cybersecurity laboratory and documented its individual contributions.

The resulting project provides hands-on experience in identifying vulnerabilities, examining digital evidence, validating security findings, and understanding the importance of secure system configuration.

---

**Academic Project:** IE3132 – Penetration Testing  
**Group:** 42  
**Project:** Project Shadow — The Vanished Research  
**Purpose:** Educational cybersecurity training and assessment  
**Repository Access:** Private — Authorized Group Members and Examiners
