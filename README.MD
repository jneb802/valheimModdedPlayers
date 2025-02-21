# Valheim Modded Players

The goal of this app is identify how many modded Valheim players exist. 

This app runs a daily query on the [ThunderstoreAPI](https://thunderstore.io/api/docs/) to get the total downloads of the BepinEx Valheim Pack. The results are stored in downloads.json and then compared day-over-day. The assumption is that a new download of the BepinEx Valheim pack is a new modded valheim player because the BepinEx Valheim pack is required to play modded Valheim.