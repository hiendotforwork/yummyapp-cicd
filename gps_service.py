class GPSSignalLostError(Exception):
    pass


# Backward compatibility alias
GPSignalLostError = GPSSignalLostError

def get_current_location():
    return (10.0, 105.0)
    