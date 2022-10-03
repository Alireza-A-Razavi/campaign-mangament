class CampaignStatus:
    NOT_CONFIRMED = "not confirmed"
    RUNNING = "running" # tha campaing is confirmed by admin and is still open for signing 
    SUCCESSFUL = "successful" 
    FAILDED = "failed"
    
    CHOICES = [
        (NOT_CONFIRMED, "Not confirmed yet"),
        (SUCCESSFUL, "Campain was successful"),
        (FAILDED, "Campain has failed"),
        (RUNNING, "Running"),
    ]