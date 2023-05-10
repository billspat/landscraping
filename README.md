ParkScrape

Example to pull images from google maps street view for vegetation

Python Library  https://rrwen.github.io/google_streetview/

Requires access to Google cloud with an active account.  Does not need to be a Gmail account. 

To get a key you create project in console.cloud.google.com, and enable the "StreetMaps Static" api.  At this point
it will require a billing account, so most university-enabled accounts will not have billing associated with it. 
However it does seem to work with the free trial. 


example shell session 

```
pip install google_streetview
GKEY=<THE KEY FROM google cloud console>
google_streetview -s key=$GKEY
GLAT=1.381491974459891
GLON=103.81287571755809

google_streetview -s key=$GKEY
google_streetview --location=$GLAT,$GLON  --size=640x640

```

Can also get metadata without using the python application, and at no cost to the quota. 

see https://developers.google.com/maps/documentation/streetview/metadata

`https://maps.googleapis.com/maps/api/streetview/metadata?location=<STRING>&key=YOUR_API_KEY&signature=<YOUR_SIGNATURE>`

"location — can be either a text string (such as Chagrin Falls, OH) or a comma-separated pair of latitude/longitude coordinates (40.457375,-80.009353)."

examle output: 

```json
{
   "copyright" : "© 2017 Google",
   "date" : "2016-05",
   "location" : {
      "lat" : 48.85783227207914,
      "lng" : 2.295226175151347
   },
   "pano_id" : "tu510ie_z4ptBZYo2BGEJg",
   "status" : "OK"
}
```

Given a bounding box, could we run through a grid of lat/long, and pull metadata, 
which would return if there is a streetview image at that location or not. 

Versus a script that would follow paths. 

The output lat/longs could be used to extract pano images. 




