"""
Auto-Recommendation System Module

Generates intelligent recommendations for system improvements,
code enhancements, and evolutionary strategies using AI-driven analysis.
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional
from datetime import datetime
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AutoRecommendationSystem:
    """
    AI-driven recommendation system for autonomous improvements.
    """
    
    def __init__(self):
        """Initialize the auto-recommendation system."""
        self.recommendation_history = []
        self.applied_recommendations = []
        self.recommendation_rules = self._initialize_rules()
        logging.info("AutoRecommendationSystem initialized")
    
    def _initialize_rules(self) -> Dict[str, Any]:
        """
        Initialize recommendation rules and patterns.
        
        Returns:
            Dict containing recommendation rules
        """
        return {
            "performance": {
                "high_latency": {
                    "threshold": 100,
                    "recommendations": [
                        "Implement caching for frequently accessed data",
                        "Optimize database queries with indexing",
                        "Use async operations for I/O-bound tasks",
                        "Profile code to identify bottlenecks"
                    ]
                },
                "high_cpu": {
                    "threshold": 80,
                    "recommendations": [
                        "Optimize computational algorithms",
                        "Implement multiprocessing for CPU-intensive tasks",
                        "Use more efficient data structures",
                        "Consider algorithm complexity reduction"
                    ]
                },
                "high_memory": {
                    "threshold": 85,
                    "recommendations": [
                        "Implement memory-efficient data structures",
                        "Add garbage collection optimization",
                        "Use generators for large datasets",
                        "Profile memory usage and fix leaks"
                    ]
                }
            },
            "code_quality": {
                "missing_docs": {
                    "threshold": 0.3,
                    "recommendations": [
                        "Add docstrings to all public functions and classes",
                        "Create comprehensive API documentation",
                        "Add inline comments for complex logic",
                        "Generate automated documentation with Sphinx"
                    ]
                },
                "high_complexity": {
                    "threshold": 500,
                    "recommendations": [
                        "Refactor large files into smaller modules",
                        "Extract complex functions into smaller ones",
                        "Apply SOLID principles for better modularity",
                        "Use design patterns for complex logic"
                    ]
                },
                "code_duplication": {
                    "threshold": 5,
                    "recommendations": [
                        "Extract common code into shared utilities",
                        "Use inheritance or composition to reduce duplication",
                        "Create reusable components and libraries",
                        "Apply DRY (Don't Repeat Yourself) principle"
                    ]
                }
            },
            "security": {
                "vulnerabilities": {
                    "recommendations": [
                        "Update packages with known vulnerabilities",
                        "Implement input validation and sanitization",
                        "Use parameterized queries to prevent SQL injection",
                        "Add authentication and authorization checks",
                        "Implement rate limiting and throttling",
                        "Use secure communication protocols (HTTPS, TLS)"
                    ]
                }
            },
            "testing": {
                "low_coverage": {
                    "threshold": 80,
                    "recommendations": [
                        "Increase test coverage to at least 80%",
                        "Add unit tests for critical functions",
                        "Implement integration tests for key workflows",
                        "Add end-to-end tests for user scenarios",
                        "Use property-based testing for edge cases"
                    ]
                }
            }
        }
    
    def analyze_metrics_for_recommendations(self, metrics: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Analyze metrics and generate recommendations.
        
        Args:
            metrics: System and code metrics
        
        Returns:
            List of recommendation dictionaries
        """
        logging.info("Analyzing metrics for recommendations...")
        
        recommendations = []
        
        # Performance recommendations
        if "cpu_percent" in metrics:
            if metrics["cpu_percent"] > self.recommendation_rules["performance"]["high_cpu"]["threshold"]:
                for rec in self.recommendation_rules["performance"]["high_cpu"]["recommendations"]:
                    recommendations.append({
                        "category": "performance",
                        "subcategory": "high_cpu",
                        "priority": "high",
                        "recommendation": rec,
                        "current_value": metrics["cpu_percent"],
                        "threshold": self.recommendation_rules["performance"]["high_cpu"]["threshold"]
                    })
        
        if "memory_percent" in metrics:
            if metrics["memory_percent"] > self.recommendation_rules["performance"]["high_memory"]["threshold"]:
                for rec in self.recommendation_rules["performance"]["high_memory"]["recommendations"]:
                    recommendations.append({
                        "category": "performance",
                        "subcategory": "high_memory",
                        "priority": "high",
                        "recommendation": rec,
                        "current_value": metrics["memory_percent"],
                        "threshold": self.recommendation_rules["performance"]["high_memory"]["threshold"]
                    })
        
        # Code quality recommendations
        if "missing_docstrings" in metrics and "python_files" in metrics:
            if metrics["python_files"] > 0:
                doc_ratio = metrics["missing_docstrings"] / metrics["python_files"]
                if doc_ratio > self.recommendation_rules["code_quality"]["missing_docs"]["threshold"]:
                    for rec in self.recommendation_rules["code_quality"]["missing_docs"]["recommendations"]:
                        recommendations.append({
                            "category": "code_quality",
                            "subcategory": "missing_docs",
                            "priority": "medium",
                            "recommendation": rec,
                            "current_value": doc_ratio,
                            "threshold": self.recommendation_rules["code_quality"]["missing_docs"]["threshold"]
                        })
        
        if "complexity_issues" in metrics:
            if len(metrics["complexity_issues"]) > self.recommendation_rules["code_quality"]["high_complexity"]["threshold"] / 100:
                for rec in self.recommendation_rules["code_quality"]["high_complexity"]["recommendations"]:
                    recommendations.append({
                        "category": "code_quality",
                        "subcategory": "high_complexity",
                        "priority": "medium",
                        "recommendation": rec,
                        "issues_count": len(metrics["complexity_issues"])
                    })
        
        logging.info(f"Generated {len(recommendations)} recommendations")
        return recommendations
    
    def generate_evolutionary_strategy(self, 
                                       diagnosis_result: Dict[str, Any],
                                       analysis_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate comprehensive evolutionary strategy.
        
        Args:
            diagnosis_result: Results from self-diagnosis
            analysis_result: Results from code analysis
        
        Returns:
            Dict containing evolutionary strategy
        """
        logging.info("Generating evolutionary strategy...")
        
        # Combine metrics from all sources
        combined_metrics = {}
        
        if "resource_check" in diagnosis_result:
            combined_metrics.update(diagnosis_result["resource_check"])
        
        if "code_health" in diagnosis_result:
            combined_metrics.update(diagnosis_result["code_health"])
        
        if "metrics" in analysis_result:
            combined_metrics.update(analysis_result["metrics"])
        
        # Generate recommendations
        recommendations = self.analyze_metrics_for_recommendations(combined_metrics)
        
        # Prioritize recommendations
        high_priority = [r for r in recommendations if r.get("priority") == "high"]
        medium_priority = [r for r in recommendations if r.get("priority") == "medium"]
        low_priority = [r for r in recommendations if r.get("priority") == "low"]
        
        # Group by category
        categorized = defaultdict(list)
        for rec in recommendations:
            categorized[rec["category"]].append(rec)
        
        strategy = {
            "timestamp": datetime.now().isoformat(),
            "total_recommendations": len(recommendations),
            "high_priority_count": len(high_priority),
            "medium_priority_count": len(medium_priority),
            "low_priority_count": len(low_priority),
            "recommendations_by_priority": {
                "high": high_priority,
                "medium": medium_priority,
                "low": low_priority
            },
            "recommendations_by_category": dict(categorized),
            "implementation_plan": self._create_implementation_plan(recommendations)
        }
        
        self.recommendation_history.append(strategy)
        
        logging.info(f"Evolutionary strategy generated with {len(recommendations)} recommendations")
        return strategy
    
    def _create_implementation_plan(self, recommendations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Create a prioritized implementation plan.
        
        Args:
            recommendations: List of recommendations
        
        Returns:
            List of implementation steps
        """
        # Sort by priority
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_recs = sorted(
            recommendations,
            key=lambda x: priority_order.get(x.get("priority", "low"), 3)
        )
        
        plan = []
        for i, rec in enumerate(sorted_recs[:20], 1):  # Top 20 recommendations
            plan.append({
                "step": i,
                "category": rec["category"],
                "priority": rec.get("priority", "medium"),
                "action": rec["recommendation"],
                "estimated_impact": self._estimate_impact(rec),
                "estimated_effort": self._estimate_effort(rec)
            })
        
        return plan
    
    def _estimate_impact(self, recommendation: Dict[str, Any]) -> str:
        """
        Estimate the impact of a recommendation.
        
        Args:
            recommendation: Recommendation dictionary
        
        Returns:
            Impact level (high/medium/low)
        """
        if recommendation.get("priority") == "high":
            return "high"
        elif "security" in recommendation.get("category", ""):
            return "high"
        elif "performance" in recommendation.get("category", ""):
            return "medium"
        else:
            return "low"
    
    def _estimate_effort(self, recommendation: Dict[str, Any]) -> str:
        """
        Estimate the effort required for a recommendation.
        
        Args:
            recommendation: Recommendation dictionary
        
        Returns:
            Effort level (high/medium/low)
        """
        rec_text = recommendation.get("recommendation", "").lower()
        
        if any(word in rec_text for word in ["refactor", "redesign", "rewrite", "comprehensive"]):
            return "high"
        elif any(word in rec_text for word in ["implement", "add", "create"]):
            return "medium"
        else:
            return "low"
    
    def get_next_recommended_action(self) -> Optional[Dict[str, Any]]:
        """
        Get the next recommended action to take.
        
        Returns:
            Next action dictionary or None
        """
        if not self.recommendation_history:
            return None
        
        latest_strategy = self.recommendation_history[-1]
        implementation_plan = latest_strategy.get("implementation_plan", [])
        
        # Find first action not yet applied
        for action in implementation_plan:
            if action not in self.applied_recommendations:
                return action
        
        return None
    
    def mark_recommendation_applied(self, recommendation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Mark a recommendation as applied.
        
        Args:
            recommendation: Recommendation that was applied
        
        Returns:
            Dict containing status
        """
        self.applied_recommendations.append({
            "recommendation": recommendation,
            "applied_at": datetime.now().isoformat()
        })
        
        logging.info(f"Marked recommendation as applied: {recommendation.get('action', 'unknown')}")
        
        return {
            "success": True,
            "total_applied": len(self.applied_recommendations),
            "timestamp": datetime.now().isoformat()
        }
    
    def get_recommendation_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about recommendations.
        
        Returns:
            Dict containing recommendation statistics
        """
        total_recommendations = sum(
            strategy.get("total_recommendations", 0)
            for strategy in self.recommendation_history
        )
        
        return {
            "total_strategies_generated": len(self.recommendation_history),
            "total_recommendations": total_recommendations,
            "total_applied": len(self.applied_recommendations),
            "application_rate": (
                len(self.applied_recommendations) / total_recommendations * 100
                if total_recommendations > 0 else 0
            ),
            "latest_strategy": self.recommendation_history[-1] if self.recommendation_history else None,
            "timestamp": datetime.now().isoformat()
        }


if __name__ == "__main__":
    # Example usage
    recommender = AutoRecommendationSystem()
    
    # Sample metrics
    sample_diagnosis = {
        "resource_check": {
            "cpu_percent": 85,
            "memory_percent": 75,
            "disk_percent": 65
        },
        "code_health": {
            "python_files": 20,
            "missing_docstrings": 12,
            "complexity_issues": [{"file": "test.py", "lines": 600}]
        }
    }
    
    sample_analysis = {
        "metrics": {
            "total_files": 50,
            "total_lines": 15000
        }
    }
    
    # Generate strategy
    strategy = recommender.generate_evolutionary_strategy(sample_diagnosis, sample_analysis)
    print("Evolutionary Strategy:")
    print(json.dumps(strategy, indent=2))
    
    # Get next action
    next_action = recommender.get_next_recommended_action()
    if next_action:
        print("\nNext Recommended Action:")
        print(json.dumps(next_action, indent=2))
    
    # Get statistics
    stats = recommender.get_recommendation_statistics()
    print("\nRecommendation Statistics:")
    print(json.dumps(stats, indent=2))
