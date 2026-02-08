# Quick Start Guide - Autonomous Evolution System

## 5-Minute Setup

### 1. Install (1 minute)

```bash
# Clone the repository
git clone https://github.com/InfinityXOneSystems/auto-evolution-system.git
cd auto-evolution-system

# Install dependencies
pip install -r requirements.txt
```

### 2. Test (1 minute)

```bash
# Run the test suite
python test_autonomous_system.py

# Check system status
python gpt/autonomous_evolution_main.py --mode status
```

### 3. Immediate Quantum-X Integration (2 minutes)

```bash
# Immediately integrate quantum-x-builder with conflict detection
python gpt/autonomous_evolution_main.py --mode quantum-start
```

This will:
- ✅ Check for conflicts between systems
- ✅ Clone quantum-x-builder repository immediately
- ✅ Analyze the codebase for integration
- ✅ Validate installation and harmonious integration
- ✅ Start immediately (no waiting for scheduled time)

---

### 4. Run First Cycle (3 minutes)

```bash
# Execute a single autonomous evolution cycle
python gpt/autonomous_evolution_main.py --mode cycle
```

This will:
- ✅ Clone and analyze quantum-x-builder repository
- ✅ Diagnose system health
- ✅ Fix any issues automatically
- ✅ Clean up code and cache
- ✅ Generate improvement recommendations

---

## Start Autonomous Mode

Once you're comfortable with the cycle, start 24/7 autonomous operation:

```bash
python gpt/autonomous_evolution_main.py --mode autonomous
```

**That's it!** The system is now fully autonomous and requires zero human intervention.

---

## Quick Integration

For immediate quantum-x-builder integration without full cycle:

```bash
# Option 1: Via main system
python gpt/autonomous_evolution_main.py --mode quantum-start

# Option 2: Standalone script
python gpt/immediate_quantum_startup.py
```

See [QUANTUM_INTEGRATION.md](QUANTUM_INTEGRATION.md) for detailed integration guide.

---

## What Happens Next?

The system will automatically:

### Daily at 2:00 AM
- Analyze system drift
- Detect code duplication
- Generate improvement proposals
- Queue actionable TODOs

### Daily at 3:00 AM
- Sync with quantum-x-builder
- Analyze quantum-x codebase
- Share improvements across systems

### Daily at 4:00 AM
- Clean Python cache
- Remove temporary files
- Optimize imports
- Update dependencies

### Every 6 Hours
- Check system resources
- Monitor code health
- Scan for vulnerabilities
- Apply fixes automatically

---

## Monitoring

### View Logs
```bash
tail -f autonomous_evolution.log
```

### Check Status Anytime
```bash
python gpt/autonomous_evolution_main.py --mode status
```

---

## Configuration

Edit `system_manifest.yaml` to customize:

```yaml
schedule:
  daily_evolution_time: "02:00"    # Change timing
  quantum_x_sync_time: "03:00"     # Change timing
  diagnosis_interval_hours: 6      # Change frequency

thresholds:
  cpu_percent: 90.0                # Alert threshold
  memory_percent: 85.0             # Alert threshold
  disk_percent: 90.0               # Alert threshold
```

---

## Key Features at a Glance

| Feature             | Status | Automation Level |
|---------------------|--------|------------------|
| Self-Analyzing      | ✅     | 100%             |
| Self-Diagnosing     | ✅     | 100%             |
| Self-Fixing         | ✅     | 100%             |
| Self-Healing        | ✅     | 100%             |
| Self-Cleaning       | ✅     | 100%             |
| Self-Maintaining    | ✅     | 100%             |
| Self-Evolving       | ✅     | 100%             |
| Quantum-X Sync      | ✅     | 100%             |

**Overall Autonomy: 100% - Zero Human Intervention Required**

---

## Need Help?

1. Check the logs: `autonomous_evolution.log`
2. Run diagnostics: `python gpt/autonomous_evolution_main.py --mode status`
3. Read full documentation: `DOCUMENTATION.md`
4. Open an issue: GitHub Issues

---

## Pro Tips

💡 **Tip 1**: Run a single cycle first to see how everything works before starting autonomous mode

💡 **Tip 2**: The system creates automatic backups in `/tmp/backups/` before making changes

💡 **Tip 3**: Check the logs regularly during the first few days to understand the system's behavior

💡 **Tip 4**: Adjust thresholds in `system_manifest.yaml` based on your system's capabilities

💡 **Tip 5**: The quantum-x-builder repository is cloned to `/tmp/quantum-x-builder/` for analysis

---

## Success Indicators

You'll know the system is working correctly when you see:

✅ All tests passing  
✅ Health status: "healthy"  
✅ Autonomous mode: "running"  
✅ Scheduled tasks: 4+ tasks  
✅ No errors in logs  

---

## Example Output

### Successful Cycle
```
================================================================================
Full Autonomous Evolution Cycle Completed Successfully
Duration: 7.76 seconds
================================================================================

✓ Quantum-X Integration: SUCCESS
✓ Self-Diagnosis: HEALTHY
✓ Auto-Fix: 0 issues found
✓ Self-Healing: OPERATIONAL
✓ Cleanup: COMPLETE
✓ Maintenance: UP-TO-DATE
✓ Recommendations: GENERATED
```

### Autonomous Mode Started
```
================================================================================
AUTONOMOUS MODE ACTIVE
System is now self-managing, self-evolving, and fully autonomous
================================================================================
```

---

**You're all set! Welcome to the future of autonomous systems. 🚀**
