"""
System Conflict Detector Module

This module detects and reports conflicts between auto-evolution-system
and quantum-x-builder to ensure harmonious integration.
"""

import os
import sys
import json
import logging
import subprocess
from typing import Dict, List, Any
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SystemConflictDetector:
    """Detects and reports conflicts between integrated systems."""
    
    def __init__(self):
        """Initialize the conflict detector."""
        self.conflicts = []
        self.warnings = []
        logging.info("SystemConflictDetector initialized")
    
    def check_path_conflicts(self, quantum_x_path: str = "/tmp/quantum-x-builder") -> Dict[str, Any]:
        """
        Check for path conflicts.
        
        Args:
            quantum_x_path: Path where quantum-x-builder is cloned
        
        Returns:
            Dict containing conflict detection results
        """
        logging.info(f"Checking path conflicts for: {quantum_x_path}")
        
        conflicts = []
        
        # Check if path exists and is accessible
        if os.path.exists(quantum_x_path):
            if not os.access(quantum_x_path, os.R_OK):
                conflicts.append({
                    "type": "path_access",
                    "severity": "high",
                    "path": quantum_x_path,
                    "message": f"Path exists but is not readable: {quantum_x_path}"
                })
            
            # Check if it's a git repository
            git_dir = os.path.join(quantum_x_path, ".git")
            if not os.path.exists(git_dir):
                conflicts.append({
                    "type": "invalid_repo",
                    "severity": "medium",
                    "path": quantum_x_path,
                    "message": f"Path exists but is not a valid git repository: {quantum_x_path}"
                })
        
        # Check parent directory permissions
        parent_dir = os.path.dirname(quantum_x_path)
        if os.path.exists(parent_dir):
            if not os.access(parent_dir, os.W_OK):
                conflicts.append({
                    "type": "path_write",
                    "severity": "high",
                    "path": parent_dir,
                    "message": f"Parent directory is not writable: {parent_dir}"
                })
        
        return {
            "success": len(conflicts) == 0,
            "conflicts": conflicts,
            "path": quantum_x_path,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_module_conflicts(self) -> Dict[str, Any]:
        """
        Check for Python module naming conflicts.
        
        Returns:
            Dict containing module conflict results
        """
        logging.info("Checking for module naming conflicts...")
        
        conflicts = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get list of local modules
        local_modules = []
        for file in os.listdir(current_dir):
            if file.endswith('.py') and not file.startswith('__'):
                module_name = file[:-3]
                local_modules.append(module_name)
        
        # Check for conflicts with installed packages
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "list", "--format=json"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                installed_packages = json.loads(result.stdout)
                package_names = {pkg['name'].lower().replace('-', '_') for pkg in installed_packages}
                
                for module in local_modules:
                    if module.lower() in package_names:
                        conflicts.append({
                            "type": "module_naming",
                            "severity": "medium",
                            "module": module,
                            "message": f"Local module '{module}' has same name as installed package"
                        })
        except Exception as e:
            logging.warning(f"Could not check installed packages: {e}")
        
        return {
            "success": len(conflicts) == 0,
            "conflicts": conflicts,
            "local_modules": local_modules,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_port_conflicts(self, ports: List[int] = None) -> Dict[str, Any]:
        """
        Check for port conflicts.
        
        Args:
            ports: List of ports to check
        
        Returns:
            Dict containing port conflict results
        """
        if ports is None:
            # Default ports commonly used by development systems
            ports = [8000, 8080, 3000, 5000]
        
        logging.info(f"Checking port conflicts for ports: {ports}")
        
        conflicts = []
        
        try:
            import socket
            
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex(('localhost', port))
                sock.close()
                
                if result == 0:
                    conflicts.append({
                        "type": "port_in_use",
                        "severity": "low",
                        "port": port,
                        "message": f"Port {port} is already in use"
                    })
        except Exception as e:
            logging.warning(f"Could not check ports: {e}")
        
        return {
            "success": len(conflicts) == 0,
            "conflicts": conflicts,
            "ports_checked": ports,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_dependency_conflicts(self) -> Dict[str, Any]:
        """
        Check for dependency version conflicts.
        
        Returns:
            Dict containing dependency conflict results
        """
        logging.info("Checking for dependency conflicts...")
        
        conflicts = []
        
        try:
            # Check pip for conflicting dependencies
            result = subprocess.run(
                [sys.executable, "-m", "pip", "check"],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode != 0:
                for line in result.stdout.split('\n'):
                    if line.strip():
                        conflicts.append({
                            "type": "dependency_version",
                            "severity": "high",
                            "message": line.strip()
                        })
        except Exception as e:
            logging.warning(f"Could not check dependencies: {e}")
        
        return {
            "success": len(conflicts) == 0,
            "conflicts": conflicts,
            "timestamp": datetime.now().isoformat()
        }
    
    def run_comprehensive_conflict_check(self, quantum_x_path: str = "/tmp/quantum-x-builder") -> Dict[str, Any]:
        """
        Run comprehensive conflict detection.
        
        Args:
            quantum_x_path: Path where quantum-x-builder is cloned
        
        Returns:
            Dict containing all conflict detection results
        """
        logging.info("=" * 80)
        logging.info("Running Comprehensive Conflict Detection")
        logging.info("=" * 80)
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {}
        }
        
        # Run all checks
        results["checks"]["path_conflicts"] = self.check_path_conflicts(quantum_x_path)
        results["checks"]["module_conflicts"] = self.check_module_conflicts()
        results["checks"]["port_conflicts"] = self.check_port_conflicts()
        results["checks"]["dependency_conflicts"] = self.check_dependency_conflicts()
        
        # Aggregate results
        all_conflicts = []
        for check_name, check_result in results["checks"].items():
            if not check_result.get("success"):
                all_conflicts.extend(check_result.get("conflicts", []))
        
        results["overall_success"] = len(all_conflicts) == 0
        results["total_conflicts"] = len(all_conflicts)
        results["conflicts_by_severity"] = {
            "high": len([c for c in all_conflicts if c.get("severity") == "high"]),
            "medium": len([c for c in all_conflicts if c.get("severity") == "medium"]),
            "low": len([c for c in all_conflicts if c.get("severity") == "low"])
        }
        
        if results["overall_success"]:
            logging.info("\n✓ No conflicts detected! Systems are compatible.")
        else:
            logging.warning(f"\n⚠ {len(all_conflicts)} conflict(s) detected:")
            for conflict in all_conflicts:
                logging.warning(f"  - [{conflict.get('severity', 'unknown').upper()}] {conflict.get('message', 'Unknown conflict')}")
        
        logging.info("=" * 80)
        
        return results


if __name__ == "__main__":
    # Example usage
    detector = SystemConflictDetector()
    results = detector.run_comprehensive_conflict_check()
    
    print("\n" + "=" * 80)
    print("CONFLICT DETECTION RESULTS")
    print("=" * 80)
    print(json.dumps(results, indent=2))
