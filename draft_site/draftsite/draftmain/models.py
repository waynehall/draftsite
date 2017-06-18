from django.db import models
import uuid


class Player (models.Model):
    player_name = models.CharField(max_length=100, unique=True)
    player_id = models.AutoField(primary_key=True)
    #this block will be for measurements
    #A block here for other non-stat info
    #percentages and advanced stats
    #everything will need normalized later
    player_TS = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_PER = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_OBPM = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_DBPM = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_WS48 = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_REBPCT = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_BLKPCT = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_3PTPCT = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_ASTPCT = models.DecimalField(max_digits=20, decimal_places=3, blank=True)
    player_STLPCT = models.DecimalField(max_digits=20, decimal_places=3, blank=True)

    def __str__(self):
        return self.player_name
# Create your models here.
