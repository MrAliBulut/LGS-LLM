"""
Session logging module for exam generation.
Creates a log file for each exam generation session with timestamp-based naming.
Tracks distribution, questions, image generation, and errors.
"""

import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional


class SessionLogger:
    """Logger for a single exam generation session"""
    
    def __init__(self, distribution: Dict[str, int], visual_count: int):
        """
        Initialize session logger with timestamp-based filename.
        
        Args:
            distribution: Topic distribution dict {topic: count}
            visual_count: Number of visual questions requested
        """
        # Create logs directory if it doesn't exist
        self.logs_dir = Path("logs")
        self.logs_dir.mkdir(exist_ok=True)
        
        # Create filename with date and time
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]  # Include milliseconds
        self.log_file = self.logs_dir / f"{timestamp}.json"
        
        # Initialize session data
        self.session_data = {
            "timestamp": datetime.now().isoformat(),
            "distribution": {
                "topics_requested": distribution,
                "total_questions": sum(distribution.values()),
                "visual_count_requested": visual_count
            },
            "distribution_logic": {},
            "questions": [],
            "images": [],
            "errors": []
        }
        
        # Write initial file
        self._write_log()
        print(f"[LOG] Session log created: {self.log_file}")
    
    def _write_log(self):
        """Write current session data to log file"""
        with open(self.log_file, 'w', encoding='utf-8') as f:
            json.dump(self.session_data, f, indent=2, ensure_ascii=False)
    
    def log_distribution_logic(self, visual_distribution: Dict[str, int], visual_indices: Dict[str, set]):
        """
        Log the visual distribution logic output.
        
        Args:
            visual_distribution: Final visual distribution {topic: count}
            visual_indices: Which indices are visual per topic
        """
        self.session_data["distribution_logic"] = {
            "visual_distribution": visual_distribution,
            "visual_indices": {topic: list(indices) for topic, indices in visual_indices.items()}
        }
        self._write_log()
        print(f"[LOG] Distribution logic logged")
    
    def log_question(self, question_id: str, topic: str, question_type: str, llm_response: Dict[str, Any]):
        """
        Log a generated question.
        
        Args:
            question_id: Question ID (e.g., "q1", "q2")
            topic: Question topic
            question_type: "visual" or "text"
            llm_response: Raw JSON response from LLM
        """
        question_log = {
            "id": question_id,
            "topic": topic,
            "type": question_type,
            "llm_response": llm_response
        }
        self.session_data["questions"].append(question_log)
        self._write_log()
        print(f"[LOG] Question {question_id} logged ({question_type})")
    
    def log_image_generation(
        self,
        question_id: str,
        model_type: str,
        llm_image_prompt: str,
        engineered_prompt: Dict[str, str],
        image_size_bytes: int
    ):
        """
        Log image generation details.
        
        Args:
            question_id: Question ID this image is for
            model_type: Image generation model ("chroma" or "zimage")
            llm_image_prompt: Raw prompt from LLM
            engineered_prompt: Structured prompt from prompt engine
                               For chroma: {positive_prompt, negative_prompt}
                               For zimage: {final_prompt}
            image_size_bytes: Size of generated image in bytes
        """
        image_log = {
            "question_id": question_id,
            "model": model_type,
            "llm_prompt": llm_image_prompt,
            "engineered_prompt": engineered_prompt,
            "image_size_bytes": image_size_bytes
        }
        self.session_data["images"].append(image_log)
        self._write_log()
        print(f"[LOG] Image generation logged for {question_id} (model={model_type}, size={image_size_bytes})")
    
    def log_error(self, error_location: str, error_type: str, error_message: str, context: Optional[Dict] = None):
        """
        Log an error that occurred during session.
        
        Args:
            error_location: Where error occurred (e.g., "image_generation", "question_generation")
            error_type: Type of error (e.g., "RuntimeError", "JSONDecodeError")
            error_message: Error message
            context: Additional context about the error
        """
        error_log = {
            "timestamp": datetime.now().isoformat(),
            "location": error_location,
            "type": error_type,
            "message": error_message,
            "context": context or {}
        }
        self.session_data["errors"].append(error_log)
        self._write_log()
        print(f"[LOG] Error logged: {error_location} - {error_type}: {error_message}")
    
    def log_completion(self, total_questions_sent: int, total_images_generated: int):
        """
        Log session completion.
        
        Args:
            total_questions_sent: Number of questions actually sent
            total_images_generated: Number of images generated
        """
        self.session_data["completion"] = {
            "timestamp": datetime.now().isoformat(),
            "total_questions_sent": total_questions_sent,
            "total_images_generated": total_images_generated,
            "total_errors": len(self.session_data["errors"])
        }
        self._write_log()
        print(f"[LOG] Session completed: {total_questions_sent} questions, {total_images_generated} images")


# Global session logger instance
_current_session: Optional[SessionLogger] = None


def create_session(distribution: Dict[str, int], visual_count: int) -> SessionLogger:
    """Create a new session logger"""
    global _current_session
    _current_session = SessionLogger(distribution, visual_count)
    return _current_session


def get_session() -> Optional[SessionLogger]:
    """Get current session logger"""
    return _current_session


def close_session():
    """Close current session"""
    global _current_session
    _current_session = None
