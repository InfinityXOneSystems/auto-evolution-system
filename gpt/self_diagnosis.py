"""
Self-Diagnosis Module

Continuously monitors and diagnoses system health, performance,
and potential issues for autonomous correction.
"""

import os
import sys
import json
import logging
import psutil
import time
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class SelfDiagnosisSystem:
    """Autonomous system health monitoring and diagnosis."""
    
    def __init__(self):
        """Initialize the self-diagnosis system."""
        self.health_history = []
        self.issue_thresholds = {
            "cpu_percent": 90.0,
            "memory_percent": 85.0,
            "disk_percent": 90.0,
            "response_time_ms": 1000
        }
        logging.info("SelfDiagnosisSystem initialized")
    
    def check_system_resources(self) -> Dict[str, Any]:
        """
        Check system resource utilization.
        
        Returns:
            Dict containing resource metrics and status
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            resources = {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "memory_available_gb": memory.available / (1024**3),
                "disk_percent": disk.percent,
                "disk_free_gb": disk.free / (1024**3),
                "timestamp": datetime.now().isoformat()
            }
            
            # Check for issues
            issues = []
            if cpu_percent > self.issue_thresholds["cpu_percent"]:
                issues.append(f"High CPU usage: {cpu_percent}%")
            if memory.percent > self.issue_thresholds["memory_percent"]:
                issues.append(f"High memory usage: {memory.percent}%")
            if disk.percent > self.issue_thresholds["disk_percent"]:
                issues.append(f"High disk usage: {disk.percent}%")
            
            resources["issues"] = issues
            resources["healthy"] = len(issues) == 0
            
            logging.info(f"Resource check: CPU={cpu_percent}%, Memory={memory.percent}%, Disk={disk.percent}%")
            return resources
            
        except Exception as e:
            logging.error(f"Error checking system resources: {e}")
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_code_health(self, code_path: str) -> Dict[str, Any]:
        """
        Check the health of the codebase.
        
        Args:
            code_path: Path to the code directory
        
        Returns:
            Dict containing code health metrics
        """
        try:
            logging.info(f"Checking code health for: {code_path}")
            
            if not os.path.exists(code_path):
                return {
                    "success": False,
                    "error": f"Path does not exist: {code_path}"
                }
            
            metrics = {
                "python_files": 0,
                "total_lines": 0,
                "average_file_size": 0,
                "missing_docstrings": 0,
                "complexity_issues": [],
                "timestamp": datetime.now().isoformat()
            }
            
            python_files = []
            for root, dirs, files in os.walk(code_path):
                if '.git' in root or '__pycache__' in root:
                    continue
                
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        python_files.append(file_path)
                        metrics["python_files"] += 1
                        
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                lines = f.readlines()
                                metrics["total_lines"] += len(lines)
                                
                                # Check for docstring
                                content = ''.join(lines)
                                if '"""' not in content and "'''" not in content:
                                    metrics["missing_docstrings"] += 1
                                
                                # Check for very long files (potential complexity issue)
                                if len(lines) > 500:
                                    metrics["complexity_issues"].append({
                                        "file": file_path,
                                        "lines": len(lines),
                                        "issue": "File too long"
                                    })
                        except Exception:
                            pass
            
            if metrics["python_files"] > 0:
                metrics["average_file_size"] = metrics["total_lines"] / metrics["python_files"]
            
            # Determine health status
            issues = []
            if metrics["missing_docstrings"] > metrics["python_files"] * 0.3:
                issues.append("Many files missing docstrings")
            if len(metrics["complexity_issues"]) > 5:
                issues.append("Multiple files with high complexity")
            
            metrics["issues"] = issues
            metrics["healthy"] = len(issues) == 0
            
            logging.info(f"Code health check complete: {metrics['python_files']} files, {metrics['total_lines']} lines")
            return metrics
            
        except Exception as e:
            logging.error(f"Error checking code health: {e}")
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def check_dependencies(self, requirements_path: str = None) -> Dict[str, Any]:
        """
        Check for dependency issues and vulnerabilities.
        
        Args:
            requirements_path: Path to requirements.txt or similar
        
        Returns:
            Dict containing dependency status
        """
        logging.info("Checking dependencies...")
        
        try:
            # Check if pip is available
            import pkg_resources
            installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
            
            result = {
                "installed_packages": len(installed_packages),
                "packages": dict(list(installed_packages.items())[:10]),  # Sample
                "outdated_check_needed": True,
                "timestamp": datetime.now().isoformat()
            }
            
            # In a real implementation, this would:
            # 1. Check for outdated packages
            # 2. Scan for known vulnerabilities
            # 3. Verify compatibility
            
            logging.info(f"Dependency check complete: {len(installed_packages)} packages installed")
            return result
            
        except Exception as e:
            logging.error(f"Error checking dependencies: {e}")
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def run_comprehensive_diagnosis(self, code_path: str = None) -> Dict[str, Any]:
        """
        Run a comprehensive system diagnosis.
        
        Args:
            code_path: Path to code directory for health check
        
        Returns:
            Dict containing complete diagnosis results
        """
        logging.info("Running comprehensive diagnosis...")
        
        diagnosis = {
            "timestamp": datetime.now().isoformat(),
            "resource_check": self.check_system_resources(),
            "dependency_check": self.check_dependencies(),
            "overall_health": "healthy"
        }
        
        if code_path:
            diagnosis["code_health"] = self.check_code_health(code_path)
        
        # Determine overall health
        all_issues = []
        for check_name, check_result in diagnosis.items():
            if isinstance(check_result, dict) and "issues" in check_result:
                all_issues.extend(check_result["issues"])
        
        diagnosis["all_issues"] = all_issues
        if len(all_issues) > 0:
            diagnosis["overall_health"] = "issues_detected"
            if len(all_issues) > 5:
                diagnosis["overall_health"] = "critical"
        
        self.health_history.append(diagnosis)
        
        logging.info(f"Comprehensive diagnosis complete. Health: {diagnosis['overall_health']}")
        return diagnosis
    
    def get_health_trend(self, limit: int = 10) -> Dict[str, Any]:
        """
        Get health trend over time.
        
        Args:
            limit: Number of recent records to return
        
        Returns:
            Dict containing health trend data
        """
        recent_history = self.health_history[-limit:]
        
        return {
            "record_count": len(recent_history),
            "history": recent_history,
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Example usage
    diagnosis = SelfDiagnosisSystem()
    
    # Run comprehensive diagnosis
    result = diagnosis.run_comprehensive_diagnosis(
        code_path=os.path.dirname(os.path.abspath(__file__))
    )
    
    print(json.dumps(result, indent=2))
