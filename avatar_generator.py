class AvatarGenerator:
    """
    Creates avatars from body scan data for real-time gameplay or visual representation.
    """
    def create_avatar(self, scan_data):
        if scan_data is None:
            raise ValueError("No body scan data provided.")
        # Minimal representation: scale the mesh data
        return {"mesh": scan_data * 0.1, "texture": "default"}