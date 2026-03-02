class EventTracker:
    def __init__(self):
        self.events = {
            "in_block": None,
            "equipment_arrival": None,
            "equipment_departure": None,
            "off_block": None
        }

    def update(self, aircraft_box, equipment_boxes, timestamp):
        """
        Logic to decide if an event has occurred based on movement or proximity.
        """
        # TODO: Use the delta in bounding box positions to detect 'In-Block'
        # TODO: Use proximity of equipment to aircraft to detect 'Service Start'
        pass

    def get_summary(self):
        # TODO: Calculate Turnaround Time (Off-Block minus In-Block)
        return self.events
