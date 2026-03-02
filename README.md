# Aircraft Turnaround Time (TAT) Calculator

## Background
The "Turnaround" is the period between an aircraft arriving at a gate and departing for its next flight. Accurate TAT measurement is critical for airline operational efficiency.

## Your Task
Using the provided `data/Airplane_Video.mp4`, build a Computer Vision system that detects four key operational milestones:

1. **In-Block (Arrival):** When the plane comes to a complete stop at the gate.
2. **Ground Service Start:** When the first ground equipment (e.g., stairs, fuel truck) approaches the aircraft.
3. **Ground Service End:** When all ground equipment has cleared the aircraft area.
4. **Off-Block (Departure):** When the aircraft begins its pushback from the gate.

## Repository Structure
- `src/main.py`: The entry point that runs the video processing loop.
- `src/detector.py`: Where you will implement your object detection logic.
- `src/tracker.py`: Where you will implement temporal logic to track events.
- `src/utils.py`: Helper functions for visualization.
- `config/config.yaml`: Configuration parameters for thresholds and paths.
- `notebooks/exploration.ipynb`: A sandbox for data analysis and testing.

## Setup Instructions
1. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Data Check:** Ensure `data/Airplane_Video.mp4` is located in the `data/` directory.

## Execution

To run your implementation:
   ```bash
   python src/main.py
   ```

## Tips for Success

* **FPS Handling:** Use the exploration notebook to check the video's FPS. If you skip frames to save processing power (e.g., process every 5th frame), ensure your time calculations account for the jump.
* **In-Block Logic:** To detect "In-Block," compare the bounding box of the plane over several seconds. If the coordinates are stable ($\Delta < \text{threshold}$), the plane has arrived.
* **Proximity Detection:** Equipment "Arrival" can be defined by the intersection of the equipment's bounding box and the aircraft's area.
* **Visualize:** Use the commented-out lines in `src/main.py` to see your bounding boxes in real-time while you debug.
