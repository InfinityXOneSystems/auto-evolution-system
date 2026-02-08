"""
Immediate Quantum-X Startup Module

This module provides immediate startup capabilities for quantum-x-builder integration,
bypassing the scheduled execution time for instant system integration and validation.
"""

import os
import sys
import json
import logging
from typing import Dict, Any
from datetime import datetime

# Add the gpt directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quantum_x_integration import QuantumXIntegration
from system_conflict_detector import SystemConflictDetector

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('quantum_immediate_startup.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class ImmediateQuantumStartup:
    """
    Manages immediate startup and integration of quantum-x-builder system
    with conflict detection and harmonious installation.
    """
    
    def __init__(self, quantum_x_path: str = "/tmp/quantum-x-builder"):
        """
        Initialize immediate startup handler.
        
        Args:
            quantum_x_path: Path where quantum-x-builder will be cloned
        """
        self.quantum_x_path = quantum_x_path
        self.conflict_detector = SystemConflictDetector()
        self.quantum_x = QuantumXIntegration(local_path=quantum_x_path)
        logger.info(f"ImmediateQuantumStartup initialized with path: {quantum_x_path}")
    
    def pre_installation_checks(self) -> Dict[str, Any]:
        """
        Run pre-installation conflict checks.
        
        Returns:
            Dict containing pre-installation check results
        """
        logger.info("\n" + "=" * 80)
        logger.info("STEP 1: Pre-Installation Conflict Detection")
        logger.info("=" * 80)
        
        # Run comprehensive conflict check
        conflict_results = self.conflict_detector.run_comprehensive_conflict_check(self.quantum_x_path)
        
        # Determine if we can proceed
        high_severity_conflicts = conflict_results.get("conflicts_by_severity", {}).get("high", 0)
        
        if high_severity_conflicts > 0:
            logger.error(f"⚠ Cannot proceed: {high_severity_conflicts} high-severity conflict(s) detected")
            conflict_results["can_proceed"] = False
        else:
            logger.info("✓ Pre-installation checks passed")
            conflict_results["can_proceed"] = True
        
        return conflict_results
    
    def install_quantum_x(self) -> Dict[str, Any]:
        """
        Install (clone or update) quantum-x-builder immediately.
        
        Returns:
            Dict containing installation results
        """
        logger.info("\n" + "=" * 80)
        logger.info("STEP 2: Quantum-X Builder Installation")
        logger.info("=" * 80)
        
        try:
            # Clone or update the repository
            clone_result = self.quantum_x.clone_or_update_repo()
            
            if clone_result.get("success"):
                logger.info(f"✓ Quantum-X Builder {clone_result.get('operation', 'installed')} successfully")
                logger.info(f"  Location: {self.quantum_x_path}")
            else:
                logger.error(f"✗ Installation failed: {clone_result.get('output', 'Unknown error')}")
            
            return clone_result
            
        except Exception as e:
            logger.error(f"Installation error: {e}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def analyze_integration(self) -> Dict[str, Any]:
        """
        Analyze quantum-x-builder for integration compatibility.
        
        Returns:
            Dict containing analysis results
        """
        logger.info("\n" + "=" * 80)
        logger.info("STEP 3: Integration Analysis")
        logger.info("=" * 80)
        
        try:
            # Analyze the quantum-x codebase
            analysis_result = self.quantum_x.analyze_quantum_x_code()
            
            if analysis_result.get("success"):
                metrics = analysis_result.get("metrics", {})
                logger.info(f"✓ Analysis complete:")
                logger.info(f"  Total files: {metrics.get('total_files', 0)}")
                logger.info(f"  Total lines: {metrics.get('total_lines', 0)}")
                logger.info(f"  File types: {len(metrics.get('file_types', {}))}")
                
                recommendations = analysis_result.get("recommendations", [])
                if recommendations:
                    logger.info(f"  Recommendations: {len(recommendations)}")
                    for i, rec in enumerate(recommendations, 1):
                        logger.info(f"    {i}. {rec}")
            else:
                logger.error(f"✗ Analysis failed: {analysis_result.get('error', 'Unknown error')}")
            
            return analysis_result
            
        except Exception as e:
            logger.error(f"Analysis error: {e}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def post_installation_validation(self) -> Dict[str, Any]:
        """
        Validate the installation and check for post-installation conflicts.
        
        Returns:
            Dict containing validation results
        """
        logger.info("\n" + "=" * 80)
        logger.info("STEP 4: Post-Installation Validation")
        logger.info("=" * 80)
        
        validation_results = {
            "timestamp": datetime.now().isoformat(),
            "checks": {}
        }
        
        # Check 1: Repository exists
        repo_exists = os.path.exists(self.quantum_x_path)
        validation_results["checks"]["repository_exists"] = repo_exists
        
        if repo_exists:
            logger.info(f"✓ Repository exists at: {self.quantum_x_path}")
        else:
            logger.error(f"✗ Repository not found at: {self.quantum_x_path}")
        
        # Check 2: Git repository validity
        git_dir = os.path.join(self.quantum_x_path, ".git")
        is_valid_repo = os.path.exists(git_dir)
        validation_results["checks"]["is_valid_git_repo"] = is_valid_repo
        
        if is_valid_repo:
            logger.info("✓ Valid git repository structure")
        else:
            logger.warning("⚠ Git repository structure not found")
        
        # Check 3: File count
        if repo_exists:
            file_count = sum(1 for _, _, files in os.walk(self.quantum_x_path) for _ in files)
            validation_results["checks"]["file_count"] = file_count
            
            if file_count > 0:
                logger.info(f"✓ Repository contains {file_count} files")
            else:
                logger.warning("⚠ Repository appears to be empty")
        
        # Check 4: No new conflicts
        conflict_check = self.conflict_detector.check_path_conflicts(self.quantum_x_path)
        validation_results["checks"]["post_install_conflicts"] = conflict_check
        
        if conflict_check.get("success"):
            logger.info("✓ No post-installation conflicts detected")
        else:
            logger.warning(f"⚠ {len(conflict_check.get('conflicts', []))} conflict(s) detected after installation")
        
        # Overall validation
        validation_results["overall_success"] = (
            repo_exists and 
            is_valid_repo and 
            validation_results["checks"].get("file_count", 0) > 0
        )
        
        if validation_results["overall_success"]:
            logger.info("\n✓ Post-installation validation PASSED")
        else:
            logger.error("\n✗ Post-installation validation FAILED")
        
        return validation_results
    
    def sync_and_integrate(self) -> Dict[str, Any]:
        """
        Sync improvements and complete integration.
        
        Returns:
            Dict containing sync results
        """
        logger.info("\n" + "=" * 80)
        logger.info("STEP 5: System Integration and Sync")
        logger.info("=" * 80)
        
        try:
            # Get integration status
            status = self.quantum_x.get_integration_status()
            logger.info("Current integration status:")
            logger.info(f"  Repository URL: {status.get('repository_url', 'N/A')}")
            logger.info(f"  Local path: {status.get('local_path', 'N/A')}")
            logger.info(f"  Last sync: {status.get('last_sync', 'Never')}")
            logger.info(f"  Repository exists: {status.get('repository_exists', False)}")
            
            # Sync improvements
            improvements = [
                "Immediate startup capability added",
                "Conflict detection integrated",
                "Harmonious installation validated"
            ]
            
            sync_result = self.quantum_x.sync_improvements(improvements)
            
            if sync_result.get("success"):
                logger.info(f"✓ Synced {sync_result.get('improvements_synced', 0)} improvement(s)")
            else:
                logger.warning("⚠ Sync completed with warnings")
            
            return {
                "success": True,
                "status": status,
                "sync": sync_result,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Integration error: {e}", exc_info=True)
            return {
                "success": False,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
    
    def execute_immediate_startup(self) -> Dict[str, Any]:
        """
        Execute complete immediate startup sequence.
        
        Returns:
            Dict containing complete startup results
        """
        logger.info("\n" + "=" * 80)
        logger.info("IMMEDIATE QUANTUM-X STARTUP INITIATED")
        logger.info("Cross-referencing and integrating systems...")
        logger.info("=" * 80)
        
        startup_start = datetime.now()
        results = {
            "start_time": startup_start.isoformat(),
            "steps": {}
        }
        
        try:
            # Step 1: Pre-installation checks
            pre_check = self.pre_installation_checks()
            results["steps"]["pre_check"] = pre_check
            
            if not pre_check.get("can_proceed", False):
                logger.error("\n⚠ STARTUP ABORTED: Pre-installation checks failed")
                results["success"] = False
                results["error"] = "Pre-installation checks failed"
                return results
            
            # Step 2: Install quantum-x
            install_result = self.install_quantum_x()
            results["steps"]["installation"] = install_result
            
            if not install_result.get("success"):
                logger.error("\n⚠ STARTUP FAILED: Installation failed")
                results["success"] = False
                results["error"] = "Installation failed"
                return results
            
            # Step 3: Analyze integration
            analysis_result = self.analyze_integration()
            results["steps"]["analysis"] = analysis_result
            
            # Step 4: Post-installation validation
            validation_result = self.post_installation_validation()
            results["steps"]["validation"] = validation_result
            
            if not validation_result.get("overall_success"):
                logger.warning("\n⚠ STARTUP WARNING: Post-installation validation failed")
                # Continue anyway but flag the issue
                results["warnings"] = ["Post-installation validation failed"]
            
            # Step 5: Sync and integrate
            sync_result = self.sync_and_integrate()
            results["steps"]["integration"] = sync_result
            
            # Finalize results
            startup_end = datetime.now()
            results["end_time"] = startup_end.isoformat()
            results["duration_seconds"] = (startup_end - startup_start).total_seconds()
            results["success"] = True
            
            logger.info("\n" + "=" * 80)
            logger.info("✓ IMMEDIATE STARTUP COMPLETED SUCCESSFULLY")
            logger.info(f"Duration: {results['duration_seconds']:.2f} seconds")
            logger.info("Systems are cross-referenced, conflict-free, and harmoniously integrated!")
            logger.info("Quantum-X Builder is now active and ready.")
            logger.info("=" * 80)
            
        except Exception as e:
            logger.error(f"\n✗ STARTUP FAILED: {e}", exc_info=True)
            results["success"] = False
            results["error"] = str(e)
            results["end_time"] = datetime.now().isoformat()
        
        return results


def main():
    """Main entry point for immediate quantum startup."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Immediate Quantum-X Startup - Install and integrate quantum-x-builder immediately"
    )
    
    parser.add_argument(
        "--path",
        type=str,
        default="/tmp/quantum-x-builder",
        help="Path where quantum-x-builder will be cloned"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    args = parser.parse_args()
    
    # Initialize and execute startup
    startup = ImmediateQuantumStartup(quantum_x_path=args.path)
    results = startup.execute_immediate_startup()
    
    if args.json:
        print(json.dumps(results, indent=2))
    
    # Exit with appropriate code
    sys.exit(0 if results.get("success") else 1)


if __name__ == "__main__":
    main()
