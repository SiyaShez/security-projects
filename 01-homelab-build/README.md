# Home Lab Build

## Objective
Build an isolated virtual environment for safe, hands-on security practice — scanning,
exploitation, and traffic analysis — without touching real production networks.

## Tools Used
- VirtualBox (hypervisor)
- Kali Linux (attacker/analysis machine)
- Windows Server 2022 Evaluation (target machine — later promoted to a domain controller,
  see [project 06](../06-active-directory))
- Internal network adapter (for isolation)

## Setup Steps

1. **Install VirtualBox** on the host machine.
2. **Create the Kali Linux VM**
   - Download the official Kali Linux VirtualBox image from kali.org
   - Allocate at least 2 CPU cores, 4GB RAM, 40GB disk
3. **Create the Windows Server target VM**
   - Downloaded the free 90-day Windows Server 2022 evaluation ISO from Microsoft's Evaluation
     Center
   - Allocated 4GB RAM, 60GB disk
4. **Configure networking for isolation**
   - In VirtualBox: Settings → Network → Attached to: **Internal Network** (same name for both VMs)
   - Assigned static IPs on the `192.168.100.0/24` subnet:
     - Kali: `192.168.100.20`
     - Windows Server: `192.168.100.10`
   - This keeps lab traffic completely separate from the home network — nothing here touches
     real, non-owned systems
5. **Verify connectivity**
   - Confirmed with `ping -c 4 192.168.100.10` from Kali — 0% packet loss, ~1-3ms latency
   - Confirmed the Windows side with `Get-NetIPAddress -InterfaceAlias "Ethernet" -AddressFamily IPv4`

## Network Diagram
```
[ Kali Linux VM ]  <---- Internal Network ---->  [ Windows Server 2022 VM ]
   192.168.100.20                                     192.168.100.10 (SRV01)
```

## Skills Gained
- VirtualBox / virtualization fundamentals
- Kali Linux setup and toolset familiarity
- Windows administration basics
- Network isolation and lab hygiene — critical for practicing safely and legally

## Notes
This lab is strictly for personal, isolated practice. All activity here stays confined to
machines and networks I own and control.
